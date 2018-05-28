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
wget https://launchpad.net/ubuntu-kylin-software-center/1.3/1.3.14/+download/ubuntu-kylin-software-center_1.3.14-0%7E349%7Eubuntu16.04.1_all.deb
wget https://download.teamviewer.com/download/linux/teamviewer-host_amd64.deb
wget https://repo.anaconda.com/archive/Anaconda2-5.1.0-Linux-x86_64.sh

#necessary apt：
	sudo apt-get install build-essential //有可能安装 build-essential 后gdb就已经安装过了  
	sudo apt-get install gdb 
	sudo apt install python-pip
	sudo apt-get install git
	sudo apt-get install teamviewer-host
	#openssh-server
		sudo apt-get install openssh-server
		#是否启动：
		#ps -e |grep ssh

	
	
	
	#pycharm 
		sudo apt-get install pycharm-community
	
	
	#Anconda 推荐2.7
		#https://www.anaconda.com/download/#linux
		wget https://repo.anaconda.com/archive/Anaconda2-5.1.0-Linux-x86_64.sh
	
	#codeblocks
		sudo add-apt-repository ppa:damien-moore/codeblocks-stable  
		sudo apt-get update  
		sudo apt-get install codeblocks  
		#将会同时安装下列软件：  
		#codeblocks-common libcodeblocks0 libwxbase2.8-0 libwxgtk2.8-0  
		#建议安装：  
		#libwxgtk2.8-dev | libwxgtk3.0-dev wx-common codeblocks-contrib   
		sudo apt-get install codeblocks-dbg  
		sudo apt-get install codeblocks-contrib  
		#将会同时安装下列软件：  
		#cccc codeblocks-contrib-common codeblocks-libwxcontrib0 cppcheck cscope  
		#gamin libgamin0 libtinyxml2-2v5 libwxsmithlib0 python-chardet  
		#python-pkg-resources python-pygments valgrind  
		#建议安装：  
		#cscope-el python-setuptools ttf-bitstream-vera valgrind-dbg kcachegrind  
		#alleyoop valkyrie   
		sudo apt-get install valgrind-dbg  
		#Valgrind 用来探测内存泄露 
		sudo apt-get install libwxbase3.0  
		sudo apt-get install libwxbase3.0-dev  
		sudo apt-get install libwxgtk3.0-0  
		sudo apt-get install libwxgtk3.0-dev  
		sudo apt-get install wx-common  
		sudo apt-get install wx3.0-headers  
		sudo apt-get install wx3.0-i18n
	
	
	
	


