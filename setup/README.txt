Steps to successful first time setup

Mechanical Assembly & Setup: 

    Tools you will need: 
	Allen Keys (")

Operating System + Programming Setup: 

    Image RPi with latest Raspbian release or other preferred OS

    enable i2c
    (Optional) enable ssh, & vnc if preferred
    (Optional) install and setup samba 

    install python 3

    	sudo apt install python3
	sudo apt upgrade python3

    Install other necessary libraries/tools:
    
	sudo apt-get install i2c-tools
    	sudo apt-get install python3-smbus
    	pip3 install customtkinter 

    clone this github repo to a location on RPi: 

        https://github.com/mpeccable/armold/tree/main

    Connect PCA9865 driver to pi. View the following link for circuit diagram and other information.

	https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/hooking-it-up

    Run i2c detect to check connection

        i2cdetect -y 1 

    If connected to 0x40 (see i2cdetect image for details), locate repo and execute 

        python3 Servo.py
        
    to run Servo.py, which enables Servo power and sends the output shaft
    to the "zeroed" position. 

    Make sure to attach servo horns WHILE RUNNING Servo.py and powering the servos. This will 
    ensure that the servos are "zeroed". This is a necessary calibration step.

 