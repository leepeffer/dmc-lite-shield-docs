# Equipment you need

- V2 socketed DIP DMC Lite Shield and Arduino GIGA R1 WiFi.
- Computer running Dragonframe, plus a USB-C **data** cable for the GIGA.
- External step/direction motor driver and suitable motor for each axis.
- Separate motor power supply sized for those drivers and motors.
- Verified signal cables; see [wiring](../hardware/wiring.md).
- A stop arrangement appropriate to the rig; see [E-stop](../setup/estop.md).

Choose external drivers by their actual input circuit, voltage/current requirements and timing—not simply the label “5 V compatible.” RJ45 provides complementary STEP/DIR signals; DB37 provides positive, single-ended signals. Neither connector supplies motor power.

Optional equipment includes a normally open pushbutton for SWITCH, a device with a compatible low-voltage trigger input, and a camera-specific remote-release cable.

This guide was checked against Dragonframe 2026 documentation. dmc-lite was introduced with Dragonframe 2024.01; that software history is not a board qualification for every release or edition. Confirm your software exposes dmc-lite before commissioning the rig. [Official manuals](../references.md).
