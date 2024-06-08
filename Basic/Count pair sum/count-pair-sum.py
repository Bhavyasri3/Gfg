#User function Template for python3

class Solution:
    def countPairs(self,arr1, arr2, M, N, x):
        c=0
        for i in arr1 :
            if (x-i>0) and ((x-i) in arr2):
                c+=1
        return c
        #code here.



#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    m,n=list(map(int,input().split()))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    x=int(input())
    ob = Solution()
    print(ob.countPairs(a,b,m,n,x))


# } Driver Code Ends