# Troubleshooting

Disconnect power immediately if you see smoke, smell overheating or find a hot/damaged component. Identify the wiring fault before fitting replacement parts.

| Symptom | Check first | Next step |
|---|---|---|
| No power light | GIGA supply, USB cable, header alignment | Disconnect power before inspecting or reseating the shield |
| Power light on, no Dragonframe connection | Data-capable USB cable, correct serial port, other apps using port | Confirm both dmc-lite cores and [connection settings](setup/dragonframe.md) |
| STEP light active, motor still | External driver supply, enable, motor wiring and channel assignment | Check receiver compatibility and signal cable; LED is not motion feedback |
| No STEP light during jog | Correct controller/channel, stop state, firmware | Test one axis; if needed inspect STEP pulses with suitable equipment |
| Wrong direction | Axis direction setting | Change software direction; never swap STEP and DIR |
| Wrong distance | Microsteps, gearing and axis units | Measure a short move and recalibrate scale |
| Missed steps or rough motion | Acceleration, speed, motor current, load and binding | Reduce speed; check receiver wiring, supply and cooling |
| Two channels faulty | Shared U1/U2/U5/U6 and common cabling/power | Use the [driver map](hardware/driver-replacement.md); rule out wiring before replacing an IC |
| D26 on, device not triggered | Relay contact continuity and receiver wiring | D26 indicates coil drive only; check the selected event and hold time |
| D27 on, no logic response | LOG2/GND wiring, receiver threshold and load | Measure the terminal; its series resistor can reduce loaded voltage |
| D28 changes, no button action | D49 option enabled and uploaded | Check Scene → Triggers input/action assignment |
| Red E-stop LED behaves “backwards” | Normally-open versus normally-closed firmware | Read the [E-stop state table](setup/estop.md); LED shows contact grounding |
| E-stop does not inhibit motion | D48 option, firmware mode, wiring | Disable motor power; verify open, closed and disconnected states |
| Camera does not release | Camera-specific cable, remote settings, contact mapping | Verify continuity unpowered; J6 pad numbers are not plug pin names |

A multimeter can check continuity with power off and static voltages, but cannot reliably characterize short STEP pulses or timing. Use suitable test equipment or seek assistance for signal diagnosis. Do not ground a differential negative output while testing.

For [support](support.md), record the board revision, firmware configuration, Dragonframe version, external driver model, affected channel and exact symptoms. Clear photos of wiring and IC orientation help.
