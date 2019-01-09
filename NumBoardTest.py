import RPi.GPIO as GPIO
import time



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

GPIO.output(A,GPIO.HIGH)
print("TC")
time.sleep(1)
GPIO.output(A,GPIO.LOW)
time.sleep(1)
GPIO.output(B,GPIO.HIGH)
print("TR")
time.sleep(1)
GPIO.output(B,GPIO.LOW)
time.sleep(1)
GPIO.output(C,GPIO.HIGH)
print("BR")
time.sleep(1)
GPIO.output(C,GPIO.LOW)
time.sleep(1)
GPIO.output(D,GPIO.HIGH)
print("BC")
time.sleep(1)
GPIO.output(D,GPIO.LOW)
time.sleep(1)
GPIO.output(E,GPIO.HIGH)
print("BL")
time.sleep(1)
GPIO.output(E,GPIO.LOW)
time.sleep(1)
GPIO.output(F,GPIO.HIGH)
print("TL")
time.sleep(1)
GPIO.output(F,GPIO.LOW)
time.sleep(1)
GPIO.output(G,GPIO.HIGH)
print("M")
time.sleep(1)
GPIO.output(G,GPIO.LOW)




GPIO.cleanup()
