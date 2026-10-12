# E-Stop (Emergency Stop) Setup

The DMC Lite Shield includes an optically isolated emergency stop (e-stop) output for safely shutting down motor movement in case of emergency.

## Overview

The e-stop feature provides:

- **Optical isolation** for electrical safety
- **Quick shutdown** of all motor operations
- **Integration** with external e-stop systems

!!! warning "Firmware Configuration Required"
    The e-stop functionality is **disabled by default** and must be enabled in the firmware configuration before use.

## Enabling E-Stop in Firmware

To enable the e-stop functionality:

1. Open the DMC Lite firmware sketch in Arduino IDE (see [Firmware Installation](firmware.md) for location)

2. Navigate to the `config.h` file for the `dmc_m7` core

3. Find the following line (it will be commented out):

   ```cpp
   // #define KILL_SWITCH_PIN D48
   ```

4. Uncomment the line by removing the `//`:

   ```cpp
   #define KILL_SWITCH_PIN D48
   ```

5. Save the file

6. Upload the modified firmware to your Arduino Giga (see [Firmware Installation](firmware.md) for upload instructions)

## Hardware Connection

!!! warning "TODO: Connection Details Needed"
    Detailed information about the e-stop connector, wiring, and external connections is not available on the dmclite.com website.

<!-- TODO: Add:
- E-stop connector type and location on the shield
- Pin assignments or terminal labels
- Wiring diagram for external e-stop button/switch
- Electrical specifications (voltage, current)
- Normally open vs normally closed configuration
- How the optical isolation is implemented
-->

### Connecting an External E-Stop Button

<!-- TODO: Add step-by-step connection instructions -->

## How E-Stop Works

When the e-stop is triggered:

1. The DMC Lite Shield immediately stops sending step signals to all motor drivers
2. Motors will hold their current position (assuming drivers are powered and holding torque)
3. Motion must be manually resumed after clearing the e-stop condition

!!! danger "Safety Note"
    The e-stop signal from the DMC Lite Shield controls the motion control signals only. Your motor drivers may continue to power the motors (holding torque). For complete system shutdown, implement additional safety measures at the driver or power supply level.

## Testing the E-Stop

After enabling and connecting the e-stop:

1. **Initial Test (Safe Position)**
   - Position all rig components in a safe location
   - Ensure nothing can be damaged if motion stops abruptly

2. **Activate E-Stop Before Motion**
   - Trigger the e-stop
   - Attempt to move motors via Dragonframe
   - Verify that motors do not move

3. **Activate E-Stop During Motion**
   - Start a slow, safe motion move
   - Trigger the e-stop mid-motion
   - Verify that motion stops immediately
   - Check that motors hold position

4. **Reset E-Stop**
   - Clear the e-stop condition
   - Verify that motion control can resume

!!! tip "Regular Testing"
    Test your e-stop system regularly to ensure it's functioning correctly. Include e-stop testing in your pre-shoot safety checklist.

## E-Stop Best Practices

### Safety Considerations

- **Always have an e-stop accessible** during motion control operations
- **Position e-stop button** where operators can reach it quickly
- **Test before each session** to verify e-stop functionality
- **Train all operators** on e-stop location and usage
- **Consider multiple e-stop stations** for larger rigs

### System Design

- Combine DMC Lite e-stop with driver-level safety features for redundancy
- Consider adding physical hard stops or limit switches to prevent mechanical damage
- Document your e-stop wiring and configuration for maintenance

### Limitations

!!! warning "E-Stop Scope"
    The DMC Lite Shield e-stop controls only the step/direction signals. It does not:
    
    - Cut power to motor drivers
    - Control camera shutters
    - Disable other equipment
    
    Design your complete safety system accordingly.

## Troubleshooting E-Stop Issues

### E-Stop Not Working

1. Verify the firmware has been modified and uploaded with `KILL_SWITCH_PIN D48` uncommented
2. Check e-stop wiring and connections
3. Test e-stop switch/button continuity with a multimeter
4. Verify the e-stop is properly connected to the designated pin <!-- TODO: Add pin location -->

### False E-Stop Triggers

1. Check for loose connections in e-stop wiring
2. Verify proper grounding and shielding if using long cables
3. Check for electrical noise from nearby equipment
4. Verify correct normally-open or normally-closed configuration <!-- TODO: Specify which -->

### Motors Don't Hold Position After E-Stop

- This is a driver configuration issue, not a DMC Lite issue
- Check your driver's hold current settings
- Ensure drivers remain powered when e-stop is triggered

---

**Next:** [Troubleshooting](../troubleshooting.md) for additional help with common issues.
