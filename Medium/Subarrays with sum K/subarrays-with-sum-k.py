#User function Template for python3

class Solution:
    def findSubArraySum(self, nums, N, goal):
        su= 0
        d = {0:1}  
        count = 0
        
        for i in range(len(nums)):
            su += nums[i]
            if su - goal in d:
                count += d[su - goal]
            if su in d:
                d[su] += 1
            else:
                d[su] = 1
                
        return count

        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.findSubArraySum(Arr, N, k))
# } Driver Code Ends