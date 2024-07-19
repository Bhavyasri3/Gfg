#User function Template for python3
import bisect 
class Solution:

	def constructLowerArray(self,arr):
		# code here
		ans=[]
		sortedlist=[]
		for i in reversed(arr):
		    k=bisect.bisect_left(sortedlist,i)
		    sortedlist.insert(k,i)
		    ans.append(k)
		return ans[::-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.constructLowerArray(arr)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends