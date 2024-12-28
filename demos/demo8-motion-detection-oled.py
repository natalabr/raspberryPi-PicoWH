from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime
import machine


WIDTH = 128
HEIGHT = 64

PIR = Pin(15, Pin.IN, Pin.PULL_UP)

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.fill(0)

while True:
    if PIR.value() == 0:
        oled.text("GO NINJA", 0, 10)
    else:
        oled.text("GO TO SLEEP", 0, 20)
        
    oled.show()
    utime.sleep(1)
    oled.fill(0)
