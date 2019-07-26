#!/usr/bin/python
# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO
import time

channel = 21 #管脚40，参阅树莓派引脚图，物理引脚40对应的BCM编码为21

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

while True:
        if GPIO.input(channel) == GPIO.LOW:
                print "土壤检测结果：潮湿"
        else:
                print "土壤检测结果：干燥"
        time.sleep(1)
