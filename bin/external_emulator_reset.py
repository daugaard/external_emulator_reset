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

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

def kill_emulators():
	proc = subprocess.Popen(["pgrep","osmose"],  stdout=subprocess.PIPE)
	for pid in proc.stdout:
		os.kill(int(pid),signal.SIGTERM)
	proc = subprocess.Popen(["pgrep","retroarch"],  stdout=subprocess.PIPE)
	for pid in proc.stdout:
		os.kill(int(pid),signal.SIGTERM)
	


while 1:
	input_value = GPIO.input(4)
	if not input_value:
		print "External reset received - Killing emulators"
		kill_emulators()
	time.sleep(1)
