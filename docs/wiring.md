# Wiring Guide
All about the wiring of electronics for your robot. This page is divided into signal wires & power wires.

Wiring may depend on the compute board you select. The following boards have variations in their wiring:

* [Raspberry Pi 3/4/5](boards/raspberry-pi/wiring-guide.md)
* [TI SK-TDA4VM](boards/tda4vm/wiring-guide.md)
* [BeagleY-AI](boards/beagley-ai/wiring-guide.md)
* [Axiomtek Intel-based CAPA55R](boards/capa55r/wiring-guide.md)

## Signals

Signal wires perform the communication on your robot, between sensors, CPU, and actuators.  Several wires make up a cable, and the cables get plugged in when you build your robot.
All signals on SCUTTLE can be made with regular off-the-shelf Dupont-style terminals, all female.  Lengths are 10cm and 20cm as shown.

> [!NOTE]
> Do not peel the wires apart. Keep them bonded for strong and organized connections.

![dupont cables photo](https://i.imgur.com/YN3LAEp.jpg)

> Colors Selection

We chose the colors to make good use of any pack of wires.  When you add sensors and actuators, try to stay consistent.

| Function | Preferred Color |
| ------ | ----------------- |
| Ground | Black, Brown, Green |
| Power, 3.3v | Red, Purple |
| PWM signals | Orange, Yellow |
| CLOCK (I2C) | Gray |
| SIGNAL (I2C) | White |

### Cables

This section covers cables you can DIY.

??? "Cable Diagrams"
    To build signal cables, use these diagrams.

    ![cable-encoder-l](image/wg_cable_encoder_lh.png ':class=image-25')

    _Figure: cables for left encoder_

    ![cable-encoder-R](image/wg_cable_encoder_rh.png ':class=image-25')

    _Figure: cables for right encoder_

    ![cable-motor](image/wg_cable_motor.png ':class=image-25')

    [grab the diagram](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=diagram1.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1yAXCKNeVdJE7FfkX81iIosMF-5VFMIfJ%26export%3Ddownload)

    _Figure: cables for motor_

    ![cable-i2c](image/wg_cable_i2c.png ':class=image-25')

    _Figure: cables for i2c_


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

The connections from SBC to the motor driver may depend on which compute board you're using:

* [Raspberry Pi 3/4/5](boards/raspberry-pi/wiring-guide.md#motors)
* [BeagleY-AI](boards/beagley-ai/wiring-guide.md#motors)

### Source: Battery

![battery image](image/wg_battery.png ':class=image-25')

_Figure: battery components_

## Addons

> This section to include popular addons such as RPLIDAR, ultrasonic sensor, and more.
> It will contain circuitry-related information for planning power and signals to your actuators.

---
