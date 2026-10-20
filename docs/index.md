---
hide:
  - navigation
  - toc
---

# DMC Lite Shield owner's guide

Find the connection, understand the light, then follow the setup. This visual guide covers the **V2 socketed DIP board** and Arduino GIGA R1 WiFi.

[![V2 top-view board tour: camera, replaceable drivers, controls, eight RJ45 ports, DB37 and indicators.](assets/images/board-tour.svg)](assets/images/board-tour.svg)

*Tap or click to enlarge.*

[Start with one axis](getting-started/overview.md) · [All pinouts](hardware/wiring.md) · [Troubleshooting](troubleshooting.md)

## What does that light mean?

[![Each board LED located and explained; STEP lights show activity, not motor position.](assets/images/led-map.svg)](assets/images/led-map.svg)

*Tap or click to enlarge.*

[Read the indicator guide](hardware/indicators.md). The red E-stop light follows the contact state; it does not certify that motion has stopped.

## Connect buttons, triggers and the relay

[![Seven J5 terminals numbered in top-view orientation, with relay contacts distinguished from logic power.](assets/images/control-terminal.svg)](assets/images/control-terminal.svg)

*Tap or click to enlarge.*

[Wiring examples and Dragonframe events](setup/triggers.md) · [Stop-button setup](setup/estop.md)

## Replace a damaged driver

[![Four driver sockets mapped to pairs of channels, with pin-1 orientation.](assets/images/driver-map.svg)](assets/images/driver-map.svg)

*Tap or click to enlarge.*

Buy **TI AM26C31INE4 / AM26C31IN, 16-pin PDIP (N)** for this socketed version. [Follow the replacement procedure](hardware/driver-replacement.md) before removing a chip.

## Put the Dragonframe sketch on the Arduino

[![Visual sequence for finding and uploading the paired M7 and M4 sketches.](assets/images/flashing-workflow.svg)](assets/images/flashing-workflow.svg)

*Tap or click to enlarge.*

[Open the step-by-step flashing guide](setup/firmware.md) for macOS, Windows and Linux folder navigation, IDE settings and troubleshooting.

## Before you power up

The shield sends control signals; external drivers supply motor power. **RJ45 is not Ethernet.** Disconnect power before changing cables or removing ICs.

These are CAD views of the October 16, 2026 V2 socketed DIP design. They do not document assembly or operating tests. First-board acceptance results, delivered firmware configuration and camera plug wiring remain unconfirmed. V1 and surface-mount versions need their own instructions. [Sources and illustration notes](image-plan.md).
