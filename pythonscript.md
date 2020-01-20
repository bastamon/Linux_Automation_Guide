《python linux系统管理与自动化运维》
![cover]()

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
$ conda env create -f environment.yaml # 这会创建一个新环境，而且它具有同样的在 environment.yaml 中列出的库。
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

---------------------------------------------
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

# 第3章 打造命令工具
### 3.1.1 使用sys.argv获取命令行参数
```
from __future__ import print_function
import os
import sys

def main():
    sys.argv.append("")
   print(sys.argv[0])
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        raise SystemExit(filename + 'dose not exists')
    elif not os.access(filename, os.R_OK):
        raise SystemExit(filename + 'is not accessible')
    else:
        print(filename + ' is accessible')        
      
        
if __name__ == '__main__':
    main()
```


可以得出语法:
```python 参数0(sys.argv[0]) 参数1(sys.argv[1]) …… 参数n(sys.argv[n]) ```  

---------------
补充：

在python2.x中 ，异常是这样的处理的，异常基类后面加一个逗号“ ，”  然后跟着异常类型:
```
import traceback
try:
  1/0
except Exception , err:
  print err
```

而在python3.x中，异常是这样处理的，基类通过关键 词"as" 连接异常类型:
```
import traceback
try:
  1/0
except Exception as err:
  print(err)
```
    
### 3.1.2使用sys.stdin和fileinput读取标准输入
>文件“read_stdin.py”：
```
from __future__ import print_function
import sys

for line in sys.stdin:
    print (line,end="")
```

就可以像shell一样，在终端输入，注意第二行的实现方式：
```
$ cat /etc/passwd | python read_stdin.py    //  cat读管道方式交给read_stdin.py
$ python read_stdin.py < /etc/passwd    //read_stdin.py实现读地址
$ python read_stdin.py -    //read_stdin.py实现读标准键盘输入
```

------------------------------------
调用read函数读取标准输入中的所有内容调用readlines函数将标准输入的内容读取到一个列表中（不太懂）：
```
from __future__ import print_function
import sys

def get_content():
    return sys.stdin.readlines()

print(get_content())
```

-------------------------------------


fileinput可以依次读取命令行参数中给出的多个文件，也就是说fileinput会遍历sys.argv[1:]列表，fileinput遍历文件内容:
```
#!/usr/bin/python
from __future__ import print_function
import fileinput
for line in fileinput.input():
    meta= [fileinput.filename(),fileinput.fileno(),fileinput.filelineno(),fileinput.isfirstline(),fileinput.isstdin()]
    print(*meta,end="")
    print(line,end="")
```

使用shell运行：
```
$ cat /etc/passwd | python read_from_fileinput.py
$ python read_from_fileinput.py < /etc/passwd
$ python read_from_fileinput.py /etc/passwd
$ python read_from_fileinput.py /etc/passwd /etc/hosts
```
### 3.1.3 使用SystemExit异常打印错误信息
>文件“tes_stdout_stderr.py”
```
import sys

sys.stdout.write('hello') 
sys.stderr.write('world') 
```

调用：
```
$ python tes_stdout_stderr.py >/dev/null
$ python tes_stdout_stderr.py 2>/dev/null
```
>文件：test_system_exit.py
```
import sys

sys.stderr.write('error message')
sys.exit(1)
```

shell输入：
```
python test_system_exit.py
```

### 3.1.4使用getpass获取密码

实现隐藏标准输入
```
from __future__ import print_function
import getpass

user=getpass.getuser()
passwd=getpass.getpass('your passwd:')
print(user,passwd)
```

## 3.2 使用ConfigParse解析配置文件☆☆☆(dependancy python 2.7~2.8)

假设已安装MySql，那就有/etc/mysql/my.cnf,pip的配置文件位于~/.pip/pip.conf中。还有*.ini等<font color=#FF1493>配置文件</font>

ConfigParse中判断配置项相关的方法有：
* sections:返回一个包含所有章节的列表
* has_section:判断章节是否存在
* items:以元组的形式返回所有选项
* options:返回一个包含章节下所有选项的列表
* has_option:判断某个选项是否存在
* get、getboolean、getinit、getfloat：获取选项的值
```
import ConfigParser

cf = ConfigParser.ConfigParser(allow_no_value = True)
cf.read('my.cnf')   //创建mysql的副本路径
## ['my.cnf']
cf.sections()
## ['client','mysqld']
cf.has_section('client')
## True
cf.options('client')
## ['port','user','password','host']
cf.has_option('client','user')
## True
cf.get('client','host')
## '127.0.0.1'
cf.getint('client','port')
## 3306
```

ConfigParse中修改配置项相关的方法有：
* remove_section:删除一个章节
* add_section:添加一个章节
* remote_option:删除一个选项
* set:添加一个选项
* write：将ConfigParse对象中的数据保存到文件中
```
# -*- coding: utf-8 -*-
import os
import ConfigParser


cf = ConfigParser.ConfigParser(allow_no_value = True)
cf.read('my.cnf')   ## 读取mysql的副本路径缓存进cf
## ['my.cnf']
cf.sections()
## ['client','mysqld']
cf.has_section('client')
## True
cf.options('client')
## ['port','user','password','host']
cf.has_option('client','user')
## True
cf.get('client','host')
## '127.0.0.1'
cf.getint('client','port')
## 3306

os.system("pause")
print("write")
cf.remove_section('client')
## 
cf.add_section('mysql')
## 增加mysql章节
cf.set('mysql','host','127.0.0.1')
## 在mysql章节下增加hos t = 127.0.0.1
cf.set('mysql','port','3306')
## 在mysql章节下增加port = 3306
cf.write(open('my_copy.cnf','w'))
## 将cf写到my_copy.cnf副本
```


## 3.3使用argparse解析命令行参数

argparse是标准库中用来解析命令行参数的模块；argparse能根据程序中的定义从<font color=#FF1493>sys.argv</font>中解析出这些参数，并自动生成帮助和使用信息

### 3.3.1 ArgumentParse解析器
```
# 使用argparse解析命令行参数前，必须先创建一个解析器
import argparse
parser = argparse.ArgumentParser() 
```
ArgumentParser类的初始化函数有多个参数，其中比较常用的是description,用以程序描述信息。

为应用程序添加参数选项需要用ArgumentParser对象的add_argument方法

```add_argument(name or flags...[,action][,nargs][,const][,default][,type][,choices][,required][,help][,metavar][,dest])```

* name/flags:参数的名字
* action:遇到参数时的动作{store,store_const,store_ture/store_false,append,append_const,version }
* nargs:参数的个数,可以是巨头的数字,或者是“+”号与“*”号。其中,“*”号表示0或多个参数,“+”表示1或多个参数
* const action和nargs:
* default:
* type:参数的类型
* choices:参数允许的值
* required:可选参数是否可以省略
* help:参数的帮助信息
* metavar:在usage说明中的参数名称
* dest:解析后的参数名称

解析参数用ArgumentParser对象的parse_args方法，该方法返回一个Namespace对象。获取对象后，参数值通过属性的方式进行访问


```
from __future__ import print_function
import argparse


def _argparse():
    parser = argparse.ArgumentParser(description="This is description")  #创建ArgumentParser解析器
    #以add_argument函数添加选项，通过parser.server 获取 --host选项的值
    parser.add_argument('--host', action = 'store', dest = 'server', default = "localhost", help= 'connect to host')
    # 通过parse.boolean_switch 获取-t选项的值
    parser.add_argument('-t',action ='store_true', default = False, dest = 'boolean_switch', help = 'Set a switch to true')
    return parser.parse_args()


def main():
    parser= _argparse()
    print(parser)
    print('host = ', parser.server)
    print('boolean_switch=', parser.boolean_switch)


if __name__ =='__main__':
    main()
```
### 3.3.2模仿MySQL客户端的命令参数

```
from __future__ import print_function
import argparse


def _argparse():
    parser = argparse.ArgumentParser(description='A python-mysql client')
    parser.add_argument('--host',action='store',dest='host',required=True,help='connect to host')   #parser.host
    parser.add_argument('-u','--user',action='store',dest='user',required=True,help='user for login')   #parser.user
    parser.add_argument('-p','--password',action='store',dest='password',required=True,help='passwoed to use when connecting to server')    #parser.password
    parser.add_argument('-P','--Port',action='store',dest='port',default=3306,type=int,required=True,help='port number to use for connection or 3306 for default')    #parser.port
    parser.add_argument('-v','--version',action='version',version='%(prog)s 0.1')#parser.version
    return parser.parse_args()#返回add_argument参数的dest中解析出来的值


def main():
    parser = _argparse()
    conn_args = dict(host=parser.host,user=parser.user,password=parser.password,port=parser.port)
    print(conn_args)


if __name__=='__main__':
    main()
```
>关联3.5节click、prompt_toolkit

