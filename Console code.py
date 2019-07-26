# coding=UTF-8
#!/usr/bin/python

import RPi.GPIO as GPIO
import time
for i in range (10):
    channel = 16  # 引脚号16
    data = []  # 温湿度值
    j = 0
    # 计数器
    a=20
    GPIO.setmode(GPIO.BCM)  # 以BCM编码格式

    time.sleep(1)  # 时延一秒

    GPIO.setup(channel, GPIO.OUT)

    GPIO.output(channel, GPIO.LOW)
    time.sleep(0.02)  # 给信号提示传感器开始工作
    GPIO.output(channel, GPIO.HIGH)

    GPIO.setup(channel, GPIO.IN)

    while GPIO.input(channel) == GPIO.LOW:
        continue

    while GPIO.input(channel) == GPIO.HIGH:
        continue

    while j < 40:
        k = 0
        while GPIO.input(channel) == GPIO.LOW:
            continue

        while GPIO.input(channel) == GPIO.HIGH:
            k += 1
            if k > 100:
                break

        if k < 8:
            data.append(0)
        else:
            data.append(1)

        j += 1

    print "开始工作."
   # print  data  # 输出初始数据高低电平

    humidity_bit = data[0:8]  # 分组
    humidity_point_bit = data[8:16]
    temperature_bit = data[16:24]
    temperature_point_bit = data[24:32]
    check_bit = data[32:40]

    humidity = 0
    humidity_point = 0
    temperature = 0
    temperature_point = 0
    check = 0

    for i in range(8):
        humidity += humidity_bit[i] * 2 ** (7 - i)  # 转换成十进制数据
        humidity_point += humidity_point_bit[i] * 2 ** (7 - i)
        temperature += temperature_bit[i] * 2 ** (7 - i)
        temperature_point += temperature_point_bit[i] * 2 ** (7 - i)
        check += check_bit[i] * 2 ** (7 - i)

    tmp = humidity + humidity_point + temperature + temperature_point  # 十进制的数据相加

    if check == tmp:  # 数据校验，相等则输出
        print "temperature : ", temperature, ", humidity : ", humidity
        c="温度"+str(temperature)+"."+"/"+"湿度"+str(humidity)
        GPIO.setup(21, GPIO.IN)
        if GPIO.input(channel) == GPIO.LOW:
            print "土壤检测结果：潮湿"
            c=c+"\n"+"土壤潮湿"+"\n"+"推荐不要浇水，具体以机器操作为准"
        else:
            print "土壤检测结果：干燥"
            c=c+"\n"+"土壤干燥"+"\n"+"推荐浇水，具体以机器操作为准"
        f=open("123.txt","w+")
        f.write(c)
        f.close
        if temperature >= 20:
            print"jiaoshui"
            GPIO.setup(25, GPIO.OUT)
            GPIO.output(25, GPIO.LOW)
            print("3")
            time.sleep(1.0)
            print("2")
            time.sleep(1.0)
            print("1")
            time.sleep(1.0)
            GPIO.cleanup()
            GPIO.setmode(GPIO.BCM)  # 以BCM编码格式

            time.sleep(1)  # 时延一秒

            GPIO.setup(channel, GPIO.OUT)

            GPIO.output(channel, GPIO.LOW)
    else:  # 错误输出错误信息，和校验数据
        print "出现错误，输出校验结果"
        print "temperature : ", temperature, ", humidity : ", humidity, " check : ", check, " tmp : ", tmp
    time.sleep(2)

    GPIO.cleanup()  # 重置针脚
