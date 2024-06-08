#User function Template for python3

class Solution:
    def isPossible(self,a, b, n, k):
        c=0
        a1= a.sort()
        b1=b.sort(reverse = True)
        for i in range(n):
            if (a[i]+b[i]) >= k:
                c+=1
        if c==n:
            return True
        return False
        
    # Your code goes here
   


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
    	sz = [int(x) for x in input().strip().split()]
    	n, k = sz[0], sz[1]
    	a = [int(x) for x in input().strip().split()]
    	b = [int(x) for x in input().strip().split()]
    	ob=Solution()
    	if ob.isPossible(a, b, n, k):
    		print(1)
    	else:
    		print(0)
    	
    	T -= 1

if __name__ == "__main__":
    main()







# } Driver Code Ends