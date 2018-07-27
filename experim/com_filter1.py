# -*- coding:utf-8 -*-
from __future__ import print_function
import sys
import re


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
            if re.match('# CMP',line):
                start_line.append(num)
                # print("find CMP in" + str(num))
                fg = True
                continue
            if "#" == line and fg:
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
                cmp_book[num] = cmp_book[num] + "\n#"  # cmp_book[num] = "\n" + cmp_book[num]+"\n#"
        # print(cmp_book)
        for num, page in enumerate(cmp_book):
            # for line in page.split("\n"):
            if "PRP PART_NAME 'SHORTING_RES'" in page or "PRP PART_NAME 'RES" in page or "PRP PART_NAME 'CAP" in page:
                # dele page
                del cmp_book[num]
        print("file " + la[i] + " done\n")
        ex_book = []

        for page in cmp_book:
            try:
                exstr = "".join(re.findall('# CMP [0-9]{1,4}',page)).ljust(10)

                exstr += "\t" + "".join(re.findall('[1-9]{1,4}', "".join(re.findall('ID=[1-9]{1,4}',page)))).rjust(4)

                exstr += "\t" + "".join(re.findall("'(.+?)'", "".join(re.findall('PRP PART_NUMBER.*[^\n]',page)))).ljust(22)

                exstr += "\t" + "".join(re.findall("(?<=TOP 0\s).*?(?=N)",page)).ljust(25)
                exstr += "\t" + "".join(re.findall("(?<=TOP 1\s).*?(?=N)", page)).ljust(25)

                exstr += "\t" + "".join(re.findall("[^N\s].*","".join(re.findall("N.*", str(re.findall("TOP 0\s.*",page)[0]))))).ljust(10)
                exstr += "\t" + "".join(re.findall("[^N\s].*", "".join(re.findall("N.*", str(re.findall("TOP 1\s.*", page)[0]))))).ljust(10)
                print(exstr)
                ex_book.append(exstr)

            except IndexError as err:
                print(cmp_book+str(err))
                pass
            # exstr = "".join(re.findall('# CMP [0-9]{1,4}',page))+"\t"+str(re.findall('[1-9]{1,4}',str(re.findall('ID=[1-9]{1,4}',page)))[0])
            #
            # exstr += "\t"+"".join(re.findall('[1-9]{1,4}',"".join(re.findall('ID=[1-9]{1,4}',page))))
            #
            # exstr += "\t"+ "".join(re.findall("'(.+?)'","".join(re.findall('PRP PART_NUMBER.*[^\n]',page))))
            #
            # exstr += "\t" + "".join(re.findall("(?<=TOP 0\s).*?(?=N)",page))
            # exstr += "\t" + "".join(re.findall("(?<=TOP 1\s).*?(?=N)", page))
            #
            # exstr += "\t" + "".join(re.findall("[^N\s].*","".join(re.findall("N.*", str(re.findall("TOP 0\s.*",page)[0])))))
            # exstr += "\t" + "".join(re.findall("[^N\s].*", "".join(re.findall("N.*", str(re.findall("TOP 1\s.*", page)[0])))))
            # print(exstr)
            # ex_book.append(exstr)


        content_w += "\n".join(ex_book)
    with open('./resultcom.txt', 'w') as resfile:
        resfile.write(content_w)


def main():
    sys.argv.append("")
    # la = sys.argv[1:]
    comfilter(sys.argv[1:])


if __name__ == '__main__':
    main()
