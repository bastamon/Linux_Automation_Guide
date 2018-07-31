import xlrd
import xlwt
import sys
from xlutils.copy import copy

def main(arr):
    xls_file = xlrd.open_workbook(arr)
    xls_sheet = xls_file.sheets()[0]
    col_value = xls_sheet.col_values(1)
    for i,x in enumerate (col_value[1:]):
         col_value[i+1]="0x".join(str(hex(int(x))))

    new_xls = copy(xls_file)
    w_sheet = new_xls.get_sheet(0)
    for row_index in range(1, len(col_value)):
        w_sheet.write(row_index, 1, col_value[row_index-1])
    w_sheet.save(arr)


if __name__ == '__main__':
    sys.argv.append()
    main(sys.argv[1])