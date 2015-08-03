import xlrd

d= xlrd.open_workbook("sample.xls")
#obtain handle to excle file
d.sheet_names()
#obtain list of worksheet names
sheet = d.sheet_by_index(index)
sheet= d.sheet_by_name(name)
#Obtain worksheet by index/name
row= sheet.row(index)
row[0]= ctype
row[0].value
sheet.ncols
sheet.nrows
sheet.cell_values(x,y)