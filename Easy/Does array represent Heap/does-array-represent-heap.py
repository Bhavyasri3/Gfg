
class Solution:
    def isMaxHeap(self,arr,n):
        # Your code goes here
        for i in range(n//2):
            m=(2*i)+1
            k=(2*i)+2
            if(m<n and k<n and (arr[i]<arr[m] or arr[i]<arr[k])):
                return 0
            else:
                if(m>=n and k<n and arr[i]<arr[k]):
                    return 0
                if(k>=n and m<n and arr[i]<arr[m]):
                    return 0
        return 1



#{ 
 # Driver Code Starts
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob=Solution()
        print(int(ob.isMaxHeap(arr,n)))
# } Driver Code Ends