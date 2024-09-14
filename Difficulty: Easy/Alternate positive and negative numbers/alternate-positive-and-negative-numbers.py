#User function Template for python3

class Solution:
    def rearrange(self,arr):
        n=len(arr)
        pos,neg=[],[]
        for item in arr:
            if item>=0:
                pos.append(item)
            else:
                neg.append(item)
        pIdx,nIdx=0,0
        i=0
        while i<n and pIdx<len(pos) and nIdx<len(neg):
            if i%2:
                arr[i]=neg[nIdx]
                nIdx+=1
            else:
                arr[i]=pos[pIdx]
                pIdx+=1
            i+=1
        while pIdx<len(pos):
            arr[i]=pos[pIdx]
            pIdx+=1
            i+=1
        while nIdx<len(neg):
            arr[i]=neg[nIdx]
            nIdx+=1
            i+=1
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends