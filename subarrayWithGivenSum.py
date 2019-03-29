'''
Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. 
Each test case consists of two lines. The first line of each test case is N and S, where N is the size of 
array and S is the sum. The second line of each test case contains N space separated integers denoting the 
array elements.

Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such 
occuring subarray from the left if sum equals to subarray, else print -1.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= A[i] <= 1010

Example:
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5

Explanation :
Testcase1: sum of elements from 2nd position to 4th position is 12
Testcase2: sum of elements from 1st position to 5th position is 15
'''
class subArrayWithGivenSum():
    testCases = None
    testCasesArray = []
    nIntegers = None
    subSum = []

    def __init__(self):
        self.testCases = input('Number of testcases: ')
        self.fillTestCases()
        self.subArraySum()
        
    def fillTestCases(self):
        for i in range(0, int(self.testCases)):
            print("Testcase [" + str(i+1) + "]")
            self.testCasesArray.append(self.fillArray())
        print("--------------------------------------------------------")   
        for i in self.testCasesArray:
            print("TestCase [" + str(self.testCasesArray.index(i)) + "]")
            print(i)
        print("--------------------------------------------------------")

    def fillArray(self):
        self.SizeSum()
        array = []
        nums = input("Insert " + str(self.nIntegers) + " integers separated by space: ").split()
        if(len(nums) > int(self.nIntegers) or len(nums) < int(self.nIntegers)):
            print("ERROR!.. You have entered more/less than " + str(self.nIntegers) + " integers")
            return self.fillArray()
        else:
            for i in nums:
                array.append(i)
        return array
    
    def SizeSum(self):
        self.nIntegers = 0
        nums = input("Insert SIZE of Array and subArray SUM integers separated by space: ").split()
        if(len(nums) > int(2)):
            print("ERROR!.. You have entered more values than what is expected!")
            return self.fillSizeSum()
        else:
            self.nIntegers = nums[0]
            self.subSum.append(nums[1])

    def subArraySum(self):
        for i in self.testCasesArray:
            count = 0           
            for j in range(0, len(i)):
                subSum = 0
                stopIteration = False
                k = j
                while k in range(0, len(i)):
                    subSum = subSum + int(i[k])
                    if(subSum == int(self.subSum[self.testCasesArray.index(i)])):
                        count = count + 1
                        print("Testcase [" + str(int(self.testCasesArray.index(i)) + 1) + "]")
                        print("Solution from position [" + str(j) + "] to [" + str(k) + "]")
                        print("--------------------------------------------------------")
                        stopIteration = True
                    else:
                        k = k + 1
                if(stopIteration == True):
                    subSum = int(self.subSum[self.testCasesArray.index(i)])
                    break
            if(subSum != int(self.subSum[self.testCasesArray.index(i)])):
                print("Testcase [" + str(int(self.testCasesArray.index(i)) + 1) + "]")
                print("-1")
                print("--------------------------------------------------------")       

k = subArrayWithGivenSum()