import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
G=17
R=22
Y=18
c=0
#while c<20:
	#GPIO.output(G,GPIO.HIGH)
	#time.sleep(.2)
	#GPIO.output(G,GPIO.LOW)
	#GPIO.output(R,GPIO.HIGH)
	#time.sleep(.2)
	#GPIO.output(R,GPIO.LOW)
	#c+=1
	
c=0

while c<20:
	GPIO.output(G,GPIO.HIGH)
	time.sleep(2)
	GPIO.output(G,GPIO.LOW)
	GPIO.output(Y,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(Y,GPIO.LOW)
	GPIO.output(R,GPIO.HIGH)
	time.sleep(2)
	GPIO.output(R,GPIO.LOW)
	c+=1
