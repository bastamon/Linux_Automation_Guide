# 第5章 Linux系统管理
## 5.1 文件读写
### 5.1.1 内置open()函数
```
file = open('data1.txt', 'r')
```
> 'w' 若文件非空，则文件会被清空。若文件不存在则会创建

> 'x' 创建文件，若文件存在则会抛出FileExistsError异常

### 5.1.2 避免文件句柄泄露

推荐:
```
with open('data1.txt', 'r') as file:
    print(f.read())
```
不推荐长句
```
```



## 5.2 文件与文件路径管理
### 5.2.1 使用os.path进行文件和路径管理
基础补充：os,os.path模块关于文件，目录常用的方法[链接](https://www.cnblogs.com/marianyad/p/6613753.html)
```
os.getcwd()#返回当前进程路径的字符串
os.path.chdir(file)#改变到目标目录
os.path.abspath(file)#返回路径的字符串
```
* 1.拆分路径 
> split(arg=path):  返回一个二元组，包含文件的路径与文件名

> dirname(arg=path): 返回文件的路径

> basename(arg=path): 返回文件的文件名

> splitext(arg=path): 返回一个去除文件扩展名的部分和扩展名的二元组☆☆☆☆

* 2.构建路径
> expanduser(arg): 展开用户的HOME目录，如‘~’，‘~username’

> abspath(arg): 得到文件或路径的**绝对**路径

> join(args): 使用路径分隔符拼接路径
* 3.获取文件属性
> getatime: 获取文件访问时间

> getmtime: 获取文件修改时间

> getctime: 获取文件创建时间

> getsize: 获取文件的大小

* 4.判断文件类型
> exists: 文件？存在

> isfile: 是？文件

> isdir: 是？文件夹/目录

> islink: 是？链接

> ismount: 是？挂载点

### 5.2.2 使用os模块管理文件和目录
> unlink: 删除path路径所指文件

> rmdir: 删除path路径所指向的文件夹，文件夹必须为空，否则报错

> mkdir: 创建文件夹

> rename: 重命名文件或文件夹

## 5.3 查找文件
### 5.3.1 使用fnmatch库找到特定文件
> fnmatch: 判断文件名是否符合特定的模式

> fnmatchcase: 不区分大小写的情况下，判断文件名是否符合特定的模式

> filter: 返回输入列表中，符合特定的模式的文件名列表

> translate: 将通配符转换为正则表达式
