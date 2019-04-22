# 第二章Python的生态工具

## 2.1 Python内置小工具

### 2.1.1 启动一个http下载服务器：

py2.x
```$ python -m SimpleHTTPServer```

或py3.x中

```$ python -m http.server```

### 2.2 pip高级用法
* install
* download
* uninstall
* freeze
* list
* show查找安装包
* check检查安装包的依赖是否完整
* search
* wheel打包软件到wheel
* hash
* completion生成命令补全
* help


freeze导出系统已安装的安装包列表到requirements
```$ pip freeze > requirements.txt```

install从requirements文件安装
```$ pip install -r requirements.txt```

completion 使用pip命令补全
```$ pip completion --bash >>~/.profile```

#### 改变pip镜像源

创建~/.pip/pip.conf
```
cat pip.conf
[global]
index-url=https://pypi.douban.com/simple
```

下载到本地
```$ pip install --download='pwd' -r requirements.txt```

本地安装
```$ pip install --no-index -f file://'pwd' -r requirements.txt```
        
如：
```$ pip install --download='pwd' flask```



### 2.3 Python编辑器

vim常用命令总结
![vim常用命令总结](http://img.blog.csdn.net/20160712110935064?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

#### 代码补全插件snipmate(已安装)
#### 语法检查插件Syntastic(已安装)
#### jedi-vim(需要安装)
```$ pip install jedi```


### 2.4 Python编程辅助工具
#### 2.4.2 使用IPython交互式编程
```$ sudo apt-get install ipython```

可以使用？通配符获取帮助信息



#### 2.4.3 使用jupyter
```$ pip install jupyter```

        如果Linux没有图形界面，可以设置--no-browser和设置--ip=0.0.0.0进行外部访问，如果不指定--ip参数，默认ip是localhost(本地)
```$ jupyter notebook --no-browser --ip=0.0.0.0```

在外部机器中替换0.0.0.0为Linux服务器ip即可。

jupyter Notebook各种使用方法记录·持续更新![持续更新](https://blog.csdn.net/tina_ttl/article/details/51031113)
使用%matplotlib inline预声明画图
```%matplotlib inline```



### 2.5 python调试器

标准库的pdb和开源的ipdb,部分pdb调试命令:
* break
* continue
* next
* step
* where
* enable
* disable
* pp/p
* list
* up
* down
* restart
* args
* clear
* return







### 2.7python工作环境的管理使用pyenv和virtualenv管理
#### pyenv管理
```$ git clone https://github.com/yyuu/pyenv.git ~/.pyenv ```

配置环境变量:
```
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile  
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile  
$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile  //添加pyenv初始化到你的shell
```

重新启动你的shell使更改生效:
```
$ exec $SHELL  
$ source ~/.bash_profile
```

安装版本:
```$ pyenv install 3.6.0/2.7.13```

切换版本:
```$ pyenv global 3.6.0/2.7.13```

删除版本:
```$ pyenv uninstall 3.6.0/2.7.13```


#### pyenv+virtualenv插件管理
```$ git clone git://github.com/yyuu/pyenv.git ~/.pyenv/plugins/pyenv-virtualenv```

配置环境
```$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile```

重启生效
```
$ exec $SHELL
$ source ~/.bash_profile
```
--------------------

以上2.7节内容因为有Anaconda Navigator 更好替换之
