# Wiring Guide

>
> All about the wiring of electronics for your robot. This page is divided into signal wires & power wires.  As of 2025, find the full wiring documentation in archives under "wiring guide."  Our goal is to break down this guide into pieces and include them directly here in the github.  In that way, users can download individual pieces and collaborators can improve the diagrams and push updates in the github.  We now use draw.io for easy diagrams with good quality while powerpoint has been used in the past. 
>

Here's a preview of the wiring for the Pi and TI configurations.  Proceed to the subsections for details.

| Pi Wiring Thumbnail | TI wiring thumbnail | BeagleY-AI Thumbnail |
| ------------------- | ------------------- | -------------------- |
| ![img](image/wg_overview_pi.png) | ![img](image/wg_overview_TDA4VM.png) | ![img](image/wg_overview_byai.png) |

# Templates
_template for diagrams_
We're publishing an open source diagrams packet so you can access the working files and use them for your project!  This includes wiring diagrams, cable diagrams, routing diagrams, and more!  Access these examples and you can use the .drawio files relating to your project to make great documentation.  The packet ranges from 2023-2025 and many individual diagrams are unfinished or not yet up to standard.  But it's certainly enough to get you some good examples.
* [download PDF packet](https://github.com/dmalawey/ScuttleTechGuide/blob/06d364108e8cc1c2e09686d637b52af152cc41cd/docs/2025_DiagramsPacket.pdf)
* [download .drawio files](https://github.com/dmalawey/ScuttleTechGuide/blob/06d364108e8cc1c2e09686d637b52af152cc41cd/docs/2025.12_SCTLwiringPacket.zip) (6Mb zip file with .drawio files)

## Signals

Signal wires perform the communication on your robot, between sensors, CPU, and actuators.  Several wires make up a cable, and the cables get plugged in when you build your robot.
All signals on SCUTTLE can be made with regular off-the-shelf Dupont-style terminals, all female.  Lengths are 10cm and 20cm as shown.

## Standards

We chose the colors to make good use of any pack of wires.  When you add sensors and actuators, try to stay consistent.

| Function | Preferred Color |
| ------ | ----------------- |
| Ground | Black, Brown, Green |
| Power, 3.3v | Red, Purple |
| PWM signals | Orange, Yellow |
| CLOCK (i2C | Gray |
| SIGNAL (i2C) | White |


See the following exported images for the standard diagrams in our wires.  We aim to keep alignment of graphics including wire colors, scale of diagram parts, to have diagram colors that match real life, and use connector graphics that show the configuration of orientations and terminals arrangement.

- ![img](img/wiring_standards_cables1.jpg)
- ![img](img/wiring_standards_cables2.jpg)
- ![img](img/wiring_standards_connector1.jpg)
- ![img](img/wiring_standards_connector2.jpg)


### Cables


**Signals Routing**
The following image shows the routing of signals for PWM on the robot.  Then see the routing of signals for i2c.  Last, find the pinout designations for the i2c-based encoders.

- ![diagram, wiring signals for PWM](img/wiring_signals_routing2.jpg)
- ![diagram, wiring signals for i2C](img/wiring_signals_routing1.jpg)
- ![diagram, wiring signals pinout1.jpg](img/wiring_signals_pinout1.jpg)


The following diagrams give motor signals, motor power, motor pinout with images.

- ![img](img/wiring_motor_signals.jpg)
- ![img](img/wiring_motor_power.jpg)
- ![img](img/wiring_motor_pinout.jpg)

## Power

### Power Routing

The overview for power cables on SCUTTLE v3

![power overview](image/wg_overview_power.png ':class=image-25')

_Figure: power overview_

Here are the cables to power the motors from the motor driver.

![motor leads](image/wg_motor_leads.png ':class=image-25')

_Figure: motor leads_

### Actuator: Motor Driver

The cables to power the motor driver from 12v.

![motor driver](image/wg_motor_driver.png ':class=image-25')

_Figure: motor driver wiring_

|The motor wires to communicate from CPU to the motor driver| BeagleY-AI Connectivity|
|--------------| -------------- |
|![motor leads](image/wg_cable_motor_signal.png)| ![Beagle motor leads](image/Beagle_wiring_whitebg.png)|

_Figure: motor signal cable_

### Source: Battery

![battery image](image/wg_battery.png ':class=image-25')

_Figure: battery components_

## Addons

> This section to include popular addons such as RPLIDAR, ultrasonic sensor, and more.
> It will contain circuitry-related information for planning power and signals to your actuators.

---
