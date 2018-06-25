#第1部分:apt准备
sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler
sudo apt-get install --no-install-recommends libboost-all-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install libhdf5-serial-dev

sudo apt-get install python-dev

sudo apt-get install libgflags-dev libgoogle-glog-dev liblmdb-dev




#第2部分:caffe git 下载
		git clone https://github.com/BVLC/caffe.git
	#下载完成之后,进入CAFFE文件夹, 进入里面的PYTHON文件夹,然后输入
		apt-get install python-pip  
		for req in $(cat requirements.txt); do pip install $req; done  

#第3部分:编译Caffe
	#到Caffe文件夹中，拷贝一份Makefile.config.example并重命名成Makefile.config，修改该配置文件：
		cp Makefile.config.example Makefile.config  
	#使用文本编辑器打开Makefile.config，因为这里没有配置GPU，所以去掉CPU_ONLY := 1前面的注释；
	#由于Ubuntu16.04文件结构的变化，#Whatever else you find you need goes here.处要改成下面这样
		# Whatever else you find you need goes here.  
		INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial  
		LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib /usr/lib/x86_64-linux-gnu/hdf5/serial

	#设置到这里开始编译，make pycaffe，结果报错，错误和numpy相关，重新打开Makefile.config目录，又查找了一下numpy的安装目录，发现对应不上，需要重新设置，需要把原本如下的内容：
		# NOTE: this is required only if you will compile the python interface.  
		# We need to be able to find Python.h and numpy/arrayobject.h.  
		PYTHON_INCLUDE := /usr/include/python2.7 \  
				/usr/lib/python2.7/dist-packages/numpy/core/include 
	#更改为：
		# NOTE: this is required only if you will compile the python interface.  
		# We need to be able to find Python.h and numpy/arrayobject.h.  
		PYTHON_INCLUDE := /usr/include/python2.7 \  
				/usr/local/lib/python2.7/dist-packages/numpy/core/include  

	#之后就是编译：
		make pycaffe  
		make all  
		make test  
		make runtest  

	#make默认单核运算，如果想加快速度，我这里是4核，可以在每条命令后面加上-j4，如果有报错，建议最好make clean重新开始。
	#如果所有测试都通过，则说明安装好了。
	
	
#第4部分:测试
	#测试Caffe的Python接口，切换到caffe/python文件目录下，记录下来当前路径，输入以下命令：
		export PYTHONPATH=/path/to/caffe/python:$PYTHONPATH  		
		
	#进入python环境，输入：
		import caffe  

	#如果没有报错，证明安装成功。
	#上面的方法，一旦关闭终端或者打开新终端则失效，如果放到配置文件中，可以永久有效果，命令操作如下：
	    #A.把环境变量路径放到 ~/.bashrc文件中  
		sudo echo export PYTHONPATH="~/caffe/python" >> ~/.bashrc  
		#B.使环境变量生效  
		source ~/.bashrc