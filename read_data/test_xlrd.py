# -*- coding: utf-8 -*-
# author:BerryHN

import xlrd

workbook=xlrd.open_workbook("/Users/zhiren1111/Desktop/test.xls")
worksheets=workbook.sheet_names()
worksheet1=workbook.sheet_by_index(0)


num_rows=worksheet1.nrows
print num_rows

for curr_row in range(num_rows):
    print worksheet1.row_values(curr_row)

num_cols=worksheet1.ncols
for curr_col in range(num_cols):
    print worksheet1.col_values(curr_col)


for rown in range(num_rows):
    for coln in range(num_cols):
        cell=worksheet1.cell_value(rown,coln)
        print cell
