# V2 board test checklist

A practical check that the board works with your setup. Tick **Pass** or **Fail** as you go. If you cannot test something, leave it blank and add a quick note.

!!! warning "Check your motor cables"
    V2 RJ45 pins **2 and 6 are not grounds**. Check old cables before using them; these ports are not Ethernet. See [V2 pinouts](hardware/wiring.md), [firmware setup](setup/firmware.md) and [E-stop setup](setup/estop.md).

??? info "Before testing: enable E-stop and the external button"
    Open **`dmc_m7.ino` → `config.h`** in Arduino IDE. Under `#ifdef ARDUINO_ARCH_MBED_GIGA`, remove the `//` from these existing lines:

    ```cpp
    #define KILL_SWITCH_PIN D48
    #define LOGIC_SWITCH_PIN D49
    ```

    Enable only the inputs you are using. Edit the existing lines—do not add duplicates or change the Portenta section.

    - **E-stop:** connect J5 **6** to GND through the stop contact. The default above stops when the contact **closes**.
    - **Normally-closed E-stop:** in the official Dragonframe 2026 sketches, also uncomment `#define KILL_SWITCH_NORMALLY_CLOSED 1`. This stops when the contact **opens**. Leave this line commented for a normally-open contact. Older sketches may not support it.
    - **External button:** normally-open button between J5 **5** and GND. Choose its action in Dragonframe’s **Scene → Triggers**.

    Use J5 **1 or 7** for GND; do not feed voltage into either input. Test stop behavior before moving motors.

    **Relay, LOG2, differential motor outputs and activity lights need no extra enable lines.** Keep the standard V2 output pins: `LOGIC_OUT_0 D40` (relay) and `LOGIC_OUT_1 D41` (LOG2). Set output events in Dragonframe. No M4 edits are needed for these features.

    **Upload the changes:** with motor power off, upload M7 to **Main core**. For a fresh setup or firmware version change, also upload its matching M4 sketch to **M4 Co-processor**. Use **1.5MB M7 + 0.5MB M4** for both. If the matching M4 is already installed, this M7-only settings change needs only an M7 upload.

    [Full firmware instructions](setup/firmware.md#v2-input-and-output-settings) · [E-stop wiring and polarity](setup/estop.md)

<div id="board-checklist">
<noscript>Enable JavaScript to save progress and download results. Printed checkboxes can still be used as a paper checklist.</noscript>
<div class="test-tools" hidden>
<label for="test-record">Board test record</label>
<select id="test-record"></select>
<button type="button" id="test-new">New board test</button>
<button type="button" id="test-download">Download results</button>
<button type="button" id="test-print">Print / save PDF</button>
</div>
<p id="test-save" role="status">Progress saves in this browser only. Download results to share or keep a backup. Clearing browser data removes saved tests.</p>
<p id="test-progress" role="status"></p>
<div class="test-fields">
<label>Tester<input data-field="tester" type="text" autocomplete="off"></label>
<label>Board name / number<input data-field="board" type="text" autocomplete="off"></label>
<label>Test date<input data-field="date" type="date" autocomplete="off"></label>
<label>Motor / driver used<input data-field="drivers" type="text" autocomplete="off"></label>
<label>Camera / cable<input data-field="camera" type="text" autocomplete="off"></label>
</div>
<section class="test-section"><h2 id="test-stage-1">1. Quick look</h2><p>With power disconnected, check the board and fit it to the GIGA.</p>
<div class="test-row" data-test="s1-1"><p id="s1-1">Board looks undamaged, with no loose parts or bent pins.</p><div class="test-options" role="group" aria-labelledby="s1-1"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<div class="test-row" data-test="s1-2"><p id="s1-2">All four driver chips are seated and facing the correct way.</p><div class="test-options" role="group" aria-labelledby="s1-2"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<div class="test-row" data-test="s1-3"><p id="s1-3">Board fits securely on the GIGA without forcing it or touching other components.</p><div class="test-options" role="group" aria-labelledby="s1-3"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<label class="test-notes">Notes (optional)<textarea data-field="notes-1" rows="2"></textarea></label></section>
<section class="test-section"><h2 id="test-stage-2">2. Connect</h2><p>Start with motor power off. Use V2 firmware on both cores; enable the E-stop and switch options for those tests.</p>
<div class="test-row" data-test="s2-3"><p id="s2-3">Board powers up and connects to Dragonframe normally.</p><div class="test-options" role="group" aria-labelledby="s2-3"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<label class="test-notes">Notes (optional)<textarea data-field="notes-2" rows="2"></textarea></label></section>
<section class="test-section"><h2 id="test-stage-3">3. Stop and restart</h2><p>Test slowly, with room to move and a way to cut motor power. The board’s E-stop input does not cut motor power itself.</p>
<div class="test-row" data-test="s3-1"><p id="s3-1">E-stop stops the moving motors.</p><div class="test-options" role="group" aria-labelledby="s3-1"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<div class="test-row" data-test="s3-2"><p id="s3-2">Releasing E-stop does not restart movement by itself.</p><div class="test-options" role="group" aria-labelledby="s3-2"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<div class="test-row" data-test="s3-4"><p id="s3-4">Restarting the board and reconnecting USB causes no unexpected movement or triggers.</p><div class="test-options" role="group" aria-labelledby="s3-4"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<label class="test-notes">Notes (optional)<textarea data-field="notes-3" rows="2"></textarea></label></section>
<section class="test-section"><h2 id="test-stage-4">4. Try each motor port</h2><p>For each port: move both ways, try a slow and a normal working speed, check the matching blue light, and return to the starting point. Look for smooth movement without jumps or stalls. Power down before swapping cables.</p>
<div class="test-row" data-test="s4-1"><p id="s4-1">Channel 1 works correctly.</p><div class="test-options" role="group" aria-labelledby="s4-1"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<div class="test-row" data-test="s4-2"><p id="s4-2">Channel 2 works correctly.</p><div class="test-options" role="group" aria-labelledby="s4-2"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<div class="test-row" data-test="s4-3"><p id="s4-3">Channel 3 works correctly.</p><div class="test-options" role="group" aria-labelledby="s4-3"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<div class="test-row" data-test="s4-4"><p id="s4-4">Channel 4 works correctly.</p><div class="test-options" role="group" aria-labelledby="s4-4"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<div class="test-row" data-test="s4-5"><p id="s4-5">Channel 5 works correctly.</p><div class="test-options" role="group" aria-labelledby="s4-5"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<div class="test-row" data-test="s4-6"><p id="s4-6">Channel 6 works correctly.</p><div class="test-options" role="group" aria-labelledby="s4-6"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<div class="test-row" data-test="s4-7"><p id="s4-7">Channel 7 works correctly.</p><div class="test-options" role="group" aria-labelledby="s4-7"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<div class="test-row" data-test="s4-8"><p id="s4-8">Channel 8 works correctly.</p><div class="test-options" role="group" aria-labelledby="s4-8"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<div class="test-row" data-test="s4-11"><p id="s4-11">Several motors run together without problems.</p><div class="test-options" role="group" aria-labelledby="s4-11"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<div class="test-row" data-test="s4-10"><p id="s4-10">DB37 works too, if you plan to use it.</p><div class="test-options" role="group" aria-labelledby="s4-10"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<label class="test-notes">Notes (optional)<textarea data-field="notes-4" rows="2"></textarea></label></section>
<section class="test-section"><h2 id="test-stage-5">5. Try the extras</h2><p>Test with the accessories you have. Check what the accessory actually does, not just the indicator light.</p>
<div class="test-row" data-test="s5-1"><p id="s5-1">LOG1 relay switches the connected accessory on and off.</p><div class="test-options" role="group" aria-labelledby="s5-1"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<div class="test-row" data-test="s5-2"><p id="s5-2">LOG2 triggers its connected accessory.</p><div class="test-options" role="group" aria-labelledby="s5-2"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<div class="test-row" data-test="s5-4"><p id="s5-4">External button performs the expected action without unwanted repeats.</p><div class="test-options" role="group" aria-labelledby="s5-4"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<div class="test-row" data-test="s5-5"><p id="s5-5">Camera focus/meter and shutter work through a short shooting sequence.</p><div class="test-options" role="group" aria-labelledby="s5-5"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<label class="test-notes">Notes (optional)<textarea data-field="notes-5" rows="2"></textarea></label></section>
<section class="test-section"><h2 id="test-stage-6">6. Run a real sequence</h2><p>Run a typical shoot with movement, camera and any accessories. Let it run long enough to see whether it behaves consistently; no fixed duration needed.</p>
<div class="test-row" data-test="s6-2"><p id="s6-2">Sequence runs without disconnects, missed shots or motors drifting from their expected positions.</p><div class="test-options" role="group" aria-labelledby="s6-2"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<div class="test-row" data-test="simple-restart"><p id="simple-restart">After switching off and back on, the board still works normally.</p><div class="test-options" role="group" aria-labelledby="simple-restart"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<label class="test-notes">Notes (optional)<textarea data-field="notes-6" rows="2"></textarea></label></section>
<section class="test-section"><h2 id="test-stage-7">7. Wrap up</h2><p>Note anything odd, anything you could not test, and the setup you used. Download the results to share.</p>
<div class="test-row" data-test="simple-wrap"><p id="simple-wrap">Any problems have been fixed and rechecked, or clearly noted for follow-up.</p><div class="test-options" role="group" aria-labelledby="simple-wrap"><label><input type="checkbox" data-result="pass"> Pass</label><label><input type="checkbox" data-result="fail"> Fail</label></div></div>
<label class="test-notes">Notes (optional)<textarea data-field="notes-7" rows="2"></textarea></label></section>
</div>

For the V2 socketed DIP board. These are hands-on functional checks; electrical measurements remain a separate engineering check.
