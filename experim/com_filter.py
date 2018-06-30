# -*- coding:utf-8 -*-
from __future__ import print_function
import sys


def comfilter(la):
    # exclude_item =
    # print (la)
    # pattern = re.compile(r'[# CMP] \D')
    content_w = ""
    for i in range(0, len(la) - 1, 1):
        with open(la[i]) as cmpfile:
            content = cmpfile.read()
            # arr_line = cmpfile.readlines()
        arr_line = content.split("\n")
        start_line = []
        end_line = []
        count = 0
        fg = False
        for num, line in enumerate(arr_line):
            if "# CMP " in line:
                start_line.append(num)
                # print("find CMP in" + str(num))
                fg = True
                continue
            if "#" in line and fg:
                end_line.append(num)
                count += 1
                fg = False
        cmp_book = []
        for num in range(0, count, 1):
            cmp_book.append(arr_line[start_line[num]])
            for line_num in range(start_line[num] + 1, end_line[num], 1):
                # print(line_num)
                cmp_book[num] = cmp_book[num] + "\n" + arr_line[line_num]
            # print(cmp_book[num])
            cmp_book[num] = "#\n" + cmp_book[num]
        # print(cmp_book)
        for num, page in enumerate(cmp_book):
            # for line in page.split("\n"):
            if "PRP PART_NAME 'SHORTING_RES'" in page or "PRP PART_NAME 'RES" in page or "PRP PART_NAME 'CAP" in page:
                # dele page
                del cmp_book[num]
        print("file " + la[i] + " done\n")
        content_w += "\n".join(cmp_book)
    with open('./resultcom.txt', 'w') as resfile:
        resfile.write(content_w)


def main():
    sys.argv.append("")
    # la = sys.argv[1:]
    comfilter(sys.argv[1:])


if __name__ == '__main__':
    main()
