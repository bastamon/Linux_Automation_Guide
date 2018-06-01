###mysql的安装
##http://www.runoob.com/mysql/mysql-install.html
sudo apt-get install mysql-client mysql-server mysql-server-5.7
#记得一定要设密码
##可选安装MySQL Workbench



###Tomcat的安装
sudo apt-get install tomcat7 tomcat7-docs tomcat7-examples tomcat7-admin
#或者
sudo apt-get install tomcat8
#默认端口为:8080
##访问tomcat7首页上的Server Status、Manager App、Host Manager网页
#打开/etc/tomcat7/tomcat-users.xml
#<role rolename="manager"/>  //Tomcat6
#<role rolename="manager-gui"/>  //Tomcat7
#<role rolename="admin"/>  //Tomcat6
#<role rolename="admin-gui"/>  //Tomcat7
#<user username="admin" password="admin" roles="admin-gui,manager-gui"/>



###mysql数据库允许远程连接
https://jingyan.baidu.com/article/64d05a0258526dde54f73b6a.html

###MySQL基本操作
##查看所有数据库:
show databases
##查看当前数据库的所有表的名字
select name from sysobjects where xtype='U' and category=
##切换(使用)数据库
use DATABASES





