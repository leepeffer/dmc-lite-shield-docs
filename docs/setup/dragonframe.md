# Connect Dragonframe and test an axis

These steps follow the README supplied with Dragonframe 2026 dmc-lite. First complete [firmware installation](firmware.md) and check your [wiring](../hardware/wiring.md).

## Establish the connection

1. Connect the GIGA to the computer by USB. Start Dragonframe and open or create a scene.
2. Open **Scene → Connections…**.
3. Choose **Add Connection**, then **dmc-lite** as the device type.
4. Assign **ArcMoco #1** (or another unused ArcMoco slot).
5. Select the GIGA's serial port and click **Connect**. Close Arduino Serial Monitor if it is holding that port.

> **Image placeholder — connection dialog:** actual dmc-lite device, ArcMoco assignment and serial-port selector, with personal device details cropped where appropriate.

If connection fails, verify both core uploads, USB data cable and port selection. Avoid changing baud-rate guesses or opening a serial terminal during a Dragonframe connection.

## Set up one channel

In the Arc motion-control workspace, assign an axis to the connected controller and the desired physical channel. RJ45_1 is channel 1, through RJ45_8 for channel 8; DB37 mirrors those same channels. UI numbering should be confirmed with a short test move, one axis at a time.

Set scale from the motor's steps per revolution, the external driver's microstepping and the transmission ratio. For example, a 200-step motor at 16 microsteps gives **3,200 command pulses per motor revolution**. With a 2:1 reduction, one output revolution needs **6,400 pulses**. Use the units requested by the axis setup; for a linear axis also include travel per output revolution.

Start with low speed and acceleration, measure a short commanded move and correct scale/direction before extending travel. Reverse an axis through its direction setting; **do not swap STEP and DIR wires**. Test stop behavior before normal movement. The [Motion Control chapter](../references.md) explains axis setup, curves and calibration.

## Add other functions

- [Triggers](triggers.md): assign relay, logic-output and switch-input behavior in Scene → Triggers.
- [E-stop](estop.md): enable and test the firmware input separately.
- [Camera wiring](../hardware/wiring.md#j6-camera-remote-release): verify the remote-release cable and camera settings. Availability of the manual's Meter/Shutter test buttons on this dmc-lite setup has not yet been confirmed.

Eight STEP/DIR axes are available. The dmc-lite implementation does not provide crane virtualization or a DMX output connector. Programming an event in Dragonframe's DMX workspace does not add physical DMX output to this shield.
