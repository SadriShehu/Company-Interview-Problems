'''
A surpasser of an element of an array is a greater element to its right, therefore x[j] is a surpasser of x[i] if i < j and x[i] < x[j]. The surpasser count of an element is the number of surpassers.
Given an array of distinct integers, for each element of the array find its surpasser count i.e. count the number of elements to the right that are greater than that element.
 

Input:

The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of two lines. The first line of each test case consists of an integer N, where N is the size of array.
The second line of each test case contains N space separated integers denoting array elements.
 

Output:

Corresponding to each test case, in a new line, print the surpasser count i.e. count the number of elements to the right that are greater than that element.
 

Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 500
1 ≤ A[i] ≤ 1000

---

Solved by: Sadri Shehu
Date: 3/27/2019

[[sheet.cell_value(r, c) ] ]

for c in range(sheet.ncols):
    for r in range(sheet.nrows):
        array.append(sheet.cell_value(r, c))


'''
import xlrd

class surpasserCount():
    testCasesArray = []

    def __init__(self):
        datasheet = input("Insert you datasheet : ")
        config = xlrd.open_workbook(datasheet)
        sheet = config.sheet_by_index(0)
        for r in range(sheet.nrows):
            array = []
            for c in range(sheet.ncols):           
                array.append(sheet.cell_value(r, c))
            self.testCasesArray.append(array)
        for i in self.testCasesArray:
            print(i)

    def surpasser(self):
        print("Results from testcases: ")
        for i in self.testCasesArray:
            surpassers = []
            for j in range(0, len(i)):
                count = 0
                k = j
                while k in range(0, len(i)):
                    if(int(i[j])<int(i[k])):
                        count = count + 1
                    k = k + 1
                surpassers.append(count)
            print(surpassers)
            
k = surpasserCount()
k.surpasser()
