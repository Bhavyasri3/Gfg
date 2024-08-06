#User function Template for python3

class Solution:
    def perm(self,l,n,res,vis,choose):
        if len(choose)==n:
            res.append("".join(choose))
            return
        for i in range(n):
            # if i > 0 and l[i] == l[i-1] and not vis[i-1]:
            #     continue
            if vis[i]!=1:
                vis[i]=1
                choose.append(l[i])
                self.perm(l,n,res,vis,choose)
                vis[i]=0
                choose.pop()
        
    def permutation(self,s):
        l=sorted(s)
        n=len(l)
        res=[]
        choose=[]
        vis=[0]*n
        self.perm(l,n,res,vis,choose)
        res.sort()
        return res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    while(T>0):
        s=input()
        ob=Solution()
        ans=ob.permutation(s)
        for i in ans:
            print(i,end=" ")
        print()
        
        T-=1
# } Driver Code Ends