#!/usr/bin/python3
"""
Solis Robot - SoBot

Line_Sensor.py: Programming example for the Solis robot to move following a line.

Created By   : Vinicius M. Kawakami and Rodrigo L. de Carvalho
Version      : 1.1

Company: Solis Tecnologia
"""

from time import sleep
import serial

flag_fw = 0
flag_enable = 1
count_bl = 0

black = 49
white = 48

# Set serial port
usb = serial.Serial('/dev/ttyACM0', 57600, timeout=0, dsrdtr=False)
usb.flush()     # Waits data configuration

usb.write(b"LT E1 RD0 GR50 BL0")    # Turn on led tape in green

sleep(2)
usb.write(b"MT0 MC MD1 RI50 AT100 DT100 V3") # Parameter settings for continuous mode
sleep(1)
usb.write(b"MT0 ME1")               # Enables wheel motors on mode continuous
sleep(1)

while flag_enable == 1:

    usb.write(b"SL")            # Send command to read line sensor
    sleep(0.1)                  # Wait to return datas
    data_line = usb.readline()  # Read data
    
    #b'SL1 1 SL2 1 SL3 1\r\n' 

    left_sensor = data_line[4]
    central_sensor = data_line[10]
    right_sensor = data_line[16]

    print(f"Left: {left_sensor} - Central: {central_sensor} - Right: {right_sensor}")

    # Check if central sensor is reading black line or if all sensors are reading black
    if(((left_sensor == white) and (central_sensor == black) and (right_sensor == white)) or
     ((left_sensor == black) and (central_sensor == black) and (right_sensor == black))):
        if(flag_fw == 0):
            flag_fw = 1
            usb.write(b"LT E1 RD0 GR50 BL0")
            usb.write(b"MT0 MF")    # Moving to forward

    # Check if left and central sensor is reading black
    elif((left_sensor == black) and (central_sensor == black) and (right_sensor == white)):
        flag_fw = 0
        count_bl = 0
        usb.write(b"LT E1 RD0 GR0 BL50")
        usb.write(b"MT0 ML")        # Turn left
        sleep(0.4)
        # usb.write(b"MT0 MF")
        # sleep(0.1)

    # Check if only left sensor is reading black
    elif((left_sensor == black) and (central_sensor == white) and (right_sensor == white)):
        flag_fw = 0
        count_bl = 0
        usb.write(b"LT E1 RD0 GR0 BL50")
        usb.write(b"MT0 ML")        # Turn left
        sleep(0.7)
        # usb.write(b"MT0 MF")
        # sleep(0.1)

    # Check if central and right sensor is reading black
    elif((left_sensor == white) and (central_sensor == black) and (right_sensor == black)):
        flag_fw = 0
        count_bl = 0
        usb.write(b"LT E1 RD0 GR15 BL25")
        usb.write(b"MT0 MR")        # Turn right
        sleep(0.4)
        # usb.write(b"MT0 MF")
        # sleep(0.1)

    # Check if only right sensor is reading black
    elif((left_sensor == white) and (central_sensor == white) and (right_sensor == black)):
        flag_fw = 0
        count_bl = 0
        usb.write(b"LT E1 RD0 GR15 BL25")
        usb.write(b"MT0 MR")        # Turn right
        sleep(0.7)
        # usb.write(b"MT0 MF")
        # sleep(0.1)
        
    # Check if all sensor is reading white
    elif((left_sensor == white) and (central_sensor == white) and (right_sensor == white)):
        flag_fw = 0
        count_bl += 1
        usb.write(b"LT E1 RD50 GR0 BL0")
        usb.write(b"MT0 MB")        # Moving to back
        sleep(0.5)

        if(count_bl >= 5):
            flag_enable = 0


usb.write(b"MT0 MP")                # Moviment Pause
sleep(0.5)
usb.write(b"MT0 ME0")               # Disables wheel motors on mode continuous
usb.write(b"LT E1 RD0 GR0 BL0")
sleep(0.5)
usb.write(b"LT E1 RD50 GR0 BL0")
sleep(0.5)
usb.write(b"LT E1 RD0 GR0 BL0")
sleep(0.5)
usb.write(b"LT E1 RD50 GR0 BL0")
sleep(0.5)
usb.write(b"LT E1 RD0 GR0 BL0")
sleep(0.5)
usb.write(b"LT E1 RD50 GR0 BL0")
sleep(0.5)
usb.write(b"LT E1 RD0 GR0 BL0")
usb.write(b"LT E0")