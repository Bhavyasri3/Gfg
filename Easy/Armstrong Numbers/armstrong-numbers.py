#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        s=str(n)
        sum=0
        for i in s:
            j=int(i)
            sum+=j*j*j
            
        if n==sum:
            return "Yes"
        else:
            return "No"
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends