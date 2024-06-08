#User function Template for python3

class Solution:
    def sumOfMinAbsDifferences(self,arr,N):
        arr.sort()
        sum1 = 0
        sum2 = 0
        mm=0
        #code here.
        summ=0
        
        for i in range(N):
            if i==0:
                mm =abs(arr[i]-arr[i+1])
            elif i==N-1:
                mm =abs(arr[i]-arr[i-1])
            else:
                sum1=abs(arr[i]-arr[i+1])
                sum2=abs(arr[i]-arr[i-1])
                mm=min(sum1,sum2)
            summ+=mm
        return summ
            
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a = list(map(int,input().split()))
    ob = Solution()
    ans=ob.sumOfMinAbsDifferences(a,n)
    print(ans)


# } Driver Code Ends