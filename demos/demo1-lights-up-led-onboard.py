from machine import Pin
import time


led = Pin("LED",Pin.OUT)

def short():
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
    
def long():
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(0.5)

while True: 
    #led.on()
    #time.sleep(0.5)
    #led.off()
    #time.sleep(0.5)
    short()
    long()
    

