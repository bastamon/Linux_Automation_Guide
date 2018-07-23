from com_filter1 import comfilter
import os


if 'test.py' in os.listdir(path='.'):
    la = ["./com_filter.py", "./components1","./components2",""]
else:
    la = ["./experim/com_filter.py", "./experim/components1","./experim/components2",""]
print(len(la))
comfilter(la[1:])


# from test_xls import main

# main("node20180714.xlsx")


