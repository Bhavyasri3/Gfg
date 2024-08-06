#User function Template for python3

class Solution:
    def perm(self,l,n,res,vis,choose):
        if len(choose)==n:
            res.append("".join(choose))
            return
        for i in range(n):
            # code for removing the duplicates
            if (vis[i] or(i>0 and l[i]==l[i-1] and vis[i-1])):
                continue
            if vis[i]!=1:
                vis[i]=1
                choose.append(l[i])
                self.perm(l,n,res,vis,choose)
                choose.pop()
                vis[i]=0
    
    def find_permutation(self, S):
        # Code here
        k=list(S)
        l=sorted(k)
        n=len(l)
        res=[]
        vis=[0]*n
        choose=[]
        self.perm(l,n,res,vis,choose)
        return res
     
        
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		ans.sort()
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends