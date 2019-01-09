import RPi.GPIO as GPIO
import time
import math

def DisplayDigit(Num):
	if Num<=9:
		DisplaySingleDigit(Num)
	if Num>9:
		First_Digit=math.floor(Num/10)
		#print(First_Digit)
		Second_Digit=Num%10
		#print(Second_Digit)
		DisplaySingleDigit(First_Digit)
		time.sleep(.25)
		AllOff()
		time.sleep(.1)
		DisplaySingleDigit(Second_Digit)
		time.sleep(.25)
		

def DisplaySingleDigit(Num):
	if Num==0:
		GPIO.output(A,GPIO.HIGH)
		GPIO.output(B,GPIO.HIGH)
		GPIO.output(C,GPIO.HIGH)
		GPIO.output(D,GPIO.HIGH)
		GPIO.output(E,GPIO.HIGH)
		GPIO.output(F,GPIO.HIGH)
	if Num==1:
		GPIO.output(B,GPIO.HIGH)
		GPIO.output(C,GPIO.HIGH)
	if Num==2:
		GPIO.output(A,GPIO.HIGH)
		GPIO.output(B,GPIO.HIGH)
		GPIO.output(G,GPIO.HIGH)
		GPIO.output(E,GPIO.HIGH)
		GPIO.output(D,GPIO.HIGH)
	if Num==3:
		GPIO.output(A,GPIO.HIGH)
		GPIO.output(B,GPIO.HIGH)
		GPIO.output(C,GPIO.HIGH)
		GPIO.output(D,GPIO.HIGH)
		GPIO.output(G,GPIO.HIGH)
	if Num==4:
		GPIO.output(F,GPIO.HIGH)
		GPIO.output(G,GPIO.HIGH)
		GPIO.output(B,GPIO.HIGH)
		GPIO.output(C,GPIO.HIGH)
	if Num==5:
		GPIO.output(A,GPIO.HIGH)
		GPIO.output(F,GPIO.HIGH)
		GPIO.output(G,GPIO.HIGH)
		GPIO.output(C,GPIO.HIGH)
		GPIO.output(D,GPIO.HIGH)
	if Num==6:
		GPIO.output(A,GPIO.HIGH)
		GPIO.output(F,GPIO.HIGH)
		GPIO.output(G,GPIO.HIGH)
		GPIO.output(C,GPIO.HIGH)
		GPIO.output(D,GPIO.HIGH)
		GPIO.output(E,GPIO.HIGH)
	if Num==7:
		GPIO.output(A,GPIO.HIGH)
		GPIO.output(B,GPIO.HIGH)
		GPIO.output(C,GPIO.HIGH)
	if Num==8:
		GPIO.output(A,GPIO.HIGH)
		GPIO.output(B,GPIO.HIGH)
		GPIO.output(C,GPIO.HIGH)
		GPIO.output(D,GPIO.HIGH)
		GPIO.output(E,GPIO.HIGH)
		GPIO.output(F,GPIO.HIGH)
		GPIO.output(G,GPIO.HIGH)
	if Num==9:
		GPIO.output(A,GPIO.HIGH)
		GPIO.output(B,GPIO.HIGH)
		GPIO.output(C,GPIO.HIGH)
		GPIO.output(D,GPIO.HIGH)
		GPIO.output(F,GPIO.HIGH)
		GPIO.output(G,GPIO.HIGH)
		
	

		
		
def AllOff():
	GPIO.output(A,GPIO.LOW)
	GPIO.output(B,GPIO.LOW)
	GPIO.output(C,GPIO.LOW)
	GPIO.output(D,GPIO.LOW)
	GPIO.output(E,GPIO.LOW)
	GPIO.output(F,GPIO.LOW)
	GPIO.output(G,GPIO.LOW)
	
	

A=23
B=24
C=25
D=22
E=27
F=18
G=17

GPIO.setmode(GPIO.BCM)
GPIO.setup(A,GPIO.OUT)#Top Center
GPIO.setup(B,GPIO.OUT)#Top Right
GPIO.setup(C,GPIO.OUT)#Bottom Right
GPIO.setup(D,GPIO.OUT)#Bottom Center
GPIO.setup(E,GPIO.OUT)#Bottom Left
GPIO.setup(F,GPIO.OUT)#Top Left
GPIO.setup(G,GPIO.OUT)#Middle Center

#DisplayDigit(0)
#time.sleep(1)
#AllOff()
#DisplayDigit(1)
#time.sleep(1)
#AllOff()
#DisplayDigit(2)
#time.sleep(1)
#AllOff()
#DisplayDigit(3)
#time.sleep(1)
#AllOff()
#DisplayDigit(4)
#time.sleep(1)
#AllOff()
#DisplayDigit(5)
#time.sleep(1)
#AllOff()
#DisplayDigit(6)
#time.sleep(1)
#AllOff()
#DisplayDigit(7)
#time.sleep(1)
#AllOff()
#DisplayDigit(8)
#time.sleep(1)
#AllOff()
#DisplayDigit(9)
#time.sleep(1)
#AllOff()

for N in range(26):
	DisplayDigit(N)
	print("display number: ",N)
	time.sleep(.5)
	AllOff()
	time.sleep(.5)
	



GPIO.cleanup()
