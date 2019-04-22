# Python Linux系统管理与自动化运维
![cover](https://img14.360buyimg.com/n1/jfs/t8257/44/1255904949/179894/b4de49a3/59b665c9N0a622df0.jpg)
《python linux系统管理与自动化运维》——札记

# 准备阶段
* [Anaconda下载]https://www.anaconda.com/download/
```wget https://repo.anaconda.com/archive/Anaconda2-5.2.0-Linux-x86_64.sh```
```$ sudo sh ./Anaconda2-5.2.0-Linux-x86_64.sh```
* 安装anaconda-navigator方便管理
```$conda install -c anaconda anaconda-navigator```
* 启动anaconda-navigator
```$anaconda-navigator```
* 切换conda环境
```
$ source activate root #☆☆
$ conda info --envs ☆
$ conda create --name python27 
$ source activate python27
$ python --version
$ conda info --envs
$ deactivate python27    # 等价$activate root
$ conda remove --name python27 --all # 移除
$ conda env export > environment.yaml # 导出当前环境的包管理
```
* 复制一个环境,通过克隆来复制一个环境。这儿将通过克隆snowfllakes来创建一个称为flowers的副本。
```$conda create -n py36bak --clone py36```

> python提供了查询的接口在代码中可以直接打印出来看, 可以帮助查询官方模块的功能的路径。
```第一个：__file__
例如查看模块pyodbc的函数
import pyodbc
print(pyodbc.__file__)
第二个：dir(pyodbc)

第三个：help()不建议使用
help(pyodbc)
```
