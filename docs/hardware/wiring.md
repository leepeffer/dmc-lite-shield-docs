# Wiring & Connections

This guide covers how to connect the DMC Lite Shield to your motor drivers, camera, and other peripherals.

## Overview

The DMC Lite Shield provides multiple connection options:

- **RJ45 connectors** for motor drivers (up to 8 channels)
- **DB37 connector** for legacy Kuper-compatible systems
- **2.5mm audio jack** for camera meter and shutter control
- **E-stop output** (optically isolated)

!!! danger "Power Safety"
    Always power off all equipment before making or changing connections. Follow your motor driver manufacturer's safety guidelines.

## Mounting the Shield on Arduino Giga

1. Ensure your Arduino Giga R1 WiFi is powered off
2. Align the DMC Lite Shield's headers with the Arduino Giga's socket connectors
3. Gently press the shield down until fully seated
4. Verify all pins are properly connected

The shield is designed for a perfect, secure fit with the Arduino Giga R1 WiFi.

## Connecting Motor Drivers

### Using RJ45 Connectors

The DMC Lite Shield provides RJ45 connectors for up to 8 motor drivers.

**Cable Compatibility**: Use RJ45 cables wired **exactly like the DMC-32**. If you have existing DMC-32 cables, they are directly compatible.

!!! warning "TODO: Pinout Needed"
    Detailed RJ45 pinout information is not available on the dmclite.com website. For now, refer to DMC-32 compatible cabling.

<!-- TODO: Add:
- RJ45 pinout diagram
- Channel numbering (which RJ45 jack corresponds to which channel)
- Cable maximum length recommendations
- Shielded vs unshielded cable guidance
-->

**Connection Steps**:

1. Identify the channel number you want to use (1-8)
2. Connect the RJ45 cable from the corresponding DMC Lite Shield jack to your motor driver's input
3. Ensure your driver is configured to accept 5V step/direction signals
4. Connect your motor driver's output to your stepper motor per the driver's manual

### Using DB37 Connector

For legacy hardware designed for Kuper systems, use the DB37 connector as an alternative output method.

!!! warning "TODO: Pinout Needed"
    DB37 connector pinout information for Kuper compatibility is not available on the dmclite.com website.

<!-- TODO: Add:
- DB37 pinout diagram
- Channel mapping on DB37
- Cable requirements and recommendations
- Kuper compatibility notes
-->

## Camera Control Connection

The DMC Lite Shield includes a 2.5mm audio jack for camera meter and shutter control.

**Compatible Features**:

- Camera meter control
- Shutter trigger control

!!! warning "TODO: Wiring Details Needed"
    Specific camera control wiring, signal types, and compatible camera models are not detailed on the dmclite.com website.

<!-- TODO: Add:
- 2.5mm jack pinout (tip/ring/sleeve assignments)
- Compatible camera list
- Cable assembly instructions or recommended cables
- Signal voltage and timing specifications
-->

## E-Stop Connection

The DMC Lite Shield provides an optically isolated e-stop output for emergency motor shutdown.

!!! info "Requires Firmware Configuration"
    The e-stop feature must be enabled in the firmware. See [E-Stop Setup](../setup/estop.md) for configuration instructions.

<!-- TODO: Add:
- E-stop connector type and location
- Wiring diagram
- Connection to external e-stop systems
- Electrical isolation specifications
-->

## Power Considerations

<!-- TODO: Add:
- Power requirements for the shield
- Whether shield is powered by Arduino Giga or needs external power
- Power sequencing recommendations
- Current draw specifications
-->

## Troubleshooting Connections

### Motor Not Responding

1. Verify the RJ45 cable is fully seated on both ends
2. Check that your motor driver is receiving step/direction signals (many drivers have indicator LEDs)
3. Verify your driver is configured for 5V logic level inputs
4. Test the cable with a multimeter to ensure continuity

### Camera Control Not Working

1. Verify the 2.5mm jack is fully inserted
2. Check camera compatibility
3. Verify cable continuity
4. See [Troubleshooting](../troubleshooting.md) for more solutions

---

**Next:** [Installing Firmware](../setup/firmware.md) to flash your Arduino Giga with the DMC Lite sketch.
