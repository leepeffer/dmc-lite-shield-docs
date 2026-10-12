# Prerequisites

To build a complete motion control setup with the DMC Lite Shield and Dragonframe, you'll need several components beyond the shield itself.

## Required Components

### 1. DMC Lite Shield
The motion control I/O shield (this product).

### 2. Arduino Giga R1 WiFi
The DMC Lite Shield is designed to mount on the Arduino Giga R1 WiFi microcontroller board.

- **Purchase separately**: The Arduino Giga is not included with the shield
- **Where to buy**: Available from Arduino official retailers and distributors
- **Pre-flashed option**: Contact the manufacturer if interested in a pre-flashed bundle

### 3. Stepper Motor Drivers
The DMC Lite Shield outputs step and direction signals but does not drive motors directly. You need stepper motor drivers (one per motor/axis).

!!! info "Driver Compatibility"
    The shield provides:
    
    - Buffered and reinforced 5V step and direction signals
    - Support for up to 8 drivers/channels
    - RJ45 output (wired like DMC-32)
    - DB37 output for legacy Kuper-compatible hardware

<!-- TODO: Add specific driver recommendations, wiring requirements, and compatibility information -->

### 4. Stepper Motors
The actual motors that will move your camera rig, arms, or other equipment (one per axis of motion).

<!-- TODO: Add motor specifications, recommendations, and compatibility information -->

### 5. Connection Cables

Depending on your drivers, you'll need:

- **RJ45 cables** for modern drivers (wired exactly like DMC-32)
- **DB37 cable** for legacy Kuper-compatible hardware

<!-- TODO: Add cable specifications, pinouts, and wiring diagrams -->

### 6. Dragonframe Software
The stop-motion animation software that will control your rig via the DMC Lite Shield.

- **Version requirements**: <!-- TODO: Add minimum Dragonframe version required -->
- **Compatible editions**: <!-- TODO: Specify which Dragonframe editions support DMC Lite -->

### 7. Optional: Camera
For camera control features (meter and shutter via 2.5mm audio jack).

<!-- TODO: Add compatible camera list and connection information -->

## What's Next?

Once you have all the required components, proceed to:

1. [Installing Firmware](../setup/firmware.md) - Flash the DMC Lite sketch to your Arduino Giga
2. [Wiring & Connections](../hardware/wiring.md) - Connect your drivers and motors
3. [Dragonframe Configuration](../setup/dragonframe.md) - Configure Dragonframe to use your DMC Lite Shield

---

**Need help?** See the [Support](../support.md) page for assistance options.
