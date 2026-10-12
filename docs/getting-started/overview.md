# Overview

The DMC Lite Shield is a motion control I/O shield that mounts on the Arduino Giga R1 to provide professional motion control capabilities for Dragonframe stop-motion animation software.

## Purpose

The DMC Lite Shield serves the same purpose as the DMC-32 but with a more streamlined feature set. It's designed for motion control setups that require up to 8 channels of control.

### Key Differences from DMC-32

!!! note "DMC Lite vs DMC-32"
    The DMC Lite is both similar to and different from the DMC-32:
    
    - **Similarities**: Serves the same core motion control purpose, uses RJ45 cables wired exactly like the DMC-32
    - **Differences**: Supports only 8 channels (vs more on DMC-32), cannot run in Virtuals mode like the DMC-32

## How It Works

The DMC Lite Shield runs a dedicated firmware sketch (not the DF Moco sketch) that has been significantly improved and can run motors in real-time. The shield outputs high-quality, buffered 5V step and direction signals that connect to stepper motor drivers to operate motors.

!!! warning "Motor Drivers Required"
    The DMC Lite Shield does **not** drive motors directly. It outputs step and direction signals that must connect to a separate stepper motor driver to operate a motor.

## Does the Shield Include an Arduino Giga?

**No**, the DMC Lite Shield does not include an Arduino Giga. You must:

1. Purchase an Arduino Giga R1 separately
2. Install the DMC Lite firmware sketch yourself

!!! tip
    If you're interested in receiving a pre-flashed Arduino Giga bundle, contact the manufacturer to discuss available options.

## Next Steps

Continue to [Prerequisites](prerequisites.md) to see what you'll need for a complete setup.
