from itertools import groupby
import xlrd
import xlwt
import numpy as np


import TreeAnalysis as ta
import TreeAnalysisMOD as tam

FileName="EXCEL_15_WEATHER_NEW.xlsx"
SheetN="Sheet 1"
data = xlrd.open_workbook(FileName)
Sheet = data.sheet_by_name(SheetN)
ArrSen=[]
Check = 0

for i in range(5, Sheet.nrows - 1):
    #print (Sheet.nrows)
    StringChk = Sheet.cell(i, 0).value
    #print (str(Sheet.cell(i, 0)))
    if str(Sheet.cell(i, 0).value).isnumeric():
        ArrSen.append(i)
        #print(str(Sheet.cell(i, 0).value))
        Check = i
        #print (i, Sheet.cell(i, 1).value)
    #print(ArrSen)
    if StringChk[0] == "#" and Check == i-1:
        #print(ArrSen)
        #print("Nice")
        #f1.SenType(ArrSen)
        tam.treeanalysis(ArrSen,FileName,SheetN)
        #print (ArrSen)
        ArrSen = []
        #print(i)

    if i == int(Sheet.nrows-2):
        #print (i)
        tam.treeanalysis(ArrSen, FileName, SheetN)
        ArrSen = []


