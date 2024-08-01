class Solution:
    def findExtra(self,n,a,b):
        #add code here
        d={}
        for i in a:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in b:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i,j in d.items():
            if j==1:
                k=i
        return a.index(k)
        
        


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(Solution().findExtra(n, a, b))

# } Driver Code Ends