# Installing Firmware

The DMC Lite Shield requires a specific firmware sketch to be installed on your Arduino Giga R1 WiFi. This is **not** the standard DF Moco sketch - it's a new, significantly improved firmware that can run motors in real-time.

## Prerequisites

Before installing the firmware, ensure you have:

- ✓ Arduino Giga R1 WiFi
- ✓ Dragonframe software installed on your computer
- ✓ USB-C cable to connect Arduino Giga to your computer

!!! info "Pre-Flashed Option"
    If you're interested in purchasing a pre-flashed Arduino Giga with the DMC Lite firmware already installed, contact the manufacturer to discuss bundle options.

## Locating the Firmware

The DMC Lite firmware sketch is included with Dragonframe:

**Location**: `Dragonframe > Resources > Arc Motion Control > dmc` folder

!!! warning "TODO: Exact Path Needed"
    The exact file path varies by operating system and is not fully specified on the dmclite.com website:
    
    - **Windows**: `C:\Program Files\Dragonframe\...` <!-- TODO: Complete path -->
    - **macOS**: `/Applications/Dragonframe/...` <!-- TODO: Complete path -->
    - **Linux**: <!-- TODO: Add Linux path if supported -->

Look for the `README.rtf` file in the `dmc` folder for complete installation instructions.

## Installation Instructions

According to the DMC Lite website:

> "Follow the instructions in the README.rtf file located in the Dragonframe > Resources > Arc Motion Control > dmc folder."

!!! warning "TODO: Installation Steps Needed"
    The detailed step-by-step installation process from the README.rtf file is not available on the dmclite.com website. The following outline likely covers the main steps, but verify with the actual README.rtf:

### Likely Installation Steps

1. **Open Arduino IDE**
   - Download and install Arduino IDE if not already installed
   - Launch Arduino IDE

2. **Install Arduino Giga Board Support**
   - In Arduino IDE, go to Tools > Board > Boards Manager
   - Search for "Arduino Giga"
   - Install the Arduino Mbed OS Giga Boards package

3. **Open the DMC Lite Sketch**
   - Navigate to the Dragonframe dmc folder
   - Open the DMC Lite sketch file (`.ino` file)

4. **Configure the Sketch (Optional)**
   - See [Configuration Options](#configuration-options) below

5. **Select Board and Port**
   - Tools > Board > Arduino Mbed OS Giga Boards > Arduino Giga R1
   - Tools > Port > Select your connected Arduino Giga

6. **Upload Firmware**
   - Click the Upload button (→) in Arduino IDE
   - Wait for compilation and upload to complete
   - Verify the upload was successful

## Configuration Options

The firmware includes a `config.h` file with various settings.

### E-Stop Configuration

To enable the e-stop functionality, you must edit the firmware:

**Uncomment the following line in `config.h` for the `dmc_m7`:**

```cpp
#define KILL_SWITCH_PIN D48
```

See [E-Stop Setup](estop.md) for more details.

!!! warning "TODO: Configuration Details Needed"
    Additional configuration options in `config.h` are not documented on the dmclite.com website, such as:
    
    - Motor configuration parameters
    - Communication settings
    - Pin assignments
    - Other optional features

## Verifying Installation

After uploading the firmware:

1. Open the Arduino IDE Serial Monitor (Tools > Serial Monitor)
2. Set the baud rate to the appropriate value <!-- TODO: Add baud rate -->
3. You should see startup messages from the DMC Lite firmware
4. The Arduino Giga's built-in LED may indicate status <!-- TODO: Add LED behavior -->

## Updating Firmware

To update to a newer version of the DMC Lite firmware:

1. Install the latest version of Dragonframe (which includes firmware updates)
2. Follow the same installation procedure as above
3. The new firmware will overwrite the previous version

!!! tip "Backup Configuration"
    If you've customized `config.h`, save a copy of your settings before updating, as the update will replace the file.

## Firmware Versions

!!! warning "TODO: Version Information Needed"
    Information about firmware versions, version checking, and changelog is not available on the dmclite.com website.

<!-- TODO: Add:
- How to check current firmware version
- Firmware version history
- Compatibility between firmware versions and Dragonframe versions
-->

## Troubleshooting Firmware Installation

### Upload Fails

- Ensure the Arduino Giga is properly connected via USB-C
- Try a different USB cable or port
- Verify the correct board is selected in Arduino IDE
- Try pressing the reset button on the Arduino Giga before uploading

### Compilation Errors

- Ensure you have the latest Arduino Giga board support package installed
- Verify all required libraries are installed
- Check that you're using a compatible Arduino IDE version

### Arduino Not Recognized

- Install or update USB drivers for Arduino Giga
- Try a different USB cable (must be data-capable, not charge-only)
- Check Device Manager (Windows) or System Information (macOS) to see if the device is detected

---

**Next:** [Dragonframe Configuration](dragonframe.md) to set up Dragonframe to use your DMC Lite Shield.
