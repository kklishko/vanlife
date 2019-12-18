vanlife
=====

# Overview

The project and code here is based off the tutorial provided by Mike Murray on The Geek Pub, which can be found [here](https://www.thegeekpub.com/236867/using-the-dht11-temperature-sensor-with-the-raspberry-pi/).

# Quick start

## Requirements

The python code for data acquisition requires use of the package [Adafruit_DHT](https://github.com/adafruit/Adafruit_Python_DHT). Pip only allows for installing this package on Linux (as it queries `/proc` in order to determine the cpu architecture). Specifically, it was designed to operate off of a Raspberry Pi or Beaglebone Black, as per the project README.

Also, note that this package is considered deprecated. The prefered package is [CircuitPython](https://github.com/adafruit/Adafruit_CircuitPython_DHT), and there are plans to move to this package in the future. Additionally, Adafruit has a [project page](https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup) outlining use of this package with the DHT11 breakout board.

## Setup

First, make sure the raspberry pi is up-to-date. And then install the package using `pip`. The `Adafruit_DHT` README has instructions for installing from source, if that is preferred.

    sudo apt-get update
    sudo apt-get install python3-pip
    sudo python3 -m pip install --upgrade pip setuptools wheel
    sudo pip3 install Adafruit_DHT

## Remote Connection

TeamViewer version: 15.1.3937  (DEB)

Teamviewr ID: 1708004509