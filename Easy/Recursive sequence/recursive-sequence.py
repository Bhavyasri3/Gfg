#User function Template for python3

class Solution:
    def sequence(self, n):
        # code here
        s = 1
        m = 10 ** 9 + 7
        a = 2
        for i in range(2, n+1):
            b = a + i
            p = 1
            for j in range(a, b):
                p *= j
            s += p
            a = b
        return (s % m)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends