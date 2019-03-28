'''
A surpasser of an element of an array is a greater element to its right, therefore x[j] 
is a surpasser of x[i] if i < j and x[i] < x[j]. The surpasser count of an element is the number of surpassers.
Given an array of distinct integers, for each element of the array find its surpasser count 
i.e. count the number of elements to the right that are greater than that element.
 

Input:

The first line of input contains a single integer T denoting the number of test cases. 
Then T test cases follow. Each test case consist of two lines. The first line of each 
test case consists of an integer N, where N is the size of array.
The second line of each test case contains N space separated integers denoting array elements.
 

Output:

Corresponding to each test case, in a new line, print the surpasser count i.e. count the 
number of elements to the right that are greater than that element.
 

Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 500
1 ≤ A[i] ≤ 1000

---

Solved by: Sadri Shehu
Date: 3/27/2019
'''

class surpasserCount():
    testCases = None
    testCasesArray = []
    nIntegers = None

    def __init__(self, testCases, nIntegers):
        self.testCases = testCases
        self.nIntegers = nIntegers
        self.fillTestCases()    

    def fillTestCases(self):
        for i in range(0, int(self.testCases)):
            print("Testcase " + str(i+1))
            self.testCasesArray.append(self.fillArray())
        
        print("TestCases are: ")
        for i in self.testCasesArray:
            print(i)
        
    def fillArray(self):
        array = []
        nums = input("Insert " + str(self.nIntegers) + " integers separated by space: ").split()
        if(len(nums) > int(self.nIntegers)):
            print("ERROR!.. You have entered more than " + str(self.nIntegers) + " integers")
            return self.fillArray()
        else:
            for i in nums:
                array.append(i)
        return array

    def surpasser(self):
        print("Results from testcases: ")
        for i in self.testCasesArray:
            surpassers = []
            for j in range(0, len(i)):
                count = 0
                k = j
                while k in range(0, len(i)):
                    if(i[j]<i[k]):
                        count = count + 1
                    k = k + 1
                surpassers.append(count)
            print(surpassers)

testCases = input('Number of testcases: ')
nIntegers = input('Integer per testcase: ')

k = surpasserCount(testCases, nIntegers)
k.surpasser()
