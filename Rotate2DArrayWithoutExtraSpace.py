'''
You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise).
You need to do this in place. Note that if you end up using an additional array, you will only 
receive partial score.

Example:

If the array is 
1 2 3 4 5 6 7 8 9

Then the rotated array becomes: 
7 4 1 8 5 2 9 6 3

Input:

The first line contains an integer 'T' denoting the total number of test cases.
In each test cases, the first line contains an integer 'N' denoting the size of the 2D square matrix.
And in the second line, the elements of the matrix A[][], each separated by a space in row major form.


Output:

For each test case, print the elements of the rotated array row wise, each element separated by a 
space. Print the output of each test case in a new line.

Constraints:

1 ≤ T ≤ 70
1 ≤ N ≤ 10
1 ≤ A [ i ][ j ] ≤ 100

Example:

Input:

2
3
1 2 3 4 5 6 7 8 9
2
56 96 91 54

Output:

7 4 1 8 5 2 9 6 3
91 56 54 96 

---
Solved by: Sadri Shehu
Date: 4/1/2019
'''
class rotate2DArray():
    testCases = None
    testCasesArray = []
    nIntegers = None

    def __init__(self):
        self.testCases = input('Number of testcases: ')
        self.fillTestCases()
        self.printMatrix()

    def fillTestCases(self):
        for i in range(0, int(self.testCases)):
            print("Testcase [" + str(i+1) + "]")
            self.testCasesArray.append(self.fillArray())
        print("--------------------------------------------------------")   
        for i in self.testCasesArray:
            print("TestCase [" + str(self.testCasesArray.index(i) + 1) + "]")
            print(i)
        print("--------------------------------------------------------")

    def fillArray(self):
        self.nIntegers = input('Insert 2D Array Dimesnion: ')
        nIntegers = int(self.nIntegers) * int(self.nIntegers)
        array = []
        nums = input("Insert " + str(nIntegers) + " integers separated by space: ").split()
        if(len(nums) > nIntegers or len(nums) < nIntegers):
            print("ERROR!.. You have entered more/less than " + str(self.nIntegers) + " integers")
            return self.fillArray()
        else:          
            for i in range(int(self.nIntegers)):
                subArray = []
                for j in range(int(self.nIntegers)):
                    subArray.append(nums[int(self.nIntegers) * i + j])
                array.append(subArray)
        return array
        
    def printMatrix(self):
        for i in self.testCasesArray:
            for j in range(0, int(int(self.nIntegers)/2)):
                for k in range(j, int(int(self.nIntegers) - j - 1)):
                    temp = i[j][k]
                    i[j][k] = i[int(int(self.nIntegers) - k - 1)][j]
                    i[int(int(self.nIntegers) - k - 1)][j] = i[int(int(self.nIntegers) - j - 1)][int(int(self.nIntegers) - k - 1)]
                    i[int(int(self.nIntegers) - j - 1)][int(int(self.nIntegers) - k - 1)] = i[k][int(int(self.nIntegers) - j - 1)]
                    i[k][int(int(self.nIntegers) - j-1)] = temp
            print('2D Rotated Testcase [' + str(int(self.testCasesArray.index(i)) + 1) + ']')
            print(i)
k = rotate2DArray()