## 3.4使用logging记录日志
```import logging```

### 3.4.1 日志的作用
>诊断:记录与应用程序操作相关的日志

>审计:为商业分析而记录的日志

### 3.4.2 python 中的logging模块
<center>表3-1 logging 模块日志级别</center>
<table>
    <tr>
        <th width=15%, bgcolor=yellow >日志级别</th>
        <th width=15%, bgcolor=yellow>权重</th>
        <th width=50%, bgcolor=yellow>含义</th>
    </tr>
    <tr>
        <td>CRITICAL</td>    
        <td>50</td>
        <td>严重错误，软件不能继续运行。</td>
    </tr>
    <tr>
        <td>ERROR</td>
        <td>40</td>
        <td>发生严重错误，需要马上处理</td>
    </tr>
    <tr>
        <td>WARNING</td>
        <td>30</td>
        <td>应用程序可以容忍这些信息,但是此时应用程序还是正常运行的，不过它应该被检查及修复，否则将在不久的将来发生问题</td>
    </tr>
    <tr>
        <td>INFO</td>
        <td>20</td>
        <td>证明事情按预期工作，突出强调应用程序的运行过程</td>
    </tr>
    <tr>
        <td>DEBUG</td>
        <td>10</td>
        <td>详细信息，只有开发人员调试程序时才需要关注的事情</td>
    </tr>
</table>

### 3.4.3配置日至格式 

在使用日至之前，一些简单的配置
```
#!/usr/local/bin/python
# -*- coding:utf-8 -*-
import logging

logging.basicConfig(filename='app.log',level=logging.INFO)

logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')
```
上述程序会在当前目录产生一个app.log文件。该文件中存在INFO及INFO以上级别的日志记录。
它通过basicConfig方法对日志进行了简单的配置，也可以进行更加复杂的日至配置;logging模块中的几个概念，
> Logger:日志记录器,是应用程序中能直接使用的接口
> Handler:日至处理器,用以表明将日志保存到什么地方以及保存多久
> Fornatter:格式化,，用以配置日志的输出格式

一个日志处理器使用一个日志处理器，一个日志处理器使用一个日志格式化。

```
#!/usr/local/bin/python
#-*- coding:utf-8 -*-
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s',
    filename="app.log"
)
logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')
```

一个典型的日志配置文件:
```
[loggers]
keys=root//一个名为root的logger

[handlers]
keys=logfile//一个名为logfile的handler

[formatters]
keys=generic//一个名为generic的formatter

[logger_root]
handlers=logfile

[handler_logfile]
class=handlers.TimedRotatingFileHandler
args=('app.log','midnight',1,10)
level=DEBUG
formatter=generic

[formatter_generic]
format=%(asctime)s%(levelname)-5.5s [%(name)s:%(lineno)s]%(message)s
```

# 第4章 文本处理☆☆☆☆

## 4.1 字符串常量
### 4.1.1 定义字符串
python 不需要区分字符和字符串

遇到以下情况：
```
intro = "He's a teacher" 
statement= 'John said to me:"Can you do me a favour tonight"'
```

可以使用转义字符时

```
intro = 'He\'s a teacher'
statement = "John said to me:\"Can you do me a favour tonight\"" 
```

在python中，可以使用山歌硬好来定义字符串，如：
```
message = '''Type "copyright", "credits" or "license" for more information. Details about 'object',use 'object??' for extra details.''' 
```


### 4.1.2 字符串是不可变的有序集合
```
s = "hello"
s[0] = 'H'
```
会引起Traceback, TypeError,
> 由于Python字符串不可变的特性，对字符串进行操作只会得到一个新的字符串:

