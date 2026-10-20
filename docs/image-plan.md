# Illustration sources and remaining views

The guide now includes four faded-context component views (RJ45 ports, DB37, driver ICs and J5), a board tour, LED map, J5 close-up, driver-service map, RJ45 and DB37 function maps, camera contacts, trigger wiring, E-stop states, firmware workflow and system connections. A three-quarter CAD view is included in [first setup](getting-started/overview.md).

## What the images show

- **Top view:** supplied by Lee on October 20, 2026, from Fusion's V2 DIP board. Its source pixels are retained unchanged in `assets/images/board-top-source.png`.
- **Three-quarter view:** captured directly from the open `dmc_lite_shield-DIP-v2` Fusion document on October 20, 2026. Source retained in `assets/images/board-isometric.png`.
- **Callouts:** SVG overlays and view crops retain the CAD image geometry. Numbering and component references were checked against the archived V2 board and pin map.
- **Wiring/workflow diagrams:** explanatory vector drawings, not software screenshots or physical connector mating-face drawings.

The source model is not an assembled-board photograph. Generic component models, colors and socket/IC appearances do not prove installed parts or LED illumination. The diagrams describe the circuit; physical operation still needs testing. Click any figure to open its full-resolution SVG.

## Reading the annotations

J5 is shown in the same top-view orientation as the board: **pin 7 at the top, pin 1 at the bottom**. The printed `RELAY+` / `RELAY−` labels describe two floating contacts; they are not powered outputs. Driver pin 1 is the upper-left socket contact in this top view. Check the real PCB mark before inserting an IC.

RJ45 and DB37 images give logical pin assignments, without asserting a mating-face numbering convention. J6 shows PCB contact functions only; tip/ring/sleeve remains unverified. LED rings are position markers, not simulated illumination. In the four component-focus views, a white SVG overlay fades the surrounding board while the selected component regions retain their original pixels; no hardware geometry is regenerated.

## Still to capture or verify

| View | Needed evidence |
|---|---|
| RJ45 and DB37 numbered mating faces | Connector drawing plus physical orientation check |
| Camera cable tip/ring/sleeve | Continuity measurements and a named camera cable |
| Actual assembled-board photograph | Received hardware; visible revision and installed IC orientation |
| Finder / File Explorer sketch location | Platform-specific screenshots from the installed release |
| Arduino upload dialogs | M7/M4 target settings and actual successful uploads |
| Dragonframe trigger controls | Connected V2 and confirmed LOG1/LOG2/input mapping |

## Rebuilding vector figures

From the repository root, run `python3 tools/build_guide_figures.py`. This regenerates the fifteen annotated and explanatory SVG figures from the preserved source screenshot. The three-quarter view wrapper is a separate static SVG. Review changed arrows against the CAD before publication; never infer a pinout from an attractive illustration.

## Phone layouts

Wide figures have mobile alternatives: cropped views plus normal HTML captions and tables. They preserve the same image coordinates and component markers. `build_guide_figures.py` also regenerates these detail views. Full diagrams remain available through a link; desktop readers retain the original figures.
