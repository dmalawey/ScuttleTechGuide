# Wiring Guide

>
> All about the wiring of electronics for your robot.
> This page is divided into signal wires & power wires.
>

Here's a preview of the wiring for the Pi and TI configurations.  Proceed to the subsections for details.

| Pi Wiring Thumbnail | TI wiring thumbnail | BeagleY-AI Thumbnail |
| ------------------- | ------------------- | -------------------- |
| ![img](image/wg_overview_pi.png) | ![img](image/wg_overview_TDA4VM.png) | ![img](image/wg_overview_byai.png) |



## Signals

Signal wires perform the communication on your robot, between sensors, CPU, and actuators.  Several wires make up a cable, and the cables get plugged in when you build your robot.
All signals on SCUTTLE can be made with regular off-the-shelf Dupont-style terminals, all female.  Lengths are 10cm and 20cm as shown.

> ⚠️Please do not peel the wires apart! Keep them bonded for strong connections.

![dupont cables photo](https://i.imgur.com/YN3LAEp.jpg ':class=image-25')

> Colors Selection

We chose the colors to make good use of any pack of wires.  When you add sensors and actuators, try to stay consistent.

| Function | Preferred Color |
| ------ | ----------------- |
| Ground | Black, Brown, Green |
| Power, 3.3v | Red, Purple |
| PWM signals | Orange, Yellow |
| CLOCK (i2C | Gray |
| SIGNAL (i2C) | White |

### Cables

This section covers cables you can DIY.

<div class="accordion">

<details>
  <summary>Cable Diagrams</summary>

To build signal cables, use these diagrams.

![cable-encoder-l](image/wg_cable_encoder_lh.png ':class=image-25')

_Figure: cables for left encoder_

<br/><br/>

![cable-encoder-R](image/wg_cable_encoder_rh.png ':class=image-25')

_Figure: cables for right encoder_

<br/><br/>

![cable-motor](image/wg_cable_motor.png ':class=image-25')

[grab the diagram](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=diagram1.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1yAXCKNeVdJE7FfkX81iIosMF-5VFMIfJ%26export%3Ddownload)

_Figure: cables for motor_

<br/><br/>

![cable-i2c](image/wg_cable_i2c.png ':class=image-25')

_Figure: cables for i2c_

</details>

</div>





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
