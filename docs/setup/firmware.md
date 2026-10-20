# Firmware installation

The **Arduino GIGA**, not the shield itself, runs Dragonframe's **dmc-lite** firmware. It needs two matching sketches: `dmc_m7` and `dmc_m4`. The older `DFMoco` sketch is different.

If your GIGA arrived configured, record its firmware version and input options before changing anything. The first prototype's installed firmware has not yet been recorded; this guide does not certify a pre-flashed image.

## Find the official sketches

Use the `README.rtf` supplied with your Dragonframe installation. On the inspected macOS Dragonframe 2026 installation it is here:

```text
/Applications/Dragonframe 2026/Resources/Arc Motion Control/dmc/README.rtf
```

The same `dmc` folder contains `dmc_m7` and `dmc_m4`. On other installations, look under **Resources → Arc Motion Control**; the manual also uses the folder name `dmc-lite`. Locate the paired sketches rather than assuming a platform-specific path. Copy the complete folder to a writable working location before editing.

## Upload both cores

Disconnect motor-driver power and external trigger loads before uploading.

1. Install Arduino IDE and **Arduino Mbed OS Giga Boards** through Boards Manager. The archived V2 sketches compile with core **4.5.0**; compile success alone is not a hardware test.
2. Open `dmc_m7/dmc_m7.ino`. Select **Arduino GIGA R1** and the actual connected USB port.
3. Set **Target core → Main core** and **Flash split → 1.5MB M7 + 0.5MB M4**. Upload and confirm success.
4. Open the matching `dmc_m4/dmc_m4.ino`. Set **Target core → M4 Co-processor**, retaining the same flash split. Upload and confirm success.
5. Close Serial Monitor or other programs holding the port. Reconnect/reset as directed by the supplied README, then [connect Dragonframe](dragonframe.md).

Do not mix cores from different firmware releases. Record the source release, board-core version and configuration you actually uploaded.

## V2 input and output settings

In the **GIGA section** of M7 `config.h`, enable the options you intend to use:

```cpp
#define KILL_SWITCH_PIN D48
#define LOGIC_SWITCH_PIN D49
```

Do not duplicate existing definitions; uncomment/edit them. Review [E-stop polarity](estop.md) before enabling the stop. SWITCH uses a normally open contact to ground. Both features are disabled in the archived prototype configurations.

V2 follows STEP D22/D24…D36, DIR D23/D25…D37, LOG1 D40, LOG2 D41, meter D52 and shutter D53. See the [full mapping](../hardware/wiring.md#giga-signals-for-firmware-configuration). Avoid older pin-swapped V1 configurations.

## Verify the installation

A serial connection is only the first check. Test each axis slowly in both directions, stop contact open/closed/disconnected, SWITCH action, relay closure, LOG2 and camera contacts before using the rig. A lit input LED does not prove the corresponding firmware option is enabled.

For updates, save your current configuration, read the new release's README and repeat both uploads and the operating checks. Obtain software from [Dragonframe](https://www.dragonframe.com/downloads/) and GIGA setup guidance from [Arduino](https://docs.arduino.cc/hardware/giga-r1-wifi/).
