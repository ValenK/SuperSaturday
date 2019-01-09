import RPi.GPIO as GPIO
import time

def BlinkFun(t,pin):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(t)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(t)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

LoopBlinks=10

cnt=0

while cnt<=LoopBlinks:
    BlinkFun(.2,17)
    print("blink",cnt)
    cnt+=1

GPIO.cleanup()
