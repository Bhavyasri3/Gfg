#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        # Code here
        for i in range(1,len(s)):
            if not(ord(s[i])>=48 and ord(s[i])<=57):
                return -1
        if(s[0]=="-" or (ord(s[0])>=48 and ord(s[0])<=57)):
            return int(s)
        return -1
                
        


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends