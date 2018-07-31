# -*- coding:utf-8 -*-
from __future__ import print_function
import sys


def main(la):
    for i, x in enumerate(la):
        la[i] = int(x)
    temp = []
    for i in range(0, 3):
        temp.append(max(la))
        la.remove(temp[i])
    if len(temp) == 3:
        return temp[0] * temp[1] * temp[2]


if __name__ == '__main__':
    sys.argv.append()
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            content = file.read()
            main(content.split(" "))#以空格分割的数字文件