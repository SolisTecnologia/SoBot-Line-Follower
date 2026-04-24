# Solis Robot - SoBot
![](https://github.com/SolisTecnologia/SoBot-Line-Follower/blob/master/png/SoBotSingleLF.png)
# Introduction

AMR (autonomous mobile robotics) platform equipped with a camera system, ultrasonic and photoelectric sensors, works with a high rate of precision and repeatability of its movements, as it uses stepper motors in its movement and navigation, the SoBot also can be termed as a research and development interface, as it facilitates the practical experimentation of algorithms from the simplest to the most complex level.

This product was developed 100% by Solis Tecnologia, and has a lot of technology employing cutting-edge concepts, such as:

The motors can be controlled simultaneously or individually.
The user can select different accessories to implement to the robot.
Several programming languages can be used to connect via API.

# Components

* Main structure in aluminum
* Robot Control Driver
* Raspberry Pi 4B board <img align="center" height="30" width="40" src="https://github.com/devicons/devicon/blob/master/icons/raspberrypi/raspberrypi-original.svg">
* 2x NEMA-23 Stepper Motors
* 2x 12V/5A battery

# Programming Example
## Line Follower - [Line_Sensor.py](https://github.com/SolisTecnologia/SoBot-Line-Follower/blob/master/Line_Sensor.py)
Programming example for the Solis robot to move following a line.

This example uses 3 line sensors where the middle sensor reads black line and the tip sensors read the white floor to move.

### Programming Language

* Python <img align="center" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">

### ⚠️ Important

We recommend **avoiding general library updates** (`pip install --upgrade`).

**Why?**  
Some libraries (e.g. NumPy) introduce significant changes between versions that can break code that was previously working perfectly.

### ✅ Recommended Best Practice:

- Update **libraries individually**, one at a time:
  ```bash
  pip install numpy==2.2.6   # example of a stable version

### Required Libraries

~~~python
from time import sleep
import serial
~~~

The ''time'' library is needed to generate time delays and the ''serial'' library for serial/usb Raspberry connection with the robot controller driver.

### Code Description

The commands used in this example to control SoBot are continuous movement commands, as follows:

~~~python
usb.write(b"MT0 MC AT100 DT100 V2") # Parameter settings for continuous mode
usb.write(b"MT0 ME1")               # Enable continuous movement
usb.write(b"MT0 ME0")               # Disable continuous movement
usb.write(b"MT0 ML")                # Move left
usb.write(b"MT0 MR")                # Move right
usb.write(b"MT0 MB")                # Move backward
usb.write(b"MT0 MF")                # Move Forward
usb.write(b"MT0 MP")                # Pause movement
~~~

Commands are also used to control the lighting of the LED tape and the command to read the line sensors, as follows:

~~~python
usb.write(b"LT E1 RD0 GR50 BL0")    # Turn on led tape in green

usb.write(b"SL")                    # Send command to read line sensor
~~~

The command return for reading the line sensors are stored in the Array variable **data_line**.

~~~python
data_line = usb.readline()          # Read data
~~~

For more information about the commands used, check the Robot Commands Reference Guide.

### Flowchart

![](https://github.com/SolisTecnologia/SoBot-Line-Follower/blob/master/png/Flowchart_Line_Sensor.png)

# Reference Link
[SolisTecnologia website](https://www.solistecnologia.com.br/produtos/estacoes_sobot)

# Please Contact Us
If you have any problem when using our robot after checking this tutorial, please contact us.

### Phone:
+55 1143040786

### Technical support email: 
contato@solistecnologia.com.br

![](https://github.com/SolisTecnologia/SoBot-Line-Follower/blob/master/png/logo.png)
