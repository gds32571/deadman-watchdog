# deadman-watchdog
These are the python programs for deadman and watchdog

The watchdog program runs on a RPi (the home automation server typically) and listens for TCP connections from various computers or applications.  When a connection is made, the program responds with a serial number, then sends an MQTT message to the HA server.  The HA server uses these messages to display the status of the computer/application in Home Assistant. If a computer goes more than 75 seconds without making a connection, the watchdog sends an 'off' MQTT message to HA which then displays an off icon.

The deadman program runs on a client computer to:
   1. Signals the attending UPS that it is up and goin, avoiding an UPS controlled reboot.
   2. Makes a TCP connection to the watchdog, for status display in Home Assistant.
   
