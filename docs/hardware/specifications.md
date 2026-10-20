# Hardware at a glance

Applies to the October 16, 2026 **V2 socketed DIP** design.

| Feature | Interface |
|---|---|
| Host board | Arduino GIGA R1 WiFi |
| Motion channels | 8 STEP/DIR channels |
| RJ45 outputs | Complementary STEP+/STEP− and DIR+/DIR−, 5 V line-driver supply |
| DB37 outputs | Single-ended positive STEP/DIR signals for the same eight channels |
| Replaceable line drivers | Four TI AM26C31INE4, 16-pin PDIP; two axes per IC |
| Control terminal | J5: GND, LOG2, relay contacts, SWITCH, E-stop, GND |
| Camera interface | J6 2.5 mm jack; separate meter and shutter contact closures |
| Shield power | GIGA power rails; no motor-power output |
| Indicators | Power, eight STEP activity lights, relay drive, LOG2, switch and E-stop input |

“5 V” describes the output stage supply, not a guaranteed unloaded-to-loaded voltage at every receiver. LOG2 includes a 1 kΩ series resistor; receiver loading matters. GIGA GPIO itself operates at 3.3 V.

The accessory +5 V pins have no published qualified load budget. Do not power motors or unspecified accessories from them, or back-feed them from another supply. Relay contact load ratings, cable-length limits, board temperature limits and complete-system performance are not yet qualified for this prototype.

The dmc-lite system supports eight axes, without DMC crane virtualization or a DMX output port. The Dragonframe manual lists a 50 kHz maximum STEP rate for the sketch; this is not a measured signal-integrity rating for the shield/cable/receiver combination. See [references](../references.md).

All connector assignments are in [wiring](wiring.md). Firmware support is separate from electrical connectivity: SWITCH and E-stop require configuration.
