# Wiring Guide

All about the wiring of electronics for your robot. This page is divided into signal wires & power wires.  As of 2025, find the full wiring documentation in archives under "wiring guide."  Our goal is to break down this guide into pieces and include them directly here in the github.  In that way, users can download individual pieces and collaborators can improve the diagrams and push updates in the github.  We now use draw.io for easy diagrams with good quality while powerpoint has been used in the past. 

![img](img/wiring_bot_routing1.jpg)

## Signals

Signal wires perform the communication on your robot, between sensors, CPU, and actuators.  Several wires make up a cable, and the cables get plugged in when you build your robot.
All signals on SCUTTLE can be made with regular off-the-shelf Dupont-style terminals, all female.  Lengths are 10cm and 20cm as shown.

**Signals Routing**
The following image shows the routing of signals for PWM on the robot. Then see the routing of signals for i2c.  Having i2c already distributed on a simple breakout board gives the users access to A) probe the signals during operation for troubleshooting or B) connect further sensors, since i2c is the most popular communication protocol for off-the-shelf sensors. Last, find the pinout designations for the i2c-based encoders. Note the encoders have one difference and that is to drive the pulldown pin necessary for changing the i2c address.  By differentiating the addresses, we can communicate with both sensors on the same lines simultaneously.

- ![diagram, wiring signals for PWM](img/wiring_signals_routing2.jpg)
- ![diagram, wiring signals for i2C](img/wiring_signals_routing1.jpg)
- ![diagram, wiring signals pinout1.jpg](img/wiring_signals_pinout1.jpg)

## Motor

The following diagrams give motor signals, motor power, motor pinout with images.

**Motor Pinout:**  The motor driver is shown which receives two pairs of PWM signals.  One PWM signal can control the speed of a motor, but two are required to implement both forward and reverse.  Input 1 and 2 control the right-hand motor, and correspond to output 1 and 2.  The input ranges 0-100% PWM at 3.3v while the output ranges 0-12v where 12v is the input voltage level.  This motor driver board features two independent h-bridge MOSFETs has its very own detailed datasheet for those who wish to explore.

**Motor Power** The power diagram shows an anderson power connector which is appropriate for the 18awg paired wire, where the anderson pair can plug into the battery directly. However, in the latest v3 robot we have simple ferrules crimped on the end of this cable and tie it into power at the power distribution terminals, which are DIN terminals.   The motor wires are soldered into the motor terminals with polarity reversed for left and right, so the positive signals from the CPU ultimately give "forward" motion while each motor turns opposite from each other.   Users can duplicate this exact setup for powering LEDs, fans, or other DC actuators with the same stack of software, wiring, connections, and PWM scheme.

- ![img](img/wiring_motor_signals.jpg)
- ![img](img/wiring_motor_power.jpg)
- ![img](img/img_placeHolder.jpg)

## Power

See the power and signals across the whole robot for scuttle v3 with raspberry pi.

The first diagram shows all main cables, and the second diagram shows only the power cables.  

- ![img](img/wiring_bot_power1.jpg)
- ![img](img/wiring_bot_routing1.jpg)
- ![img](img/img_placeHolder.jpg)
  
## Addons

> This section to include popular addons such as RPLIDAR, ultrasonic sensor, and more.
> It will contain circuitry-related information for planning power and signals to your actuators.

---


# Templates
_template for diagrams_
We're publishing an open source diagrams packet so you can access the working files and use them for your project!  This includes wiring diagrams, cable diagrams, routing diagrams, and more!  Access these examples and you can use the .drawio files relating to your project to make great documentation.  The packet ranges from 2023-2025 and many individual diagrams are unfinished or not yet up to standard.  But it's certainly enough to get you some good examples.
* [download PDF packet](https://github.com/dmalawey/ScuttleTechGuide/blob/06d364108e8cc1c2e09686d637b52af152cc41cd/docs/2025_DiagramsPacket.pdf)
* [download .drawio files](https://github.com/dmalawey/ScuttleTechGuide/blob/06d364108e8cc1c2e09686d637b52af152cc41cd/docs/2025.12_SCTLwiringPacket.zip) (6Mb zip file with .drawio files)

## Standards

We chose the colors to make good use of any pack of wires.  When you add sensors and actuators, try to stay consistent.

| Function | Preferred Color |
| ------ | ----------------- |
| Ground | Black, Brown, Green |
| Power, 3.3v | Red, Purple |
| PWM signals | Orange, Yellow |
| CLOCK (i2C | Gray |
| SIGNAL (i2C) | White |

See the following exported images for the standard diagrams in our wires.  We aim to keep alignment of graphics including wire colors, scale of diagram parts, to have diagram colors that match real life, and use connector graphics that show the configuration of orientations and terminals arrangement.  Years of projects went into the decisions of how to layout graphics to make the actual engineering and building easier.  And it pays off.  You're encouraged to take these templates, make your design documents shine and make everything modifiable from the ground up.

- ![img](img/wiring_standards_cables1.jpg)
- ![img](img/wiring_standards_cables2.jpg)
- ![img](img/img_placeHolder.jpg)

The next diagrams have the famous 40-pin header found on raspberry Pi and many other microcontrollers.  We found that successfully implementing a team project that adds a sensor is repeatedly dependent on clear plans for the hookup of the terminals.  There is one stage where we simply "find a pin that works" but when designing, there is much higher discretion.  Can we connect the cables without overlaping existing connections, and together in a way that fits in one dupont housing?  These graphics become a designer's toolkit so the design is enhanced by the documentation during the work.  Use your wiring diagram in realtime to survey the pin locations and find the right spot for your next connection.

- ![img](img/wiring_standards_connector1.jpg)
- ![img](img/wiring_standards_connector2.jpg)
- ![img](img/img_placeHolder.jpg)
