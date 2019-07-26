#!/bin/sh
now=date'+%Y-%m-%d %H:%M:%S'
folder=/root/tran
cd $floder
while true
do
	now=date'+%Y-%m-%d %H:%M:%S'
	echo -e $now'start'>>log.txt
	scp 123.txt root@xxx.xx.xxx.xxx:/www/wwwroot/http/1.txt
	sleep 5
done
