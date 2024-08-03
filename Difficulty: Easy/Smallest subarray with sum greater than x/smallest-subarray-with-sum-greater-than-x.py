class Solution:
    def smallestSubWithSum(self, x, arr):
        # Your code goes here 
        c=0
        m=len(arr)+1
        temp=m
        l=[]
        # queue initialisation
        for i in arr:
            c+=i
            l.append(i)
            while c>x and l:
                m=min(len(l),m)
                c-=l.pop(0)
        if m==temp:
            return 0
        return m
        



#{ 
 # Driver Code Starts
def main():

    T = int(input())

    while (T > 0):
        x = int(input())
        a = [int(x) for x in input().strip().split()]
        print(Solution().smallestSubWithSum(x, a))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends