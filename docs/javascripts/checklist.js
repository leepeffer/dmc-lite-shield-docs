(() => {
  'use strict';
  const root = document.getElementById('board-checklist');
  if (!root) return;
  const key = 'dmc-v2-board-tests-v1';
  const rows = [...root.querySelectorAll('[data-test]')];
  const fields = [...root.querySelectorAll('[data-field]')];
  const picker = root.querySelector('#test-record');
  const status = root.querySelector('#test-save');
  const fresh = () => ({ id: crypto.randomUUID(), fields: {}, results: {} });
  let state;
  let storageError = false;
  try {
    const raw = localStorage.getItem(key);
    if (raw) {
      state = JSON.parse(raw);
      if (!Array.isArray(state.records) || !state.records.length ||
          !state.records.every(r => r && typeof r.id === 'string' && r.fields && r.results)) {
        throw new Error('Invalid saved records');
      }
    }
  } catch (_) {
    storageError = true;
  }
  if (!state) { const record = fresh(); state = { active: record.id, records: [record] }; }
  let current = state.records.find(r => r.id === state.active) || state.records[0];
  function summary() {
    const pass = rows.filter(r => current.results[r.dataset.test] === 'pass').length;
    const fail = rows.filter(r => current.results[r.dataset.test] === 'fail').length;
    return `${pass} passed · ${fail} failed · ${rows.length - pass - fail} not tested.`;
  }
  function refreshPicker() {
    picker.replaceChildren(...state.records.map((r, i) => {
      const option = document.createElement('option');
      option.value = r.id;
      option.textContent = r.fields.board || `Board test ${i + 1}`;
      option.selected = r.id === current.id;
      return option;
    }));
  }
  function save() {
    state.active = current.id;
    try {
      if (storageError) throw new Error('Storage unavailable');
      localStorage.setItem(key, JSON.stringify(state));
      status.textContent = 'Saved in this browser only. Download results to share or back up. Clearing browser data removes saved tests.';
    } catch (_) {
      status.textContent = 'Progress could not be saved in this browser. Download results before leaving; existing stored data has not been replaced.';
    }
    root.querySelector('#test-progress').textContent = summary();
  }
  function render() {
    fields.forEach(f => { f.value = current.fields[f.dataset.field] || ''; });
    rows.forEach(row => row.querySelectorAll('[data-result]').forEach(input => {
      input.checked = current.results[row.dataset.test] === input.dataset.result;
    }));
    refreshPicker();
    save();
  }
  root.addEventListener('input', event => {
    const field = event.target;
    if (!field.dataset.field) return;
    current.fields[field.dataset.field] = field.value;
    if (field.dataset.field === 'board') refreshPicker();
    save();
  });
  root.addEventListener('change', event => {
    const input = event.target;
    if (!input.dataset.result) return;
    const row = input.closest('[data-test]');
    current.results[row.dataset.test] = input.checked ? input.dataset.result : '';
    row.querySelectorAll('[data-result]').forEach(other => {
      other.checked = current.results[row.dataset.test] === other.dataset.result;
    });
    save();
  });
  picker.addEventListener('change', () => {
    current = state.records.find(r => r.id === picker.value);
    render();
  });
  root.querySelector('#test-new').addEventListener('click', () => {
    current = fresh();
    state.records.push(current);
    render();
    root.querySelector('[data-field="board"]').focus();
  });
  root.querySelector('#test-download').addEventListener('click', () => {
    const lines = ['DMC Lite V2 — board test record', `Exported: ${new Date().toISOString()}`, summary(), ''];
    fields.filter(f => !f.dataset.field.startsWith('notes-')).forEach(f => {
      lines.push(`${f.parentElement.firstChild.textContent.trim()}: ${f.value || 'Not recorded'}`);
    });
    root.querySelectorAll('.test-section').forEach(section => {
      lines.push('', section.querySelector('h2').textContent, section.querySelector('p').textContent);
      section.querySelectorAll('[data-test]').forEach(row => {
        lines.push(`[${(current.results[row.dataset.test] || 'NOT TESTED').toUpperCase()}] ${row.querySelector('p').textContent}`);
      });
      lines.push(`Notes: ${section.querySelector('textarea').value || 'None recorded'}`);
    });
    const url = URL.createObjectURL(new Blob([lines.join('\n')], { type: 'text/plain;charset=utf-8' }));
    const link = document.createElement('a');
    link.href = url;
    link.download = `dmc-v2-${(current.fields.board || 'board-test').replace(/[^a-z0-9_-]/gi, '-').slice(0,80)}.txt`;
    link.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  });
  root.querySelector('#test-print').addEventListener('click', () => window.print());
  root.querySelector('.test-tools').hidden = false;
  render();
})();