### 4.1.3 字符串函数
* 1.通用操作
```
s = "Hello, world"
"Hello" in s
```
* 2.与大小写相关的方法
```
upper#转换
lower#
isupper#判断
islower#
swapcase#将所有大写换小写，所有小写换大写
capitalize#大写首字母
istitle#判断字符串是不是标题
```
* 3.判断类方法
```
isalpha#非空且全字母
isalnum#非空且包含数字和字母
isspace#非空且包含空格、制表符、换行符
isdecimal#只包含数字字符
```
* 4.字符串方法startswith和endswith
```
s="lai ming xing"
s.startswith('lai')#True
s.startswith('lai m')#True
s.startswith('Not')#False
s.endswith('xing')#True
```
* 5.查找类函数
```
find#查找子串出现在字符串中的位置,失败则返回-1
index#同find,失败则返回ValueError
rfind#从后向前
rindex#从后向前
```
```
s = "Return the lowest index in S where substring sub is found"
s.find('in') # 18
s.find('in',19) # 24,从下标19开始找
'in' in s # True
```

* 6.字符串操作方式
字符串的join函数用以连接字符串列表，组成一个新的、更大的字符串。若仅仅需要将几个字符串连接起来，并且无需插入任何额外的字符，则可以使用空字符串调用join方法

```
print("".join(['a','b','c']))   #'abc'
print(",".join(['a','b','c']))   #'a,b,c'
print("###".join(['a','b','c']))   #'a###b###c'

```
>split()正好是和join()相反的作用


>python可以用collections.Counter保存资源热度Counter。Counter是dict的子类，比字典更加好用
### 4.1.4案例:使用Python分析Apache的访问日志
```
c=Counter('abcba')  #{'a':2,'b':2,'c':1}可用于关键字热度计数器
```
### 4.1.5字符串格式化
>在Python中有两种格式字符串的方法：%表达式和format函数，python官方手册给出的format形式化定义
```
format_spec 　　::=  　　[[fill]align][sign][#][0][width][,][.precision][type]
fill        　　　　　::=  　　<any character>
align       　　　　::=  　　"<" | ">" | "=" | "^"
sign       　　　　 ::=  　　"+" | "-" | " "
width      　　　　 ::= 　　 integer
precision   　　　　::= 　　 integer
type        　　　　::=  　　"b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
```
* fill: 表示显示时需要填充的字符，默认空白字符
* align: 表示输出结果的对齐方式,"^"表示居中
* sign: 仅对数字起作用,表示在显示数字时，是否需要显示"+"和"-"号.默认取值"-",表示在显示正数时,不会显示"+"号,在显示负数时,显示"-"号.当sign为一个空格时(" "),表示"-"和数字之间需要保留一个空格
* width: 表示显示的宽度
* precision: 表示显示的精度
* type: 表示显示的类型
```
"{0} is better than {1}. {2} is better than {3}.".format('Beautiful','ugly','Explicit','implicit')
#在参数多的时候用解释性强的字典dict来做
d = dict(good1='Beautiful', bad1='ugly',good2='Explicit',bad2='implicit')
"{good1} is better than {bad1}. {good2} is better than {bad2}.".format('Beautiful','ugly','Explicit','implicit')
```
> format也可以直接访问对象的属性
```
from collections import namedtuple
Person=namedtuple('student','name,age,sex')
xm=Person(name='sunYang',age=20,sex='male')
print("{p.name} is {p.age} old this year ".format(p=xm))
```
> 以下分别是对format函数的精度、符号、宽度、对齐方式、字符填充、都好等格式进行测试
```
print("{:.2f}".format(3.1415926))
print("{:+.2f}".format(3.1415926))
print("{:10.2f}".format(3.1415926))
print("{:10.2f}".format(3.1415926))
print("{:_^10.2f}".format(3.1415926))
print("{:,}".format(1234567))
print("{:_^+20,.2f}".format(1234.5678))
```
## 4.2 正则表达式
<centre>表4-2 正则表达式基本语法</centre>
<table>
    <tr>
        <th width=8%, bgcolor=yellow >正则表达式</th>
        <th width=20%, bgcolor=yellow>描述</th>
        <th width=50%, bgcolor=yellow>示例</th>
    </tr>
    <tr>
        <td>^</td>    
        <td>行起始标记</td>
        <td>^imp匹配以imp起始的行</td>
    </tr>
    <tr>
        <td>$</td>
        <td>行尾标记</td>
        <td>import$匹配以import结尾的行</td>
    </tr>
    <tr>
        <td>.</td>
        <td>匹配任意一个字符</td>
        <td>linu.匹配linux和linus</td>
    </tr>
    <tr>
        <td>[]</td>
        <td>匹配包含在[字符]之中的任意字符</td>
        <td>coo[kl]可以匹配cook和cool</td>
    </tr>
    <tr>
        <td>[^]</td>
        <td>匹配包含在[^字符]之外的任意字符</td>
        <td>9[^01]不能匹配到91和90</td>
    </tr>
    <tr>
        <td>[-]</td>
        <td>匹配[]中指定范围的任意字符</td>
        <td>[1-5]匹配1~5，[a-z]匹配a~z</td>
    </tr>
    <tr>
        <td>?</td>
        <td>匹配之前项的1次或0次</td>
        <td>hel?o匹配hello或helo,但不能匹配he</td>
    </tr>
    <tr>
        <td>+</td>
        <td>匹配之前项的1次或多次</td>
        <td>hel+可以匹配hel和hell,但不能匹配he</td>
    </tr>
    <tr>
        <td>*</td>
        <td>匹配之前项的0次或多次</td>
        <td>hel+*匹配he,hel,hell</td>
    </tr>
    <tr>
        <td>{n}</td>
        <td>匹配之前项的n次</td>
        <td>[0-9]{3}匹配任意一个三位数</td>
    </tr>
    <tr>
        <td>{n,}</td>
        <td>之前的项至少需要匹配n次</td>
        <td>[0-9]{3,}匹配一个三位数或更多的数字</td>
    </tr>
    <tr>
        <td>{n,m}</td>
        <td>指定之前的项至少需要匹配n次</td>
        <td>[0-9]{2,5}匹配从两位数到五位数之间的任意一个数字</td>
    </tr>
