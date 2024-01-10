class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, K) : 
        d= {0: -1}
        c=0
        m=0
        for i in range(n):
            c += arr[i]
            r = (c % K + K) % K
            m = max(m, i - d.setdefault(r, i))
        
        return m



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends