# coding: utf-8

# function
def triangle(rows):
    for rownum in range (rows):
        newValue= 1
        PrintingList = [newValue]
        for iteration in range (rownum):
            newValue = newValue * ( rownum-iteration ) * 1 / ( iteration + 1 )
            PrintingList.append(int(newValue))
        print(PrintingList)

# getting data
rows = int(raw_input())

# execution
triangle(rows)