</table>

### 4.2.2 利用re库处理正则表达式
最常用的是re模块下的findall函数，用来输出所有符合模式匹配的子串。

编译的正则表达式(运行更快)如下:
```
import re
data = "What is the difference between python 2.7.13 and Python 3.6.0 ?"
re_obj = re.compile('python [0-9]\.[0-9]\.[0-9]',flags=re.IGNORECASE)
print(re_obj.findall(data))
```
非编译的正则表达式(短)
```
import re
data = "What is the difference between python 2.7.13 and Python 3.6.0 ?"
print(re.findall('python [0-9]\.[0-9]\.[0-9]',data,flags=re.IGNORECASE))
```
### 4.2.3 常用的re方法
> 1"匹配"类的函数
* match类似于字符串的startswith函数
> 2"修改类"函数
* sub类似于字符串的replace函数
* split功能与字符串的split函数一样
> 3大小写不敏感
* flags=re.IGNORECASE
> 4非贪婪匹配
* 正则表达式默认情况下是贪婪的
```
text = "Beautiful is better than ugly. Explicit is better than implicit."
print(re.findall('Beautiful.*\.',text))
print(re.findall('Beautiful.*？\.',text)) # 如果要使用非贪婪匹配,只需在匹配字符串时加上一个"?" 
```

## 4.4 Jinja2模板
是web开发中广泛使用的模板语言Jinja2. 

它能够有效的将业务逻辑和页面逻辑分开，使代码可读性增强、并且更加容易理解和维护。

模板简单来说就是一个响应文本的文件，其中包含用展位变量表示的动态部分，模板文件在经过动态赋值后，返回给用户,其具体值只在请求的上下文中才能知道。

使用真实的值替换变量，再返回最终得到的响应字符串，这一过程称为渲染

