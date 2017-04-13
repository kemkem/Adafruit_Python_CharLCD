#!/usr/bin/python

# Example for the following hardware:
# LCD:       https://www.adafruit.com/products/181
# Backplate: https://www.adafruit.com/products/292

# /!\ Backlight must be set physically using the provided variable resistor
# Or by simply putting LCD Pin "16" to ground (ie: linked to pin 1) (max backlight)
# Also, be sure to twek contrast correctly otherwise you may not see anything

import time
import Adafruit_GPIO.MCP230xx as MCP
import Adafruit_CharLCD as LCD

# Can be selected using A0-A1-A3 (default 0x20, up to 0x27)
address = 0x20
lines = 16
cols = 2

# Virtual GPIO using the MCP chip from the backplate
gpio = MCP.MCP23008(address)

# Pin-out extracted from Adafruit_LiquidCrystal.cpp
# from https://github.com/adafruit/Adafruit_LiquidCrystal
# 
#  _rs_pin = 1;
#  _rw_pin = 255;
#  _enable_pin = 2;
#  _data_pins[0] = 3;  // really d4
#  _data_pins[1] = 4;  // really d5
#  _data_pins[2] = 5;  // really d6
#  _data_pins[3] = 6;  // really d7
lcd = LCD.Adafruit_CharLCD(1, 2, 3, 4, 5 , 6, lines, cols, gpio=gpio, backlight=7, invert_polarity=False)

lcd.clear()
time.sleep(1)

lcd.message('Line 1\nLine 2')
time.sleep(1)

lcd.clear()
lcd.message('\nLine 2 Only')

lcd.clear()
lcd.message('Off in 3 sec...')
time.sleep(3)

lcd.backlightOff()
