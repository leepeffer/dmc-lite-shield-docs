# Planned illustrations

Text placeholders mark the intended positions in the manual. Images will be added after the assembled V2 board is available. The tables remain the authoritative text alongside each image.

Use a real board photograph or a verified CAD rendering as the base. Keep physical components, traces, connector positions and pin counts unchanged when adding callouts. Label a rendering as a rendering. Do not invent cable orientation, pin-1 marks or LED locations with generative artwork.

| Image | Required callouts | Page |
|---|---|---|
| Board tour | V2 revision, eight RJ45 channels, DB37, J5, J6, four driver sockets | [Home](index.md) |
| LED map | D11 power; D3 and D18–D24 STEP channels; D26 relay; D27 LOG2; D28 switch; D1 grounded E-stop input | [Indicators](hardware/indicators.md) |
| Connector views | Mating face versus board view, latch/key, pin 1, all RJ45 and DB37 pins | [Wiring](hardware/wiring.md) |
| J5 close-up | All seven numbered positions; input/output direction; relay pair bracket; example button wiring | [Triggers](setup/triggers.md) |
| Driver service | U1/U2/U5/U6 channel pairs, verified PCB pin 1 and IC notch alignment | [Replacement](hardware/driver-replacement.md) |
| Camera cable | Measured J6 pad-to-plug mapping and named camera cable | [Wiring](hardware/wiring.md) |
| Stop wiring | Separate NO and NC diagrams with firmware mode and normal/pressed/broken-wire states | [E-stop](setup/estop.md) |
| Sketch locations | Finder / File Explorer installation folder, README and both sketch folders | [Flashing](setup/firmware.md) |
| Arduino uploads | M7/M4 target cores, flash split, port, Upload button and success result | [Flashing](setup/firmware.md) |
| Dragonframe connection | Connected dmc-lite, ArcMoco assignment, port selector | [Dragonframe](setup/dragonframe.md) |
| Dragonframe triggers | Actual connected output selectors and confirmed physical mapping | [Triggers](setup/triggers.md) |

Keep one consistent board orientation for overview images. Use numbered callouts plus text, not color alone. If a component is on the underside, use a clearly labeled bottom-view inset. Check every arrow against the component reference and net assignment before publication. Photograph unpowered hardware for wiring/service views; any powered LED photo needs a caption stating the test condition.
