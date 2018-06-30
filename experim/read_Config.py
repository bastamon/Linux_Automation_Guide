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



