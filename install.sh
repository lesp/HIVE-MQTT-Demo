#! /bin/bash

echo "Installing software for MQTT on Raspberry Pi"
sleep 1
sudo su
apt update && apt install mosquitto mosquitto-clients python3-w1thermsensor && pip3 install paho-mqtt

echo "Now you need to enable the one wire interface using the Raspberry Pi Preferences applications"
