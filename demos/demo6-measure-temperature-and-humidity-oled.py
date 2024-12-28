from machine import Pin, I2C
from dht import DHT11
import utime
from ssd1306 import SSD1306_I2C


WIDTH = 128
HEIGHT = 64

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.fill(0)

x = 0
y = 0

def calculateXY():
    print(f'{x}, {y}')
    if x < 10 and y == 0:
        x = x + 1
    elif x == 10 and y < 10:
        y = y + 1
    elif x > 0 and y == 10:
        x = x - 1
    elif x == 0 and y > 0:
        y = y - 1

while True:
    oled.fill(0)
    utime.sleep(0.2)
    sensor = DHT11(Pin(3))
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()
    print(t, h)
    oled.pixel(x, y, 1)
    x = x + 1
    if x > 10:
        x = 0
    #calculateXY()
    oled.text(f'Temperature: {t}', 0, 10)
    oled.text(f'Humidity: {h}', 0, 20)
    oled.show()
    
