#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        l1=[]
        l2=[]
        # if(len(a)!=len(b)):
        #     return "NO"
        # for i in a:
        #     l1.append(i)
        #     l1.sort()
        # for i in b:
        #     l2.append(i)
        #     l2.sort()
        
        # if l1==l2:
        #     return "YES"
        # print(l1)
        # print(l2)
        
        # return "NO"
        
        return sorted(list(a)) == sorted(list(b))
            
                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends