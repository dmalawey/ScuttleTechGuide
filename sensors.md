Author: David Malawey

By 2025 we have produced a solid number of sensor models that are popular in the maker community, commonly used in robotics, and recommended for integrating to pursue your robotics mission. As of December 2025 I will begin a library of models that have a clean CAD setup, accuratley matching real parts, and have been tested together with SCUTTLE electronics.

**Current & Power**
INA219 is a highly popular selection for DC current measurement & it reports over i2c.  We validated this sensor with the SCUTTLE motor driver, and it can attach to the dual-motor-driver power input terminals to indicate the total battery energy passing to the motors (or back, during recharge)

- ![image ina219](https://s3.amazonaws.com/gc-p/screenshots/pics/615126f5e9749a3070d1899707af0277/original.jpg)
- ![linked image ina](https://s3.amazonaws.com/gc-p/screenshots/pics/6c73b53ed12332f13ccd5ceebd52b541/original.JPG)
- ![linked image ina](https://s3.amazonaws.com/gc-p/screenshots/pics/1676e8444a0c78bd2e601f07b52e2441/original.JPG)

**Obstacles**
A newer technology than the extremely popular ultrasonic ranging sensor, VL53L0X is a time-of-flight sensor which is compact, highly accurage within a couple of mm, low cost, and easy to integrate.  Another i2c sensor readily found online and distributed globally.  This is not an exact replacement for the sonar type transducers: it measures a more narrow range using an infrared laser and performs nanosecond time measurement upon the pickup of the returned signal. This sensor can detect most obstacles but it is less suitable for checking walls, compared to ultrasonic options.  The power requirement is near zero, much less than HC-SR04.  For many years the HCSR04 was distributed with 5v input power meaning that it could not be powered with any of the many digital i/o pins on a microcontroller.  This VL53 unit can be powered with just about any pin.
Grab the [CAD model for VL53L0X here](https://grabcad.com/library/distance_sensor-1)

- ![linked image vl](https://s3.amazonaws.com/gc-p/screenshots/pics/f5448e5885d7e3fb3c4d58366ff12598/original.JPG)
- ![linked image vl](https://s3.amazonaws.com/gc-p/screenshots/pics/cda1c93d9aa5161a2e2e5f725b405375/original.JPG)
- ![linked image vl](https://s3.amazonaws.com/gc-p/screenshots/pics/9288873f93db424b96bf6e8e47437dd5/original.JPG)

**Vision**
The camera that we include in our SCUTTLE Kits is ultimately a sensor, communicating through USB and delivering vision data via pixels. We chose this design after testing several USB webcams and off-the-shelf selections including logitech and more. One important criteria for the camera was to have a microphone embedded.  The microphone is very rudimentary but is sufficient to capture speech-to-text and support interactive teleoperation of the robot. This compact square form factor is most common for industrial cameras, with a rugged steel case and interchangeable lenses. Our included selection is 720P which has proven more than sufficient for most machine-vision tasks. Working with the video feed in software, we found sometimes even downscaling the images to 256 pixels is preferred before processing the images, to balance speed and resolution. But, if you want to maintain the hardware design and gain more resolution, there are plenty of variants with 1080p or 4k resolution now. We have created a couple of different printable mounting solutions to attach the camera to 3030 rail, and our typical bracket includes an additional degree of freedom.  When the user configures SCUTTLE for a task, it is sometimes important to put the floor in view, or point upwards towards people.  Quickly make your adjustments and tighten the phillips screw to lock the angle in place.  Keep in mind that machine vision is a whole field of study and  
* Get the [Camera CAD model here](https://grabcad.com/library/scuttle-square-cam-v1-1)

- ![linked cam image](https://s3.amazonaws.com/gc-p/screenshots/pics/7146bfe8332c0045e1d6df665cb4e2b2/original.JPG)
- ![linked cam image 2](https://s3.amazonaws.com/gc-p/screenshots/pics/8f3e0d22c330675428de6a53e7be8775/original.JPG)
- ![linked cam image 3](https://s3.amazonaws.com/gc-p/screenshots/pics/876a55f4de1542a1341cadf317db3d78/original.PNG)

**Motor Driver**
This is the dual-motor driver included with SCUTTLE v3, and we are grouping it with "sensors" since it is a modular i/o device that can be independently added, wired in, and tested just like a sensor.  This is a step-up from the extremely popular L298N boards, where they are both H-bridge devices or MOSFETS, delivering a current to the output terminals in proportion to the input signals in PWM.  Robotics designers should know this is our most highly recommended mass-produced driver board for those who want to learn PWM control functions with a hands-on device, and you need more current (this offers up to 5A per channel, 10A total) and up to 40 volts.  For SCUTTLE this is the solution that controls two DC motors but for mechatronics this is an easy variable-control output device for any DC actuator including LED lamps or pumps, etc.  This model was remade december 2025 for a very good example of designing a simple circuit board in Solidworks.  Follow the feature tree or even duplicate this model and adjust the board size, hole spacing easily to produce another circuit CAD design.

As for purchasing options, HW231 is not a highly standard name of a board, so also search MC33886, which is the name of the driver chip on the board.  This can be found as low as $12 per piece and should be available in any country.  
* Get the [motor driver CAD model here](https://grabcad.com/library/hw231-1)

- ![linked driver image](https://s3.amazonaws.com/gc-p/screenshots/pics/4b95be0b44cfbaa3e54cc167a026bf80/original.jpg)
- ![linked image 2](https://s3.amazonaws.com/gc-p/screenshots/pics/7939f29b547aecdc46b2c049dcba83c0/original.jpg)
- ![linked image 3](https://s3.amazonaws.com/gc-p/screenshots/pics/d552e5d8f4d2722be0ddddf76658d6a6/original.jpg)
