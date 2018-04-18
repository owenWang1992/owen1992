#https://learnxinyminutes.com/docs/python3/
#read the article about
#create a function call mean
# variables, collection (array, set , dictionary), looping, if-else-else-if, function, object
# 

import os,xlrd

def sum(inputList):
    x = 0
    for y in inputList:
        x = x + y
    return x

print(sum([1, 2, 4, 9]))

#mean is sum/num, complete mean function and print out result of  mean([2, 4, 5, 6])
def mean(inputList):
    x = 0
    for y in inputList:
        x = x + y
    return ( x / len(inputList))
print(mean([1,2,3,4]))

#define a squart function.    squart([2, 4, 5, 6]) must return [4, 16, 25, 36]
def squart(inp):
    x = []
    for y in inp:
        x.append(y*y)
    return x
print (squart([2,4,5,6]))    



#define sumodd function to sum all odd number in a list, oddsum([1, 3, 4, 5, 6]) must result 9
def oddsum(inp):
    x = 0
    for y in inp:
        if y % 2 != 0:
            x = x + y
    return x
print (oddsum([1,3,4,5,6]))


#define listDir function to list content of a directory, for example, listDir("c:/") must print out all files in the path c:/, google to find how to do it
def listDir(path):
    print(os.listdir(path))
listDir("c:/owen1992")
#define readExcel function to read and print content of excel,  readExcel("c:/myexcel.xls", 0) will read sheet 0 content, using xlrd library
def readExcel(excelpath, sheetIndex, c):
    xl_workbook = xlrd.open_workbook(excelpath)
    sheet_names = xl_workbook.sheet_names()gi
    print('Sheet Names', sheet_names)
    xl_sheet = xl_workbook.sheet_by_name(sheet_names[sheetIndex])
    print(xl_sheet.col(c))


readExcel("LandingPageTestOP.xlsx", 0, 2)