例：python标准库自带的模板
```
from string import Template
s = Template('$who is a $role')
s.substitute(who = 'bob', role = 'teacher')
print(s)
s.substitute(who = 'lily', role = 'student')
print(s)
```
### 4.4.2 Jinja2语法入门
* 1.语法块
在Jinja2中存在三种语法:
> 控制变量{%%}
> 变量取值{{}}
> 注释{##}
使用Jinja控制结构和注释的例子:
```
{# note: disabled template because we no longer use this
    {% for user in users %}
        ...
    {%endfor%}
#}

{% if users %}
    <ul>
    {% for user in users %}
        <li>{{ user.username }}</li>
    {% endfor %}
{% endif %}
```
* 2.变量
```
<p>A value from a dicectory:{{ mydict['key'] }}.</p>
<p>A value from a list:{{ mylist[3] }}.</p>
<p>A value from a list, with a variable index: {{ mylist[myintvar] }}.</p>
<p>A value from a object:{{ myobject.somemethod() }}.</p>
```
* 3.Jinja2中的过滤器

<tbody>
    <tr align="center">
        <td>过滤器名称</td>
        <td>&nbsp; &nbsp; 说明&nbsp; &nbsp;&nbsp;</td>
    </tr>
    <tr align="center">
        <td>safe</td>
        <td>&nbsp;渲染时值不转义</td>
    </tr>
    <tr align="center">
        <td>capitialize</td>
        <td>&nbsp;把值的首字母转换成大写，其他子母转换为小写</td>
    </tr>
    <tr align="center">
        <td>&nbsp;lower</td>
        <td>&nbsp;把值转换成小写形式&nbsp;</td>
    </tr>
    <tr align="center">
        <td>&nbsp;upper</td>
        <td>&nbsp;把值转换成大写形式&nbsp;</td>
    </tr>
    <tr align="center">
        <td>&nbsp;title</td>
        <td>&nbsp;把值中每个单词的首字母都转换成大写</td>
    </tr>
    <tr align="center">
        <td>&nbsp;trim</td>
        <td>&nbsp;把值的首尾空格去掉</td>
    </tr>
    <tr align="center">
        <td>&nbsp;striptags</td>
        <td>&nbsp;渲染之前把值中所有的HTML标签都删掉</td>
    </tr>
    <tr align="center">
        <td>join&nbsp;</td>
        <td>&nbsp;拼接多个值为字符串</td>
    </tr>
    <tr align="center">
        <td>&nbsp;replace</td>
        <td>&nbsp;替换字符串的值</td>
    </tr>
    <tr align="center">
        <td>&nbsp;round</td>
        <td>&nbsp;默认对数字进行四舍五入，也可以用参数进行控制</td>
    </tr>
    <tr align="center">
        <td>int&nbsp;</td>
        <td>&nbsp;把值转换成整型</td>
    </tr>
</tbody>

在Jinja2中，变量可以通过“过滤器”修改，过滤器与变量用管道(|)分割。多个过滤器可以链式调用，前一个过滤器的输出会作为后一个过滤器的输入。如下所示
```
{{ "Hello World" | replace("Hello", "Goodbye")}}
    -> Goodbye World
    
{{ "Hello World" | replace("Hello", "Goodbye") | upper}}
    -> GOODBYE WORLD
    
{{ 42.55 | round}}
    -> 43.0
    
{{ 42.55 | round | int }}
    -> 43
```


* 4.Jinja2的控制结构
```
{% if kenny.sick %}
    Kenny is sick.
{% elif kenny.dead %}
    You killed Kenny! You bastard!!!
{% else % }
Kenny looks fine --so far
{% endif %}
```
* 5.Jinja2的for循环
在Jinja2中迭代列表：
<h1>Members</h1>
<u1>
{% for user in users %}
    <li>{{user.username}}</li>
{% endfor%}
</ul>
Jinja2也可以遍历字典：

* 6.Jinja2的宏



* 7.Jinja2的继承和Super函数



* 8.Jinja2的其他运算
> 算数运算 + -  / // % * ** +* -*
> 比较运算 == != > >= < <=
> 逻辑运算 not and or

### 4.4.3 Jinja2实战


# 第5章 Linux系统管理
## 5.1 文件读写


## 5.2 文件与文件路径管理





### 5.2.1 使用os.path进行路径和文件管理
-----------
基础补充：os,os.path模块关于文件，目录常用的方法[链接](https://www.cnblogs.com/marianyad/p/6613753.html)
```
os.getcwd()#返回当前进程路径的字符串
os.path.chdir(file)#改变到目标目录
os.path.abspath(file)#返回路径的字符串
```





# 第6章 使用Python监控Linux系统


# 第7章 文档与报告☆☆☆☆


