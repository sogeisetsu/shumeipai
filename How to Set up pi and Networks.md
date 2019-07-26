# 如何设置树莓派和网络
*工具要求：树莓派， 一个可以设置热点的电脑， 读卡器 ，大于16G的内存卡。*

**声明：此文本中所有百度网盘链接全部来自于网络，所以当网盘链接失效时你应当通过网络来获取它，当然你也可以联系sys088519@163.com来获取它。但必须要着重说明的是
所有百度网盘链接中的文件全部通过网络获得，所以此账号（sogeisetsu）和sys088519@163.com的所有者不承担任何因此引起的法律责任，如果出现版权问题，你应当在24小时内删除相关文件**

**此方法针对的是在没有显示器（这里说的显示器为可以接受HDMI信号的显示器，故不包括一般的笔记本显示器）情况下如何设置树莓派和网络连接，
此方法有部分来自[CSDN](https://blog.csdn.net/yonglisikao/article/details/81056288)，至于其他情况下的树莓派设置方法可通过[百度](https://www.baidu.com/)或者[谷歌](https://www.google.com.hk/)进行搜索**
## 树莓派官方系统烧录教程
1. 安装Win32DiskImager-0.9.5-install.exe到电脑上。
*提取码：lh90 [这是Win32DiskImager-0.9.5-install的百度网盘连接](https://pan.baidu.com/s/1FtW77uMk7f4C5PEbbasHWA)*
2. 解压 2018-06-27-yahboom-stretch.rar，打开此软件，选择官方系统img，选择SD卡的盘符，这里不能选错，否则会被格式化，如下图配置。

*提取码：p455 [这是系统镜像的百度网盘链接](https://pan.baidu.com/s/1shIiJYm9LFkgf_xlEV9Hgw)*

![图片](https://raw.githubusercontent.com/sogeisetsu/shumeipai/master/how%20to%20set%20up%20pi.png)

3.选择Write进行烧录，等待烧录完成，拔掉SD卡，插入树莓派上电，系统会自动安装完成。

## 设置网络教程
1. 用你的电脑和读卡器读取SD卡（可以直接接着刚才的烧录步骤），在boot目录下创建一个名为ssh的文件（没有拓展名，可以先建txt再改名），在boot目录下创建一个名为wpa_supplicant.conf的文件，与上面创建“ssh”文件的方法相似。只不过，需要在文件里面写下以下代码
```
country=CN
crtl interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="testing"
    psk="testingPassword"
}
```
*“country=CN”代表Wi-Fi使用地区为中国（CN），你需要将ssid后面的“testing”中的内容替换为你前面设置的网络名称，psk后面的“testingPassword”也同样需要替换为你设置的网络密码。如果这么设置不成功可以参考[树莓派实验室](http://shumeipai.nxez.com/2017/09/13/raspberry-pi-network-configuration-before-boot.html)*

2. 接下来，就可以把SD卡插上，电源插上，开始供电，树莓派启动！同时打开电脑热点。电源和SD卡插上后，你的树莓派应该就开始默默工作了（可以观察电源旁的绿灯是否闪烁，以此判断SD卡是否在工作），如果一切顺利，经过一小段时间（大约半分钟，如果太久还是不行，建议多尝试一下），树莓派就会自动连接到前面设置的Wi-Fi，你会在移动热点的设置界面看到你的树莓派——raspberrypi，同时你还能看到它的IP地址。

3. 现在你的电脑和树莓派（PI）已经处于一个局域网内，并且也知道到了PI的IP，接下来我们将使用SSH远程登陆你的PI，但是Windows并不自带ssh，所以我们需要下载一个工具——PuTTY，你同样可以在官网免费下载。下载安装完毕后，运行并像下图这样输入你PI的IP，端口（Port）默认是22，下面还有一个保存的功能，不难使用。

![图片](https://img-blog.csdn.net/20180716111717615?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lvbmdsaXNpa2Fv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

4. 然后点击open 点击否
5. 初始账号为 pi 初始密码是 raspberry
6. 当然也可以通过windows自带的远程桌面打开树莓派的图形界面，具体方法可以百度（图形界面很重要，后面会用到）

这是图形界面的图片

![图形界面](https://img-blog.csdn.net/20180716120946306?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lvbmdsaXNpa2Fv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)


## In order to save time, a considerable amount of English content is translated using Google. I have read the English content and made corresponding changes to ensure that I can read it smoothly, but because I am not good at English, you may still be unable to read English content smoothly.So if you have any questions, you can contact me at sys088519@163.com.


# how to set up pi and networks

*Tool requirements: Raspberry Pi, a computer that can set a hotspot, a card reader, a memory card larger than 16G. *

**Declaration: All Baidu network disk links in this text are all from the network, so you should get it through the network when the network disk link fails. Of course, you can also contact sys088519@163.com to get it. But it must be emphasized
All the files in the Baidu network disk link are obtained through the network, so the owner of this account (sogeisetsu) and sys088519@163.com does not bear any legal responsibility. If there is copyright issue, you should delete the relevant within 24 hours. file**

**This method is for how to set the Raspberry Pi and network connection without the display (the display here is a monitor that can accept HDMI signals, so it does not include a general notebook display).
This method is partly from [CSDN](https://blog.csdn.net/yonglisikao/article/details/81056288) As for the other way, the Raspberry Pi setting method can be passed [Baidu](https://www.baidu.com) or [Google](https://www.google.com.hk/)**

## 树莓派官方系统 burning tutorial
1. Install Win32DiskImager-0.9.5-install.exe to your computer.
*Extraction code: lh90 [This is the Baidu network disk connection of Win32DiskImager-0.9.5-install](https://pan.baidu.com/s/1FtW77uMk7f4C5PEbbasHWA)*
2. Unzip 2018-06-27-yahboom-stretch.rar, open this software, select the official system img, select the drive letter of the SD card, you can not choose the wrong here, otherwise it will be formatted, as shown below.

*Extraction code: p455 [This is the Baidu network disk link of the system image](https://pan.baidu.com/s/1shIiJYm9LFkgf_xlEV9Hgw)*

![Image](https://raw.githubusercontent.com/sogeisetsu/shumeipai/master/how%20to%20set%20up%20pi.png)

3. Select Write to burn, wait for the burning to complete, unplug the SD card, plug in the Raspberry Pi, and the system will be installed automatically.

## Setting up a web tutorial
1. Use your computer and card reader to read the SD card (you can directly follow the previous burning step), create a file named ssh in the boot directory (no extension, you can first create txt and then rename), in Create a file named wpa_supplicant.conf in the boot directory, similar to the method for creating the "ssh" file above. Just need to write the following code in the file
```
Country=CN
Crtl interface=DIR=/var/run/wpa_supplicant GROUP=netdev
Update_config=1

Network={
Ssid="testing"
Psk="testingPassword"
}
```
* "country=CN" means that the Wi-Fi usage area is China (CN). You need to replace the contents of "testing" after ssid with the network name you set earlier. The "testingPassword" after psk also needs to be replaced with The network password you set. If this setting is not successful, please refer to [Raspberry Pi Lab](http://shumeipai.nxez.com/2017/09/13/raspberry-pi-network-configuration-before-boot.html)*

2. Next, you can plug in the SD card, plug in the power, start the power supply, and start the Raspberry Pi! Also open the computer hotspot. After the power and SD card are plugged in, your Raspberry Pi should start working silently (you can observe whether the green light next to the power supply is blinking to determine if the SD card is working). If all goes well, after a short period of time (about half Minutes, if it is too long or not, it is recommended to try more), the Raspberry Pi will automatically connect to the Wi-Fi set in the front, you will see your Raspberry Pi in the mobile hotspot settings interface - raspberrypi, while you You can also see its IP address.

3. Now that your computer and Raspberry Pi (PI) are already in a LAN, and you know the IP of PI, we will use SSH to remotely log in to your PI, but Windows does not bring ssh, so we need Download a tool - PuTTY, you can also download it for free on the official website. After the download is complete, run and enter your PI's IP as shown below. The port (Port) defaults to 22, and there is a saved function below, which is not difficult to use.

![Image](https://img-blog.csdn.net/20180716111717615?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lvbmdsaXNpa2Fv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

4. Then click open click no
5. The initial account is pi. The initial password is raspberry.
6. Of course, you can also open the Raspberry Pi graphical interface through the remote desktop that comes with Windows. The specific method can be Baidu (the graphical interface is very important, it will be used later)

This is a picture of the graphical interface

![Graphic interface](https://img-blog.csdn.net/20180716120946306?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lvbmdsaXNpa2Fv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
