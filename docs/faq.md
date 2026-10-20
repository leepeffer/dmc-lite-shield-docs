# Frequently asked questions

## Which replacement driver chip do I buy?

For V2 socketed DIP: **TI AM26C31INE4**, 16-pin PDIP (N), or TI's equivalent **AM26C31IN** ordering code. Follow the [replacement guide](hardware/driver-replacement.md). This is the shield's signal IC, not the external motor power driver.

## Can I plug the RJ45 ports into a network?

No. They carry motion signals and accessory +5 V, not Ethernet. See [pinouts](hardware/wiring.md).

## Does the shield power my motors?

No. Each motor needs an external driver and suitable motor supply. Do not use the connector's +5 V accessory pins for motor power.

## Does a channel LED prove the motor moved?

No. It shows STEP signal activity, without position or driver feedback. See [LED meanings](hardware/indicators.md).

## Is the relay another independent trigger beyond LOG1 and LOG2?

No. **LOG1 drives the relay**; LOG2 is available at J5 pin 2. Relay pins 3/4 are a floating contact pair, not voltage outputs.

## Can I use a button to shoot a frame?

Yes, with the SWITCH input enabled in firmware and the action assigned in Dragonframe. Wire a normally open button from J5 pin 5 to GND; see [triggers](setup/triggers.md).

## Does the stop button cut motor power?

No. It requests a firmware stop and must be enabled/configured. It is not a safety-rated power disconnect. See [E-stop setup](setup/estop.md).

## Is this the same as a DMC-32?

No. dmc-lite provides eight axes without crane virtualization or physical DMX output. Similar connector conventions do not establish all features or cable/load compatibility.

## Does this guide apply to V1?

No. It describes the October 16, 2026 V2 socketed DIP design. Confirm your revision before using the pinouts or service procedure.

## Are firmware, cables or the GIGA included?

Check your order and packing list. See [shipment checks](getting-started/whats-in-the-box.md). Availability, shipping estimates, warranty and bundle contents must come from the seller, not assumptions in this manual.
