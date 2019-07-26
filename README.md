# shumeipai
0基础实现树莓派云灌溉系统
# <center>树莓派云灌溉系统的实现</center>
## <center>目录</center>
## 树莓派相关配置
 - 树莓派简介
    - [the introduction of pi .md](https://github.com/sogeisetsu/shumeipai/blob/master/the%20introduction%20of%20pi.md)
 - 树莓派安装系统并网络连接
    - [How to Set up pi and Networks.md](https://github.com/sogeisetsu/shumeipai/blob/master/How%20to%20Set%20up%20pi%20and%20Networks.md)
 - 树莓派摄像头的启用
    - [Preparation for the development environment before using the camera](https://github.com/sogeisetsu/shumeipai/blob/master/%E6%A0%91%E8%8E%93%E6%B4%BE%E6%91%84%E5%83%8F%E5%A4%B4%E5%BC%80%E5%8F%91%E5%89%8D%E7%9A%84%E7%8E%AF%E5%A2%83%E5%87%86%E5%A4%87.docx)
    - [Camera tutorial](https://github.com/sogeisetsu/shumeipai/blob/master/%E6%A0%91%E8%8E%93%E6%B4%BE%E5%AE%98%E6%96%B9%E6%91%84%E5%83%8F%E5%A4%B4%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B.docx)
 - 树莓派相关传感器的使用
    - [Some notes about the sensor.md](https://github.com/sogeisetsu/shumeipai/blob/master/Some%20notes%20about%20the%20sensor.md)
    - [Code to control soil moisture sensor](https://github.com/sogeisetsu/shumeipai/blob/master/%E5%9C%9F%E5%A3%A4.py)
    - [Control the code of dht11](https://github.com/sogeisetsu/shumeipai/blob/master/dh11.py)
    - [Control relay code](https://github.com/sogeisetsu/shumeipai/blob/master/%E7%BB%A7%E7%94%B5%E5%99%A8.py)
 - 树莓派控制传感器的代码
    - [Console code.py](https://github.com/sogeisetsu/shumeipai/blob/master/Console%20code.py)
 - 树莓派端的内网穿透
    - [参考这里设置](https://www.jianshu.com/p/a921e85280ed)
 - scp corntab nohup 介绍
    - scp 是负责传文件的命令
    - crontab是负责控制传文件时间的命令
    - nohup 是负责后台运行的命令
    - 这三个命令可以通过网络来学习
    - scp is the command to transfer files
     #### crontab is the command responsible for controlling the time of the file transfer
     #### nohup is the command that is responsible for running in the background
     #### These three commands can be learned through the network
 - shell 脚本
    - 此脚本目的是定时将数据上传到服务器
    - [在运行此脚本前应解决scp无密码传输的问题](https://blog.csdn.net/u012454773/article/details/72779439)
    - 后台运行的命令为  nohup sh /home/pi/tran/a.sh >> /home/pi/tran/d.txt 2>&1 &
    - The purpose of this script is to periodically upload data to the server.
    - [Scp should be resolved without password transfer before running this script] (https://blog.csdn.net/u012454773/article/details/72779439)
    - The command to run in the background is nohup sh /home/pi/tran/a.sh >> /home/pi/tran/d.txt 2>&1 &
## 云服务器相关配置

 - 服务器购买及选择
 - 端口的开关
 - 网站配置
 - frp 配置树莓派公网ip
 - 前端网页代码
 - 接受树莓派传来的文件
 - 发送文件
