# Computing Guide

This section covers the various computer options for your SCUTTLE CPU.  It starts with differences in wiring for various SBCs (single board computers).  

---

| Pi | TI | Intel |
| -- | -- | ----- |
| ![sctl_pi](image/tg_scuttle_pi.png) | ![sctl_ti](image/tg_scuttle_ti.png) | ![sctl_intel](image/tg_scuttle_intel.png) |
| [Pi 4 Datasheet](https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-datasheet.pdf) | [TDA4VM Datasheet](https://www.ti.com/lit/pdf/spruj21) | [SBC Datasheet](https://www.axiomtek.com/Download/Spec/en-US/capa55r.pdf) |
| [Pi 4 Home](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) | [TDA4VM SK Product Page](https://www.ti.com/tool/SK-TDA4VM) | [CAPA55R Product Page](https://www.axiomtek.com/Default.aspx?MenuId=Products&FunctionId=ProductView&ItemId=26529&upcat=270) |

## Pi_4

**Raspberry Pi 4B with Broadcom ARM processor**

[DOWNLOAD](https://lobfile.com/file/DIq7.drawio) editable design

Overview of wiring SCUTTLE with Pi:
![Pi wiring overview](image/wg_overview_pi.png ':class=image-25')

_Figure: Pi wiring overview_

## TI_Edge_AI

**Texas Instruments "Edge AI" class single-board-computer with TDA4VM ARM processor**

[DOWNLOAD](https://lobfile.com/file/DIq7.drawio) editable design

Overview of wiring SCUTTLE with TDA4VM:
![EDGE AI wiring overview](image/wg_overview_TDA4VM.png ':class=image-25')
_Figure: Edge AI wiring overview_

<div class="accordion">

<details>
  <summary>Edge AI Pinout</summary>

 _Edge AI Pinout_
| Function  | PIN |    |  Function |
| --------- | --- | -- | ----- |
| Power_3.3 | 1   | 2  | Power_5.0 |
| I2C_SDA   | 3   | 4  | Power |
| I2C_SCL   | 5   | 6  | GND |
| GPIO      | 7   | 8  | UART_TXD |
| GND       | 9   | 10 | UART_RXD |
| GPIO      | 11  | 12 | I2S_SCLK |
| GPIO      | 13  | 14 | GND |
| GPIO      | 15  | 16 | GPIO |
| Power_3.3 | 17  | 18 | GPIO |
| SPI_MOSI  | 19  | 20 | GND |
| SPI_MISO  | 21  | 22 | GPIO |
| SPI_SCLK  | 23  | 24 | SPI_CS0 |
| GND       | 25  | 26 | SPI_CS1 |
| ID_SDA    | 27  | 28 | ID_SCL |
| GPIO      | 29  | 30 | GND |
| GPIO      | 31  | 32 | PWM0 |
| PWM1      | 33  | 34 | GND |
| I2S_FS    | 35  | 36 | GPIO |
| GPIO      | 37  | 38 | I2S_DIN |
| GND       | 39  | 40 | I2S_DOUT |

</details>

</div>

## Intel_CAPA55R

**Axiomtek CAPA55R single-board industrial computer with Intel i7 X86 processor**

[DOWNLOAD](https://lobfile.com/file/DIq7.drawio) editable design

Overview of wiring SCUTTLE with Intel-based CAPA55R:
![Intel wiring overview](image/wg_overview_intel.png ':class=image-25')
_Figure: Intel wiring overview_

Axiomtek's CAPA55R Intel-based computer for industrial robotics:
![CAPA55R Image](https://www.axiomtek.com/Download/Photo/en-US/capa55r_4.jpg ':class=image-25')
_Figure: Axiomtek / Intel CAPA55R SBC_

---