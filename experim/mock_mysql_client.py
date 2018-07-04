# -*- coding:utf-8 -*-
from __future__ import print_function
import argparse

def _argparse():
    parser = argparse.ArgumentParser(description='A python-mysql client')
    parser.add_argument('--host',action='store',dest='host',required=True,help='connect to host')
    parser.add_argument('-u','--user',action='store',dest='user',required=True,help='user for login')
    parser.add_argument('-p','--password',action='store',dest='password',required=True,help='passwoed to use when connecting to server')
    parser.add_argument('-P','--Port',action='store',dest='port',default=3306,type=int,required=True,help='port number to use for connection or 3306 for default')
    parser.add_argument('-v','--version',action='version',version='%(prog)s 0.1')
    return parser.parse_args()


def main():
    parser = _argparse()
    conn_args = dict(host=parser.host,user=parser.user,password=parser.password,port=parser.port)
    print(conn_args)

if __name__=='__main__':
    main()