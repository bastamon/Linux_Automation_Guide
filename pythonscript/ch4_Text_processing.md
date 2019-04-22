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

