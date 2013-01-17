#! /usr/bin/python
# Listens on a GPIO pin for a button press Button must be installed with a pull-up resitor. 
# When detecting a low the script will look for emulators and kill the processes.
#
# Pin and emulators can be setup in /etc/external_emulator_reset.conf
#
# By Soren Blond Daugaard (sbd(at)ineptum.dk)
#

import RPi.GPIO as GPIO
import time
import os
import signal
import subprocess
import ConfigParser

config = ConfigParser.ConfigParser()
config.readfp(open('/etc/external_emulator_reset.conf'))

button_pin = config.getint('General','BUTTON_PIN')
emulators = config.get('General','EMULATORS')
sleep_interval = config.getint('General','POLL_TIME')

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN)

def kill_emulators():
	for emulator in emulators.split(','):
		proc = subprocess.Popen(["pgrep",emulator],  stdout=subprocess.PIPE)
		for pid in proc.stdout:
			os.kill(int(pid),signal.SIGTERM)


while 1:
	input_value = GPIO.input(button_pin)
	if not input_value:
		kill_emulators()
	time.sleep(sleep_interval)
