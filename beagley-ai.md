# BeagleY-AI

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

## Hardware setup

### 1. Cooling
The BeagleY-AI tends to run quite hot, so some kind of additional cooling is recommended.

#### Generic heat sink and fan
If you have a generic fan that is rated for 5V or more, connect the power wire to pins 2 or 4 on the BeagleY and the ground wire to pin 6. Refer to the [pinout diagram](https://pinout.beagleboard.io/).

Stick the heat sink onto the main processor, the large silver chip closest to the USB ports. 
Ensure the fan is oriented such that air is being blown through the fins of the heat sink.

The fan can be mounted in various ways, including [this joint](https://grabcad.com/library/fan_joint-1) for mounting on a DIN rail.

![Fan joint v1 mounted on a DIN rail for a BeagleY-AI](img/mg_beagley_fanJoint.jpg)

#### Raspberry Pi Active Cooler
You could also connect the fan using the 4-pin JST cable to the board's PWM fan connector located right below the GPIO pins. Connector's pinout is identical to the Rasperry Pi 5 one.

Top-side view (USB and Ethernet connectors on the bottom) \
Pins from left to right:

![JST](image/BeagleY-AI%20Fan%20connector.png)

This option would provide the dynamic fan cooling which is better because the board can manipulate the fan for better cooling (e.g. turn the fan slower or faster). 
More info about active cooling on [Beagle Docs ↗](https://docs.beagle.cc/boards/beagley/ai/02-quick-start.html#attach-cooling-fan).

### 2. Installing an OS
The BeagleY-AI is designed to run Debian Linux, an open-source operating system common among embedded systems and servers.

1. **Locate the OS images:** Go to [beagleboard.org/boards/beagley-ai ↗](https://www.beagleboard.org/boards/beagley-ai) and click the orange "Software Images" button.
    * There are three pieces of information to note for each image: the Debian version, the environment, and the Linux kernel version. For example, "BeagleY-AI Debian 12.11 2025-05-21 XFCE (v6.6.x-ti)" is Debian 12.11, with the XFCE desktop environment, and Linux kernel 6.6.

1. **Download an image:** The environment determines how you will interact with the board. Once you've selected a configuration that is suitable for your setup, click on the name to download it.
    * [XFCE ↗](https://xfce.org/about/screenshots) is a desktop environment, meaning you will have an interface similar to Windows or MacOS. Note that you'll need a micro HDMI cable and an external monitor to make use of it.
    * The minimal environment contains only a text-based command line. If you intend on running the board headless (meaning, without a dedicated display), this is the recommended configuration.

1. **Flash the image**
    1. Download and install [Balena Etcher ↗](https://etcher.balena.io/).
    1. Insert the micro SD card into your computer, either via a built-in slot or an adapter.
    1. Click "Flash from file" and pick the image from Step 2.
    1. Click "Select target" and pick the SD card. Make sure you select the correct device-- any content on it will be deleted.
    1. Click "Flash!" and wait for it to copy and verify the install.

### 3. Network setup

Ultimately you'll want the BeagleY-AI to be connected to the internet via Wi-Fi, but on first startup it won't know how to connect to your Wi-Fi network.

1. **Establish a wired connection:** Plug one end of an Ethernet cable into your computer and the other end into the Beagle.
1. **Power on the board:** Plug your BeagleY-AI into a suitable USB-C power adapter.
1. **Connect to the board:** In a terminal on your computer, run `ssh debian@beaglebone.local`. If this succeeds, you will now be running commands on the Beagle.
1. **Connect to Wi-Fi:** Run `sudo systemctl start NetworkManager` and connect to your Wi-Fi network via NetworkManager TUI:
    1. Run `sudo nmtui` and select **Activate a connection**. \
    ![nmtui-1](img/nmtui-1.png)
    1. Select desired network connect to. \
    ![nmtui-2](img/nmtui-2.png)
    1. On the right, click **Activate**.
    1. If necessary, type the network password in the pop-up window. \
    ![nmtui-3](img/nmtui-3.png)


> [!NOTE]
> If you are SSH'ed into the Beagle over Ethernet, the connection may drop out after a few minutes. A common workaround is to SSH into the board and run `sudo nmcli c m "Wired connection 1" ipv4.method link-local`.

## Electrical setup

### 1. Motors to Motor Driver
See [Wiring § Motor Driver](wiring.md#actuator-motor-driver) for how to wire the motors to the motor driver.

### 2. Motor Driver to Beagle
The BeagleY-AI controls the motors via the HW-231 Motor Driver.

![Motor Driver](image/Beagle_wiring_whitebg.png)

### 3. Encoders to Beagle
The encoders are used to determine the rotational position of each wheel. They are connected to the Beagle using the I2C protocol. The SCUTTLE design uses a simple I2C bus board to combine the I2C connections for both encoders into a single set of wires.

See [Wiring § Encoder](wiring.md#sensor-encoder)

![I2C Connection](img/wg_byai_encoder.png)

## Software setup

### 1. Pre-requisites
After successfully connecting to internet, run `sudo apt update`. 
- Your system just grabs the newest lists of available software from all its repositories and stores them in `/var/lib/apt/lists/`. 
- It simply makes sure that whenever you do an install or upgrade next, you’re working with the freshest info.

> [!WARNING]
> You could also `sudo apt upgrade` but be careful as on some boards (e.g. BeagleBone Black with the Debian image), running `apt upgrade` can actually pull in an older kernel or overwrite vendor‐customized device trees, breaking hardware support. For example, users have reported their 5.10 kernel being downgraded back to 4.19 after an unguarded `apt upgrade`. [More info ↗](https://forum.beagleboard.org/t/apt-update-apt-upgrade-automatic-kernel-change-downgrade-to-4-19/32030)
> 
> Upgrading between major OS releases (e.g. Raspberry Pi OS Bullseye → Bookworm) via `apt full-upgrade` is *not* recommended; a clean flash of the new release image is the supported path to avoid partial‐upgrade failures. See [Upgrade rather than reinstall ↗](https://forums.raspberrypi.com/viewtopic.php?t=337992) or [Upgrade from 'Buster' to Raspberry Pi OS ↗](https://forums.raspberrypi.com/viewtopic.php?t=288172).

### 2. Enabling PWM
The BeagleY-AI has hardware PWM, but to use it you'll need to import the appropriate overlays on boot.

1. Open `/boot/firmware/extlinux/extlinux.conf` in a text editor. For example, `sudo nano /boot/firmware/extlinux/extlinux.conf`.
1. Locate the "microSD (default)" section at the end of the file.
1. Replace the commented `fdtoverlays` line with the following:

    ```
    fdtoverlays /overlays/k3-am67a-beagley-ai-pwm-epwm0-gpio12.dtbo /overlays/k3-am67a-beagley-ai-pwm-epwm1-gpio13.dtbo /overlays/k3-am67a-beagley-ai-pwm-epwm0-gpio5.dtbo /overlays/k3-am67a-beagley-ai-pwm-epwm1-gpio6.dtbo
    ```

1. The full section should look like this:
    ```
    label microSD (default)
        kernel /Image
        append console=ttyS2,115200n8 root=/dev/mmcblk1p2 ro rootfstype=ext4 rootwait net.ifnames=0 quiet
        fdtdir /
        fdt /ti/k3-am67a-beagley-ai.dtb
        fdtoverlays /overlays/k3-am67a-beagley-ai-pwm-epwm0-gpio5-gpio12.dtbo /overlays/k3-am67a-beagley-ai-pwm-epwm1-gpio6-gpio13.dtbo
        #initrd /initrd.img
    ```
1. Save the file. For Nano, hit `Ctrl-X` and then `Enter`.

### 3. Installing Python
The `pip` command available from the BeagleY-AI's core environment is locked, so you'll need to use a Python virtual environment.
- To create a new virtual enviornment: `python3 -m venv ~/YOUR_ENV`
- To activate an environment: `source ~/YOUR_ENV/bin/activate`
- To deactivate an environment: `deactivate`

> [!NOTE]
> You'll have to activate the virtual environment in every terminal you wish to run or manage your Python project from.

Within the virtual environment, install the required libraries:
```bash
pip install numpy python-periphery smbus2 inputs
```

### 4. Downloading code
1. To start operating a SCUTTLE with BeagleY-AI download these files:
    - [L1_encoder.py](https://www.mediafire.com/file/okivhm6k8538pmm/L1_encoder.py/file)
    - [L1_motor.py](https://www.mediafire.com/file/pbtqgwtd8ptlqk8/L1_motor.py/file)
    - [L1_gamepad.py] (WIP)
    - [L1_log.py] (WIP)
    - [L2_speed_control.py] (WIP)
    - [L2_kinematics.py] (WIP)
    - [L2_inverse_kinematics.py] (WIP)
    - [L3_gpDemo.py] (WIP)
