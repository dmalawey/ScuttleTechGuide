# BeagleY-AI

## Getting Started

**You'll need:**

* [BeagleY-AI board](https://www.beagleboard.org/boards/beagley-ai)
* microSD card (32GB+)
* USB-C power supply
    * Minimum: Rated for 15W (5V 3A)
    * Recommended: [Official Raspberry Pi power supply](https://www.raspberrypi.com/products/27w-power-supply/) or other USB PD-capable power supply
* Ethernet cable
* Active cooler is highly recommended
    * Minimum: Adhesive heat sink and small 5V fan
    * Recommended: [Offcial Raspberry Pi active cooler](https://www.raspberrypi.com/products/active-cooler/)
* Computer with Ethernet port and SD card reader
    * Devices without built-in Ethernet ports or SD card slots may use [USB dongles](https://www.amazon.com/Anker-Ethernet-PowerExpand-Aluminum-Portable/dp/B08CK9X9Z8)

### 1. Cooling

#### Generic heat sink and fan
If you have a generic fan that is rated for 5V or more, connect the power wire to pins 2 or 4 on the BeagleY and the ground wire to pin 6. Refer to the [pinout diagram](https://pinout.beagleboard.io/).

Stick the heat sink onto the main processor, the large silver chip closest to the USB ports. 
Ensure the fan is oriented such that air is being blown through the fins of the heat sink.

The fan can be mounted in various ways, including [this joint](https://grabcad.com/library/fan_joint-1) for mounting on a DIN rail.

![Fan joint v1 mounted on a DIN rail for a BeagleY-AI](img/mg_beagley_fanJoint.jpg)

#### Raspberry Pi Active Cooler
You could also connect the fan using the 4-pin JST cable to the board's PWM fan connector located right below the GPIO pins. Connector's pinout is identical to the Rasperry Pi 5 one.

Top-side view (USB and Ethernet connectors on the bottom) \
Pins from left to right: \
1 - 5V; 2 - PWM; 3 - GND; 4 - TACH.

This option would provide the dynamic fan cooling which is better because the board can manipulate the fan for better cooling (e.g. turn the fan slower or faster). 
More info about active cooling on [Beagle Docs](https://docs.beagle.cc/boards/beagley/ai/02-quick-start.html#attach-cooling-fan). 
### 2. Installing an OS
The BeagleY-AI is designed to run Debian Linux, an open-source operating system common among embedded systems and servers.

1. **Locate the OS images:** Go to [beagleboard.org/boards/beagley-ai](https://www.beagleboard.org/boards/beagley-ai) and click the orange "Software Images" button.
    * There are three pieces of information to note for each image: the Debian version, the environment, and the Linux kernel version. For example, "BeagleY-AI Debian 12.11 2025-05-21 XFCE (v6.6.x-ti)" is Debian 12.11, with the XFCE desktop environment, and Linux kernel 6.6.

1. **Download an image:** The environment determines how you will interact with the board. Once you've selected a configuration that is suitable for your setup, click on the name to download it.
    * [XFCE](https://xfce.org/about/screenshots) is a desktop environment, meaning you will have an interface similar to Windows or MacOS. Note that you'll need a micro HDMI cable and an external monitor to make use of it.
    * The minimal environment contains only a text-based command line. If you intend on running the board headless (meaning, without a dedicated display), this is the recommended configuration.

1. **Flash the image**
    1. Download and install [Balena Etcher](https://etcher.balena.io/).
    1. Insert the micro SD card into your computer, either via a built-in slot or an adapter.
    1. Click "Flash from file" and pick the image from Step 2.
    1. Click "Select target" and pick the SD card. Make sure you select the correct device-- any content on it will be deleted.
    1. Click "Flash!" and wait for it to copy and verify the install.

### 3. Software setup

1. **Connect to the board:** Ultimately you'll want the BeagleY-AI to be connected to the internet via Wi-Fi, but on first startup it doesn't know how to connect to your Wi-Fi network.
    1. Plug one end of an Ethernet cable into your computer and the other end into the Beagle.
    1. WIP


### Num. Connecting Beagle to encoders
![I2C Connection](image/byai_i2c_upd.png)

**1. Locate and mount**

On the 40-pin expansion header:

| Header Pin | Signal |
|:----------:|:------:|
| Pin 1       | 3.3 V   |
| Pin 3       | SDA     |
| Pin 5       | SCL     |
| Pin 9       | GND     |

**2. Verify the Scuttle Pin-Outs**
 ```
From both sides (top → bottom):
  GND
  3.3 V
  SDA
  SCL
  3.3 V
  GND