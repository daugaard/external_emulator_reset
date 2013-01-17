External Emulator Reset script for Raspberry Pi
===============================================
By Soren Blond Daugaard

The External Emulator Reset script will monitor an external button on Raspberry Pi and reset all emulators when pressed.

Install
-------
Install on the pi by doing the following:
> git clone git://github.com/daugaard/external_emulator_reset.git
> cd external_emulator_reset
> sudo ./install_script

The script will now start every time the pi is booted. Uninstall script is also included if needed.

Configuration
-------------
Edit the /etc/external_emulator_reset.conf to setup the input button and emulators in use. The button must be wired with a pull-up. 


