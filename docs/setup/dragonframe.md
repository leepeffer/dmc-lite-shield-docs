# Dragonframe Configuration

Once you've installed the DMC Lite firmware on your Arduino Giga and connected your motor drivers, you need to configure Dragonframe to communicate with the DMC Lite Shield.

## Prerequisites

Before configuring Dragonframe:

- ✓ DMC Lite firmware is installed on Arduino Giga ([Installation Guide](firmware.md))
- ✓ DMC Lite Shield is properly mounted on Arduino Giga
- ✓ Motor drivers are connected to the shield ([Wiring Guide](../hardware/wiring.md))
- ✓ Arduino Giga is connected to your computer via USB
- ✓ Dragonframe is installed and launched

## Supported Dragonframe Versions

!!! warning "TODO: Version Requirements Needed"
    The minimum Dragonframe version required for DMC Lite Shield support and any version-specific notes are not specified on the dmclite.com website.

<!-- TODO: Add:
- Minimum Dragonframe version required
- Recommended Dragonframe version
- Version-specific compatibility notes
- Which Dragonframe editions support DMC Lite (Core vs Pro)
-->

## Configuration Steps

!!! warning "TODO: Detailed Steps Needed"
    The step-by-step Dragonframe configuration process is not detailed on the dmclite.com website. The README.rtf file in the Dragonframe installation likely contains these instructions.

### Expected Configuration Process

The configuration likely involves:

1. **Open Dragonframe Motion Control Settings**
   - Launch Dragonframe
   - Navigate to Motion Control or Arc settings
   <!-- TODO: Add exact menu path -->

2. **Select DMC Lite Controller**
   - Choose DMC Lite from the list of available controllers
   <!-- TODO: Add exact option name -->

3. **Select Serial Port**
   - Choose the COM port (Windows) or device path (macOS/Linux) for your Arduino Giga
   - The port should be the same one you used when uploading firmware

4. **Configure Channels**
   - Assign your motion control axes to the DMC Lite Shield's 8 channels
   - Configure motor parameters for each axis
   <!-- TODO: Add specific parameter details -->

5. **Test Connection**
   - Use Dragonframe's test or jog features to verify communication
   - Each motor should respond to commands

## Channel Configuration

The DMC Lite Shield supports **up to 8 channels** for motor control.

!!! info "Channel Limitations"
    Unlike the DMC-32, the DMC Lite Shield:
    
    - Supports only 8 channels (not more)
    - Cannot run in Virtuals mode

<!-- TODO: Add:
- How channels map to RJ45 connectors
- How channels map to DB37 pins
- Channel numbering convention
- How to assign axes to channels in Dragonframe
-->

## Motor Parameters

!!! warning "TODO: Motor Configuration Needed"
    Information about configuring motor parameters in Dragonframe for the DMC Lite Shield is not available on the dmclite.com website.

<!-- TODO: Add:
- Steps per revolution/unit settings
- Acceleration and velocity settings
- Direction inversion
- Microstepping configuration
- Backlash compensation
-->

## Camera Control Setup

The DMC Lite Shield includes camera meter and shutter control via 2.5mm audio jack.

<!-- TODO: Add:
- How to enable camera control in Dragonframe
- Camera control settings and parameters
- Compatible camera models
- Cable wiring for camera connection
-->

## Real-Time Motor Control

The DMC Lite firmware is significantly improved over previous versions and can run motors in real-time. This provides:

- Smoother motion during live moves
- Better synchronization between axes
- Improved performance for complex moves

!!! info "Not DF Moco"
    The DMC Lite Shield does **not** run the standard DF Moco sketch. It uses a new, dedicated firmware designed specifically for real-time motor control.

<!-- TODO: Add details about real-time capabilities and any specific settings -->

## Troubleshooting Connection Issues

### Dragonframe Can't Find the Controller

1. Verify the Arduino Giga is connected via USB and powered on
2. Check that the DMC Lite firmware is properly installed (see [Firmware Installation](firmware.md))
3. Try disconnecting and reconnecting the USB cable
4. Restart Dragonframe
5. Check Device Manager (Windows) or System Information (macOS) to confirm the Arduino is recognized

### Motors Not Responding

1. Verify motor drivers are properly connected ([Wiring Guide](../hardware/wiring.md))
2. Check that drivers are powered
3. Verify driver configuration for 5V step/direction signals
4. Test motor parameters and channel assignments in Dragonframe
5. Check for loose connections on RJ45 or DB37 cables

### Communication Errors

1. Ensure no other software is using the Arduino's serial port
2. Try a different USB port on your computer
3. Check for USB driver updates
4. Verify the baud rate setting matches between firmware and Dragonframe <!-- TODO: Add specific baud rate -->

---

**Next Steps:**

- [E-Stop Setup](estop.md) - Configure emergency stop functionality
- [Troubleshooting](../troubleshooting.md) - Additional troubleshooting help
- [FAQ](../faq.md) - Frequently asked questions
