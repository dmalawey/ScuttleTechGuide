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

2. **Download an image:** The environment determines how you will interact with the board. Once you've selected a configuration that is suitable for your setup, click on the name to download it.
    * [XFCE](https://xfce.org/about/screenshots) is a desktop environment, meaning you will have an interface similar to Windows or MacOS. Note that you'll need a micro HDMI cable and an external monitor to make use of it.
    * The minimal environment contains only a text-based command line. If you intend on running the board headless (meaning, without a dedicated display), this is the recommended configuration.

1. **Flash the image**
    1. Download and install [Balena Etcher](https://etcher.balena.io/).
    1. Insert the micro SD card into your computer, either via a built-in slot or an adapter.
    1. Click "Flash from file" and pick the image from Step 2.
    1. Click "Select target" and pick the SD card. Make sure you select the correct device-- any content on it will be deleted.
    1. Click "Flash!" and wait for it to copy and verify the install.

### 3. Network setup

Ultimately you'll want the BeagleY-AI to be connected to the internet via Wi-Fi, but on first startup it doesn't know how to connect to your Wi-Fi network.

1. Plug one end of an Ethernet cable into your computer and the other end into the Beagle.
2. Boot your BeagleY-AI and run 'sudo systemctl start NetworkManager' allowing the board connect to networks.
3. There are two ways now to connect to Wi-Fi networks. \
    - Connecting through NetworkManager TUI (more friendly to first-time users) \
    -> Run **sudo nmtui** and navigating with arrow keys through opened menu click **Activate a connection** \
    ![nmtui-1](img/nmtui-1.png) \
    -> scroll down and select desired network connect to \
    ![nmtui-2](img/nmtui-2.png) \
    -> on the right side click **Activate** \
    -> In case network is protected, in the popped up window type password \
    ![nmtui-3](img/nmtui-3.png)

    - Using nmcli (for advanced users) \
    -> Type **sudo systemctl enable NetworkManager** tu turn on NetworkManager every time you boot the board automatically \
    -> Type **sudo nmcli dev status** to confirm if the dedicated network can be seen by the board \
    -> Type **sudo nmcli device wifi connect 'Your_SSID' password 'Password'** to connect \
    -> Type **sudo nmcli connection modify 'Your_SSID' connection.autoconnect yes** to connect automatically to the same network each boot \
    -> To check if there is internet access type **ping www.google.com**. The resulting output must be this: \
    $ ping www.google.com \
    PING www.google.com (142.250.190.14) 56(84) bytes of data. \
    64 bytes from lhr25s10-in-f14.1e100.net (142.250.190.14): icmp_seq=1 ttl=116 time=10.5 ms

## Environment setup

### 1. Connecting to encoders

1. Connecting the motors



2. Connecting Beagle to encoders
![I2C Connection](image/byai-i2c.png)

**Locate and mount**

On the 40-pin expansion header:

| Header Pin | Signal |
|:----------:|:------:|
| Pin 1       | 3.3 V   |
| Pin 3       | SDA     |
| Pin 5       | SCL     |
| Pin 9       | GND     |

**Verify the Scuttle Pin-Outs**
 ```
From both sides (top → bottom):
***Right encoder***
i2c board       encoder
  GND ---->     GND
  3.3 V ---->   3.3 V
  SDA ---->     SDA/SCn
  SCL ---->     SCL/SCK
  3.3 V ---->   A1/MOSI
  GND ---->     A2/MISO
```

### 3. Connecting to Motor Driver
![Motor Driver](image/Beagle_wiring_whitebg.png)
To allow Beagle communicate with motors the board must be connected to HW-231 Motor Driver using a 5 pin header. Check with the wiring diagram:

**---Right Motor---**
| Channel | Wire | Pin | GPIO |
|:-----:|:------:|:---:|:----:|
| A | Orange | 33 | 13 |
| B | Yellow | 32 | 12 |

**---Left Motor---**
| Channel | Wire | Pin | GPIO |
|:-----:|:------:|:---:|:----:|
| A | Brown | 29 | 5 |
| B | Red | 31 | 6 |

The 5th wire, the black one, is ground. Must be connected to pin 34. 

## Software setup

### 1. Pre-Installation
***Recommended***: After successfully connecting to internet type **sudo apt update**. 
- Your system just grabs the newest lists of available software from all its repositories and stores them in /var/lib/apt/lists/. 
- It simply makes sure that whenever you do an install or upgrade next, you’re working with the freshest info.

***Proceed with caution!***: You could also type **sudo apt upgrade** but be careful as:
- On some boards (e.g. BeagleBone Black with the Debian image), running apt upgrade can actually pull in an older kernel or overwrite vendor‐customized device trees, breaking hardware support. For example, users have reported their 5.10 kernel being downgraded back to 4.19 after an unguarded **apt upgrade**. [-->Source](https://forum.beagleboard.org/t/apt-update-apt-upgrade-automatic-kernel-change-downgrade-to-4-19/32030?utm_source=chatgpt.com)
- Upgrading between major OS releases (e.g. Raspberry Pi OS Bullseye → Bookworm) via **apt full-upgrade** is **NOT** recommended; a clean flash of the new release image is the supported path to avoid partial‐upgrade failures. [-->Upgrade rather than reinstall -](https://forums.raspberrypi.com/viewtopic.php?t=337992&utm_source=chatgpt.com) [ Upgrade from 'Buster' to Raspberry Pi OS<--](https://forums.raspberrypi.com/viewtopic.php?t=288172&utm_source=chatgpt.com)

### 2. Installing Required libraries
Since it's impossible to install required libraries through pip in core environment on BeagleY-AI, users are required to create an external one. \
- To do so type: **python3 -m venv ~/<>>** \
- To activate the newly created environment: **source ~/i2c-env/bin/activate** \
- In case user wants to go back to the core environment: **deactivate**

Once user activated the environment, these libraries must be installed: \
**pip install numpy** \
**pip install python-periphery**

### 3. Installing program files
1. To start operating SCUTTLE with BeagleY-AI download these files: \
[L1_encoder.py](https://www.mediafire.com/file/okivhm6k8538pmm/L1_encoder.py/file) \
[L1_motor.py](https://www.mediafire.com/file/pbtqgwtd8ptlqk8/L1_motor.py/file) \
[L1_gamepad.py] (WIP) \
[L1_log.py] (WIP) \
[L2_speed_control.py] (WIP) \
[L2_kinematics.py] (WIP) \
[L2_inverse_kinematics.py] (WIP) \
[L3_gpDemo.py] (WIP) \