#User function Template for python3

class Solution:
    def reversedBits(self, x):
        # code here 
        br = '{:032b}'.format(x)
        rv=br[::-1]
        num=int(str(rv),2)
        return num



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends