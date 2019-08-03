# 树莓派学习
*作者：苏月晟*

***


***该文档部分引用自网络，引用部分已经注明***


**0基础实现树莓派云灌溉系统**
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
    - 服务器我购买的是阿里云的轻量级服务器，现在可以使用学生优惠
    - 服务器需要搭一个网站的框架，推荐用flask 我用的是宝塔
    - 使用宝塔只需要看官方教程就够了
    
    *Server I purchased Alibaba Cloud's lightweight server, now I can use student discounts
The server needs to build a website framework, recommend using flask. I use a pagoda.
It is enough to use the pagoda only to see the official tutorial.*
 - 端口的开关
    - 需要开一些端口
    - 我开的是这些端口
    - ![图片](https://img-blog.csdnimg.cn/20190727001946742.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3N1eXVlcw==,size_16,color_FFFFFF,t_70)
 - 网站配置
    - 宝塔页面上配置上数据库，ftp，网站。其实刚开始设置宝塔的时候会有提示，按照提示设置lnmp就好了
     **Configure the database, ftp, website on the Pagoda page. In fact, when you first set up the pagoda, there will be a prompt, follow the prompts to set lnmp just fine**
 - frp 配置树莓派公网ip
    - 这个参考前面内网穿透的教程
 - 前端网页代码
    - [前端](https://github.com/sogeisetsu/shumeipai/blob/master/index%20(2).html)
    - [Front end code](https://github.com/sogeisetsu/shumeipai/blob/master/index%20(2).html)
 - 接受树莓派传来的文件
    - 在前端代码里有说明
 - 发送文件
    - 在前端代码里有说明
### 更新

- 设置域名
   1. 域名可以从阿里云，腾讯云等购买
   2. 在域名服务商那里可以设置解析，TTL建议3600，***实验发现，600s的经常性304***
   3. 然后从宝塔面板绑定域名
   4. 这样就可以通过域名访问了
   5. 我在这个项目中的域名是[www.qkgoride.club](http://www.qkgoride.club/)*截至2019/8/3 17：23此域名仍无法访问，原因是刚刚修改过相关内容，需要3600s后才可正常访问*
