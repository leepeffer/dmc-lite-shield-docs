# Frequently Asked Questions

Common questions about the DMC Lite Shield.

## General Questions

### Does the DMC Lite Shield come with an Arduino Giga?

**No**, the DMC Lite Shield does not include an Arduino Giga. You need to:

- Purchase an Arduino Giga R1 WiFi separately
- Install the DMC Lite firmware sketch yourself

However, if you're interested in receiving a pre-flashed Arduino Giga bundle, contact the manufacturer to discuss available options.

### Is this a replacement for the DMC-32?

Both yes and no. The DMC Lite serves the same purpose as the DMC-32 but has fewer features:

**Similarities**:

- Provides motion control for Dragonframe
- Uses RJ45 cables wired exactly like the DMC-32
- Controls stepper motor drivers

**Key Differences**:

- **Channel Limit**: DMC Lite supports only 8 channels (vs more on DMC-32)
- **Virtuals Mode**: DMC Lite cannot run in Virtuals mode like the DMC-32

The DMC Lite is ideal for motion control setups requiring up to 8 axes. For larger setups or those requiring Virtuals mode, the DMC-32 remains the better choice.

## Compatibility

### Does this run the DF Moco Sketch?

**No**, the DMC Lite Shield does not run the standard DF Moco sketch. It runs a new, dedicated DMC Lite sketch which has been significantly improved and can run motors in real-time.

This new firmware provides better performance for real-time motor control operations.

### Can the DMC Lite Shield run motors directly?

**No**, the DMC Lite Shield outputs high-quality, buffered 5V step and direction signals. These signals must connect to a stepper motor driver to operate a motor.

You will need:

- One stepper motor driver per axis/motor
- Appropriate power supply for your drivers and motors
- Connection cables (RJ45 or DB37)

See [Prerequisites](getting-started/prerequisites.md) for a complete component list.

### What Arduino boards are compatible?

The DMC Lite Shield is designed specifically for the **Arduino Giga R1 WiFi** and is not compatible with other Arduino models. The shield is designed to mount perfectly and communicate seamlessly with the Arduino Giga.

## Setup & Requirements

### What else do I need for a complete motion control setup in Dragonframe?

Besides the DMC Lite Shield and Arduino Giga, you'll need:

1. **Stepper Motor Drivers** - One per axis (motor)
2. **Stepper Motors** - Appropriate for your rig's requirements
3. **Connection Cables** - RJ45 cables (DMC-32 compatible) or DB37 cable for legacy hardware
4. **Dragonframe Software** - For motion control
5. **Power Supplies** - For drivers and motors
6. **Computer** - To run Dragonframe and connect to the Arduino Giga

See the [Prerequisites](getting-started/prerequisites.md) page for detailed information.

### How do I install the Dragonframe sketch on the Arduino Giga?

Follow the instructions in the `README.rtf` file located in the `Dragonframe > Resources > Arc Motion Control > dmc` folder.

For detailed guidance, see our [Firmware Installation](setup/firmware.md) page.

### How do I enable the e-stop functionality?

To enable the e-stop feature:

1. Open the DMC Lite firmware sketch in Arduino IDE
2. Navigate to the `config.h` file for the `dmc_m7` core
3. Uncomment the line: `#define KILL_SWITCH_PIN D48`
4. Save and upload the modified firmware to your Arduino Giga

See the [E-Stop Setup](setup/estop.md) page for complete instructions and wiring details.

## Ordering & Availability

### How many units are kept in stock?

Due to the low production volume of this product, limited stock is maintained. However, units may be available for immediate shipping.

**Recommendation**: Contact the manufacturer to check current availability.

### How fast can these be shipped?

**Regular Orders**: If units are in stock, shipping time depends on your location and selected shipping method.

**Bulk Orders**: For orders of 5 or more units, the manufacturer can manufacture and ship anywhere in the world within **12 days**.

### Where can I buy the DMC Lite Shield?

Visit [www.dmclite.com](https://www.dmclite.com) for ordering information.

## Version Information

### What is the status of V2?

As of October 10, 2026, V2 of the DMC Lite Shield is in development:

**Development Progress**:

1. ✓ Plan - Done
2. ✓ Layout - Done
3. ⏳ Routing - In progress
4. Prototype production - Next
5. Prototype testing - Upcoming
6. Final order - Upcoming

You can show interest in V2 (without commitment) by filling out the form on the [DMC Lite website](https://www.dmclite.com).

!!! info "Current Version"
    This documentation covers the current version of the DMC Lite Shield. Version-specific information will be added as V2 becomes available.

## Support

### I need help with motion control. Are you available?

**Yes!** The manufacturer offers support and consultation for motion control setups.

See the [Support](support.md) page for contact information.

### Where can I find technical specifications?

See the [Hardware Specifications](hardware/specifications.md) page for detailed technical information about the shield.

### I have a question that's not answered here

Please check:

1. Other documentation pages in this manual
2. The [Troubleshooting](troubleshooting.md) page
3. Contact support via the [Support](support.md) page

---

**Can't find what you're looking for?** See the [Support](support.md) page for help.
