import RPi.GPIO as GPIO
import time                

print("PC ON: PC-ON")   
print("Exit: Q and q")
 
while True:
    user_choice=input("Choice:")
    if user_choice=="PC-ON":        
          GPIO.setmode(GPIO.BCM)     
          GPIO.setup(25,GPIO.OUT)    
          GPIO.output(25,GPIO.LOW)
          print("3")
          time.sleep(1.0)            
          print("2")
          time.sleep(1.0)            
          print("1")
          time.sleep(1.0)            
          GPIO.cleanup() 
    elif user_choice=="q" or user_choice=="Q":      
          GPIO.cleanup()         
