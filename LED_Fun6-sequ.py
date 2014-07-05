#!/usr/bin/env python
#
# Raspberry Pi Class.
# David M. N. Bryan, dave@drstrangelove.net
#
# This is licend under creative commons license:
# http://creativecommons.org/licenses/by-nc-sa/3.0/
# Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)
#

#import the Raspberry Pi GPIO Library
import RPi.GPIO as GPIO
import time

# Define OUTPUT Pins on RPI for the LEDs
GPIORed_PIN=27
GPIOGreen_PIN=17
GPIOBlue_PIN=22

# How about some input please?
BUTTON1_PIN=24
BUTTON2_PIN=25

# How long do we sleep between cycles
SLEEP_TIME=1

# Set the pins on the GPIO up.

# Setup the OUTPUTS (LEDS)
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIORed_PIN, GPIO.OUT)
GPIO.setup(GPIOGreen_PIN, GPIO.OUT)
GPIO.setup(GPIOBlue_PIN, GPIO.OUT)

#Setup the INPUTs (Buttons)
GPIO.setup(BUTTON1_PIN, GPIO.IN)
GPIO.setup(BUTTON2_PIN, GPIO.IN)

def blink_all_leds(SLEEP_TIME):
        GPIO.output(GPIORed_PIN, True)
        GPIO.output(GPIOGreen_PIN, True)
        GPIO.output(GPIOBlue_PIN, True)
        time.sleep(SLEEP_TIME)
        GPIO.output(GPIORed_PIN, False)
        GPIO.output(GPIOGreen_PIN, False)
        GPIO.output(GPIOBlue_PIN, False)
        time.sleep(SLEEP_TIME)

def blink_led(COLOR, SLEEP_TIME):
  switch (COLOR) {

    case RED:
        GPIO.output(GPIORed_PIN, True)
        time.sleep(SLEEP_TIME)
        GPIO.output(GPIORed_PIN, False)
        time.sleep(SLEEP_TIME)

    case GREEN:
        GPIO.output(GPIOGreen_PIN, True)
        time.sleep(SLEEP_TIME)
        GPIO.output(GPIOGreen_PIN, False)
        time.sleep(SLEEP_TIME)

    case BLUE:
        GPIO.output(GPIOBlue_PIN, True)
        time.sleep(SLEEP_TIME)
        GPIO.output(GPIOBlue_PIN, False)
        time.sleep(SLEEP_TIME)

while True:

  if ( GPIO.input(BUTTON1_PIN) == True ):
	blink_all_leds(1)
	BUTTONPushed += 1

  if ( GPIO.input(BUTTON2_PIN) == True ):
	blink_all_leds(0.10)
	BUTTONPushed += 1

  if ( BUTTONPushed >= 2):
	print "Someone pushed both buttons! %d" % (BUTTONPushed)
	blink_led("RED", .5)
