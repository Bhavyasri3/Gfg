#User function Template for python3

class Solution:
    def DivisibleByEight(self,s):
        #code here
        a=""
        a=int(s[-3:])
        if(a%8==0):
            return 1
        else:
            return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S=input()
        ob=Solution()
        print(ob.DivisibleByEight(S))
# } Driver Code Ends