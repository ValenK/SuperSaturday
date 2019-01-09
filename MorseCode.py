import RPi.GPIO as GPIO
import time

def dot(pin):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(ts)
	GPIO.output(pin,GPIO.LOW)
def dash(pin):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(td)
	GPIO.output(pin,GPIO.LOW)
def partspace(pin):
	GPIO.output(pin,GPIO.LOW)
	time.sleep(ts)
	GPIO.output(pin,GPIO.LOW)
def wordspace(pin):
	GPIO.output(pin,GPIO.LOW)
	time.sleep(tws)
	GPIO.output(pin,GPIO.LOW)
def letterspace(pin):
	GPIO.output(pin,GPIO.LOW)
	time.sleep(td)
	GPIO.output(pin,GPIO.LOW)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

pn=17
ts=.3
td=3*ts
tws=7*ts

#V
dot(pn)
partspace(pn)
dot(pn)
partspace(pn)
dot(pn)
partspace(pn)
dash(pn)
letterspace(pn)
#A
dot(pn)
partspace(pn)
dash(pn)
letterspace(pn)
#L
dot(pn)
partspace(pn)
dash(pn)
partspace(pn)
dot(pn)
partspace(pn)
dot(pn)
letterspace(pn)
#E
dot(pn)
letterspace(pn)
#N
dash(pn)
partspace(pn)
dot(pn)




	
	
GPIO.cleanup()
