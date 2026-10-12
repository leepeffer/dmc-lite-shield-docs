# Troubleshooting

This page covers common issues you might encounter with the DMC Lite Shield and their solutions.

## Installation Issues

### Arduino Giga Not Recognized

**Symptoms**: Computer doesn't detect Arduino Giga when connected via USB

**Solutions**:

1. Try a different USB-C cable (must be data-capable, not charge-only)
2. Try a different USB port on your computer
3. Install or update Arduino USB drivers:
   - **Windows**: Install Arduino IDE, which includes drivers
   - **macOS**: Drivers usually installed automatically
   - **Linux**: May require adding user to `dialout` group
4. Check Device Manager (Windows) or System Information (macOS) for device detection
5. Try the Arduino Giga without the shield attached to isolate the issue

### Firmware Upload Fails

**Symptoms**: Arduino IDE shows errors during firmware upload

**Solutions**:

1. Verify the correct board is selected: Tools > Board > Arduino Mbed OS Giga Boards > Arduino Giga R1
2. Ensure the correct port is selected: Tools > Port > [Your Arduino]
3. Press the reset button on the Arduino Giga just before uploading
4. Install the latest Arduino Mbed OS Giga Boards package via Boards Manager
5. Close other programs that might be using the serial port
6. Try uploading with the shield removed to rule out shield-related issues

### Compilation Errors

**Symptoms**: Arduino IDE shows errors when compiling the DMC Lite sketch

**Solutions**:

1. Ensure you're using a compatible version of Arduino IDE
2. Verify all required libraries are installed
3. Check that the Arduino Giga board support package is up to date
4. Verify you haven't introduced syntax errors if you modified `config.h`

## Connection & Communication Issues

### Dragonframe Can't Find DMC Lite

**Symptoms**: Dragonframe doesn't show the DMC Lite Shield or can't connect to it

**Solutions**:

1. Verify the Arduino Giga is connected via USB and powered on
2. Check that the DMC Lite firmware is installed (not another sketch)
3. Confirm the correct serial port is selected in Dragonframe
4. Restart Dragonframe
5. Disconnect and reconnect the USB cable
6. Check if another program is using the serial port (Arduino IDE Serial Monitor, etc.)
7. Review [Dragonframe Configuration](setup/dragonframe.md) for setup steps

### Communication Errors or Timeouts

**Symptoms**: Dragonframe connects but shows errors during operation

**Solutions**:

1. Check for loose USB connection
2. Try a different USB port or cable
3. Verify the baud rate matches between firmware and Dragonframe settings <!-- TODO: Add specific baud rate -->
4. Check for USB power issues (try a powered USB hub if using a long cable)
5. Look for USB driver updates for your operating system

## Motor Control Issues

### Motors Not Responding

**Symptoms**: Motors don't move when commanded from Dragonframe

**Solutions**:

1. **Check Physical Connections**:
   - Verify RJ45 or DB37 cables are fully seated
   - Check connections between drivers and motors
   - Ensure motor wiring matches your driver's requirements

2. **Verify Driver Configuration**:
   - Confirm drivers are configured for 5V step/direction signals
   - Check driver power supply
   - Verify driver enable/disable state (some drivers have enable pins)
   - Check driver DIP switches or settings

3. **Check Dragonframe Settings**:
   - Verify motors are assigned to the correct channels
   - Check motor parameters (steps per revolution, etc.)
   - Test with slower speeds/accelerations initially

4. **Test with Multimeter** (Advanced):
   - Check for step/direction signals at the shield's output
   - Verify 5V signal levels

### Motors Move in Wrong Direction

**Solutions**:

1. Invert the direction setting for that axis in Dragonframe
2. Alternatively, reverse the motor winding connections at the driver
3. Alternatively, swap the step/direction signal wiring (if using custom cables)

### Erratic or Noisy Motor Movement

**Solutions**:

1. Check for loose connections in the step/direction signal path
2. Verify proper grounding of the system
3. Use shielded cables if experiencing electrical noise
4. Reduce motor acceleration/speed settings
5. Check for mechanical binding in your rig
6. Verify driver microstepping configuration

### Motors Stutter or Miss Steps

**Solutions**:

1. Reduce acceleration or maximum speed in Dragonframe
2. Check motor driver current limiting settings (may be too low)
3. Verify your motor is appropriately sized for the load
4. Check for mechanical binding or excessive friction
5. Ensure power supply can handle the current draw of all motors
6. Check driver cooling (overheating can cause issues)

## Camera Control Issues

### Camera Not Responding to DMC Lite

!!! warning "TODO: Camera Troubleshooting Needed"
    Specific camera control troubleshooting steps are not detailed on the dmclite.com website.

**General Solutions**:

1. Verify the 2.5mm cable is fully inserted
2. Check camera compatibility with DMC Lite <!-- TODO: Add compatible camera list -->
3. Verify camera control is enabled and configured in Dragonframe
4. Test cable continuity with a multimeter
5. Check camera settings (some cameras require specific settings for external control)

<!-- TODO: Add camera-specific troubleshooting steps -->

## E-Stop Issues

See the [E-Stop Setup](setup/estop.md#troubleshooting-e-stop-issues) page for e-stop-specific troubleshooting.

## Hardware Issues

### Shield Not Mounting Properly

**Symptoms**: DMC Lite Shield doesn't fit correctly on Arduino Giga

**Solutions**:

1. Verify you have an authentic Arduino Giga R1 WiFi (not a clone or different model)
2. Check for bent pins on either the shield or Arduino
3. Ensure nothing is obstructing the connection
4. Apply even pressure when seating the shield

### Suspected Electrical Damage

**Symptoms**: Shield was working but now shows no signs of life

**If you suspect electrical damage**:

1. Remove the shield from the Arduino Giga
2. Test the Arduino Giga alone with a simple sketch to verify it still works
3. Inspect the shield for visible damage (burned components, damaged traces)
4. Check for short circuits with a multimeter (power off first!)
5. Contact support for repair or replacement options (see [Support](support.md))

!!! danger "Power Safety"
    If you suspect electrical damage, disconnect power immediately and do not reconnect until the issue is identified and resolved.

## Performance Issues

### Moves Not Smooth

1. Adjust acceleration and speed settings in Dragonframe
2. Verify motor driver microstepping settings (higher microstepping = smoother motion)
3. Check for mechanical binding or friction in the rig
4. Ensure adequate power supply for all motors
5. Verify driver current settings are appropriate for your motors

### Real-Time Performance Issues

The DMC Lite firmware is designed for real-time motor control, but performance can be affected by:

1. Computer system performance
2. USB connection quality
3. Dragonframe settings
4. Number of active axes

Try reducing the number of simultaneous axes or adjusting timing parameters.

## Still Need Help?

If you've tried the solutions above and still have issues:

1. Document your problem:
   - What were you doing when the issue occurred?
   - What have you tried already?
   - What is your hardware setup?
   - Any error messages?

2. Check the [FAQ](faq.md) page

3. Contact support (see [Support](support.md) page)

---

**See also:**

- [FAQ](faq.md) - Frequently asked questions
- [Support](support.md) - How to get help
