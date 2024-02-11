#User function Template for python3

class Solution:
    def recamanSequence(self, n):
        # code here
        l=[0]*n
        s = {0}
        for i in range(1,len(l)):
            if(l[i-1]-i>0) and l[i-1]-i not in s:
                s.add(l[i-1]-i)
                l[i] = l[i-1]-i
            else:
                s.add(l[i-1]+i)
                l[i] = l[i-1]+i
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.recamanSequence(n)
        for i in range(n):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends