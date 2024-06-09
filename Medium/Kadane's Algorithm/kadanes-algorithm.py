#User function Template for python3

class Solution:
    
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr, n):
        maxsofar=-9999999
        maxendhere=0;
        for i in range(len (arr)):
            maxendhere+=arr[i]
            if maxendhere>maxsofar:
                maxsofar=maxendhere
            if maxendhere<0:
                maxendhere=0
        return maxsofar
        ##Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr, n))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends