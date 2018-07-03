# -*-coding:utf-8 -*-
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


