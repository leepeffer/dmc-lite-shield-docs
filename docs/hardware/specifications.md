# Hardware Specifications

The DMC Lite Shield is a motion control I/O shield designed to mount on the Arduino Giga R1 WiFi microcontroller board.

## Key Features

### Motion Control Outputs

**Number of Channels**: Up to 8 stepper motor drivers

**Signal Type**: Buffered and reinforced step and direction signals

**Output Voltage**: 5V logic level

**Output Connectors**:

- RJ45 connectors (wired exactly like DMC-32)
- DB37 connector for legacy Kuper-compatible hardware

### Camera Control

**Interface**: 2.5mm audio jack

**Functionality**:

- Camera meter control
- Shutter control

<!-- TODO: Add specific camera control signal specifications, voltage levels, and timing -->

### Emergency Stop (E-Stop)

**Type**: Optically isolated e-stop output

**Configuration**: Requires enabling in firmware (see [E-Stop Setup](../setup/estop.md))

<!-- TODO: Add e-stop electrical specifications, isolation details, and connection requirements -->

## Physical Specifications

**Form Factor**: Arduino Giga R1 shield

**Mounting**: Designed to mount directly onto Arduino Giga R1 WiFi with perfect fit

<!-- TODO: Add physical dimensions, weight, mounting hole positions, and connector locations -->

## Electrical Specifications

<!-- TODO: Add the following specifications:
- Input voltage requirements
- Power consumption
- Maximum current per output channel
- Signal frequency ranges
- Input/output protection details
-->

## Pinout

!!! warning "TODO: Pinout Information Needed"
    Detailed pinout information for the RJ45, DB37, and 2.5mm jack connectors is not available on the dmclite.com website and needs to be added.

<!-- TODO: Add connector pinouts:
- RJ45 connector pinout (with reference to DMC-32 compatibility)
- DB37 connector pinout (Kuper compatibility)
- 2.5mm audio jack pinout for camera control
- Arduino Giga pin usage
-->

## Compatibility

### Arduino Compatibility

- **Compatible**: Arduino Giga R1 WiFi
- **Not compatible**: Other Arduino models (designed specifically for Giga)

### Software Compatibility

- **Dragonframe**: Requires DMC Lite firmware sketch (not DF Moco sketch)
- **Virtuals Mode**: Not supported (unlike DMC-32)

### Hardware Compatibility

- **Stepper Drivers**: Any driver accepting 5V step/direction signals
- **Legacy Systems**: Kuper-compatible via DB37 output
- **DMC-32 Cables**: RJ45 cables wired for DMC-32 are directly compatible

## Environmental Specifications

<!-- TODO: Add operating temperature range, humidity limits, and storage conditions -->

---

**Next:** [Wiring & Connections](wiring.md) to learn how to connect your drivers and peripherals.
