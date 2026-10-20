# Manuals and verification notes

## Official references

| Source | Use |
|---|---|
| [Dragonframe support / user manual](https://www.dragonframe.com/support/) | Download the manual or open Help in the installed program |
| [Dragonframe downloads](https://www.dragonframe.com/downloads/) | Software and its supplied dmc-lite README/sketches |
| [DMC-32 guide v1.3](https://www.dragonframe.com/download/DMC32-1.3.pdf) | Related connector conventions; not the electrical specification for this shield |
| [TI AM26C31 ordering information](https://www.ti.com/product/AM26C31/part-details/AM26C31IN) | Confirms AM26C31IN / AM26C31INE4 equivalence and PDIP package |
| [TI AM26C31 datasheet](https://www.ti.com/lit/ds/symlink/am26c31.pdf) | Driver function, package, pin numbering and electrical limits |
| [Arduino GIGA R1 WiFi](https://docs.arduino.cc/hardware/giga-r1-wifi/) | Host board setup and power guidance |
| [Dragonframe camera support](https://www.dragonframe.com/camera-support/) | Camera-specific capture setup |

Read the manual matching your installation. The website's download can point to a different edition than the installed application.

## Basis of this edition

Updated October 20, 2026. Connector assignments, IC/channel mapping and LED circuit meanings were checked against the archived October 16 V2 DIP schematic/board and component list. This public manual intentionally excludes manufacturing archives, private order records and firmware source.

The installed **Using Dragonframe 2026** manual was consulted at printed pages **234–235** (trigger channels), **263–268** (input, relay, logic and camera triggers) and **275–276** (dmc-lite capabilities). Installation and Scene → Connections steps follow the installed `Resources/Arc Motion Control/dmc/README.rtf`. These sources describe intended software behavior, not proof that every UI option is exposed by a connected V2 prototype.

## Still awaiting physical confirmation

- First-board operating checks and the actual installed firmware/configuration.
- J6 tip/ring/sleeve mapping and a camera-specific verified cable.
- Connected Dragonframe labels and mapping for LOG1/relay, LOG2 and camera test controls.
- Complete-board electrical load limits, relay switching limits and timing.
- Photographs with connector orientation, LED callouts and driver pin-1 marks.

Until those checks are recorded, follow the explicit limits on each page. In particular, no LED is proof of motion, capture or safety-system performance.
