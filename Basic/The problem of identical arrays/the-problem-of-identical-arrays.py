#User function Template for python3

def check (arr,  brr, n) : 
    c=0
    d1={}
    d2={}
    for i in arr:
        if i not in d1:
            d1[i]=1
        else:
            d1[i]+=1
    for i in brr:
        if i not in d2:
            d2[i]=1
        else:
            d2[i]+=1
    if d1==d2:
        return 1
    else:
        return 0
      
    #Complete the function




#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    brr = list(map(int,input().strip().split()))
    
    print(check(arr, brr, n))




# } Driver Code Ends