# ubuntuguide
ubuntuguide

# For disk install
cheak Secure Boot:OFF
UEFI should be off

500GB
主分区：
efi分区bootloader>=64MB
etx4>=10G
逻辑分区:
/boot     >=1GB
/home   >=other


# For initial apt source
# sudo gedit /etc/apt/sources.list  

#sjtu(上海交通大学更新服务器)
deb http://ftp.sjtu.edu.cn/ubuntu/ lucid main multiverse restricted universe
deb http://ftp.sjtu.edu.cn/ubuntu/ lucid-backports main multiverse restricted universe
deb http://ftp.sjtu.edu.cn/ubuntu/ lucid-proposed main multiverse restricted universe
deb http://ftp.sjtu.edu.cn/ubuntu/ lucid-security main multiverse restricted universe
deb http://ftp.sjtu.edu.cn/ubuntu/ lucid-updates main multiverse restricted universe
deb-src http://ftp.sjtu.edu.cn/ubuntu/ lucid main multiverse restricted universe
deb-src http://ftp.sjtu.edu.cn/ubuntu/ lucid-backports main multiverse restricted universe
deb-src http://ftp.sjtu.edu.cn/ubuntu/ lucid-proposed main multiverse restricted universe
deb-src http://ftp.sjtu.edu.cn/ubuntu/ lucid-security main multiverse restricted universe
deb-src http://ftp.sjtu.edu.cn/ubuntu/ lucid-updates main multiverse restricted universe  


deb-src http://mirror.neu.edu.cn/ubuntu/ xenial main restricted #Added by software-properties
deb http://mirror.neu.edu.cn/ubuntu/ xenial main restricted
deb-src http://mirror.neu.edu.cn/ubuntu/ xenial restricted multiverse universe #Added by software-properties
deb http://mirror.neu.edu.cn/ubuntu/ xenial-updates main restricted
deb-src http://mirror.neu.edu.cn/ubuntu/ xenial-updates main restricted multiverse universe #Added by software-properties
deb http://mirror.neu.edu.cn/ubuntu/ xenial universe
deb http://mirror.neu.edu.cn/ubuntu/ xenial-updates universe
deb http://mirror.neu.edu.cn/ubuntu/ xenial multiverse
deb http://mirror.neu.edu.cn/ubuntu/ xenial-updates multiverse
deb http://mirror.neu.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
deb-src http://mirror.neu.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse #Added by software-properties
deb http://archive.canonical.com/ubuntu xenial partner
deb-src http://archive.canonical.com/ubuntu xenial partner
deb http://mirror.neu.edu.cn/ubuntu/ xenial-security main restricted
deb-src http://mirror.neu.edu.cn/ubuntu/ xenial-security main restricted multiverse universe #Added by software-properties
deb http://mirror.neu.edu.cn/ubuntu/ xenial-security universe
deb http://mirror.neu.edu.cn/ubuntu/ xenial-security multiverse

#then terminal input 
sudo apt-get update 


#necessary apt：
	#openssh-server
		sudo apt-get install openssh-server
		#是否启动：
		#ps -e |grep ssh
		
	#teamviewer-host
	sudo apt-get install teamviewer-host
	
	
	#pycharm 
	sudo apt-get install pycharm-community
	
	
	#Anconda
	#https://www.anaconda.com/download/#linux
	
	
	
	
	
	


