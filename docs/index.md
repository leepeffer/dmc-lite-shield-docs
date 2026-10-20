# DMC Lite Shield owner's guide

The shield connects Dragonframe to up to eight external motor drivers. It mounts on an Arduino GIGA R1 WiFi and adds motor signal outputs, camera contacts, a relay, a logic trigger and switch inputs.

**Check your board first:** this guide covers the **V2 socketed DIP prototype**, with four removable 16-pin driver ICs. It does not cover V1 or a surface-mount driver revision. As of October 20, 2026, the first prototype is in production; operating tests and the firmware installed on a delivered board remain unconfirmed.

> **Image placeholder — board tour:** top view identifying RJ45 channels 1–8, DB37, J5 controls, J6 camera, driver sockets and pin-1 marks. Connector close-ups will show the viewing direction explicitly.

## What do you want to do?

| Task | Guide |
|---|---|
| Connect and move your first axis | [First setup](getting-started/overview.md) |
| Make or check a cable | [Pinouts and wiring](hardware/wiring.md) |
| Understand a light | [LED indicators](hardware/indicators.md) |
| Replace a damaged driver chip | [Replacement parts and procedure](hardware/driver-replacement.md) |
| Trigger a camera accessory or work light | [Triggers, switches and relay](setup/triggers.md) |
| Connect a stop button | [E-stop input](setup/estop.md) |
| Install or update firmware | [Firmware](setup/firmware.md) |
| Diagnose a problem | [Troubleshooting](troubleshooting.md) |

The shield sends control signals; external drivers supply motor power. Its RJ45 ports are **not Ethernet**. Turn off and disconnect power before changing cables or removing ICs.
