# DMC Lite Shield — owner's manual

Public documentation for the **V2 socketed DIP shield** used with Arduino GIGA R1 WiFi and Dragonframe.

Start with the [owner's guide](docs/index.md). Find [connector pinouts](docs/hardware/wiring.md), [LED meanings](docs/hardware/indicators.md), [replacement drivers](docs/hardware/driver-replacement.md), and [triggers, switches and relays](docs/setup/triggers.md).

This edition describes the October 16, 2026 V2 prototype design. Hardware acceptance testing and the installed firmware configuration are not yet documented. It must not be read as a tested production release or as instructions for V1.

## Edit and preview

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
mkdocs build --strict
```

Add pages to `mkdocs.yml`. Annotated CAD views and wiring diagrams illustrate the guide; see [illustration sources](docs/image-plan.md). Keep wiring labels anchored to verified connector pin numbers, never an assumed left-to-right view.

GitHub Actions builds on pull requests and deploys main through GitHub Pages when Pages is configured. Repository: [leepeffer/dmc-lite-shield-docs](https://github.com/leepeffer/dmc-lite-shield-docs). Content license: [CC BY 4.0](LICENSE). External manuals retain their own licenses. This repository contains customer documentation and preconfigured V2 sketch downloads, not manufacturing files. The project owner confirmed permission to redistribute the modified Dragonframe/DZED sketches on November 5, 2026. Those downloads retain their original copyright notices and are not covered by this documentation’s CC BY 4.0 license.
