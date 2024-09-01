#Your task is to complete this function
#Function should return an integer denoting the required answer
class Solution:
    def maxPathSum(self, arr1, arr2):
        # Code here
        n1,n2=len(arr1),len(arr2)
        i,j=0,0
        sum1,sum2=0,0
        result=0
        
        while i <n1 and j<n2:
            if arr1[i] < arr2[j]:
                sum1+=arr1[i]
                i+=1
            elif arr1[i]>arr2[j]:
                sum2+=arr2[j]
                j+=1
            else: #Both are equal, comsider the max sum and add the common element once

                result+=max(sum1,sum2)+arr1[i]
                sum1,sum2=0,0
                i+=1
                j+=1
        while i<n1:                    # Add remaining elements of arr1
            sum1+=arr1[i]
            i+=1
        while j<n2:                    #Add remaining elements of arr2
            sum2+=arr2[j]
            j+=1
        result+=max(sum1,sum2)                    #Add the maximum of the remaining sums to the results
        return result




#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxPathSum(arr1, arr2)
        print(ans)

# } Driver Code Ends