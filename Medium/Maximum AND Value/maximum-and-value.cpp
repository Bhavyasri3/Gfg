//{ Driver Code Starts
//Initial Template for C++
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++
 
class Solution
{
    public:
    // Function for finding maximum AND value.
    int maxAND (int arr[], int N)
    {
        int ans=0;
        for(int i=31;i>=0;i--){
            int count=0;
            for(int it=0;it<N;it++){
                if(arr[it]>0) count+=((arr[it]>>i)&1);
            }
            if(count>1){
                ans+=(1<<i);
                for(int it=0;it<N;it++){
                    if(arr[it]>0 && !((arr[it]>>i)&1)){
                        arr[it]=0;
                    }
                }
            }
        }
        return ans;
    }
};

//{ Driver Code Starts.
 
// Driver function
int main()
{
    int t;
    cin>>t;//testcases
    while(t--)
    {
        int n;
        cin>>n;//input n
        int arr[n+5],i;
        
        //inserting elements
        for(i=0;i<n;i++)
        cin>>arr[i];
        Solution obj;
        //calling maxAND() function
        cout <<  obj.maxAND(arr,n)<<endl;
    }
    return 0;
}
// } Driver Code Ends