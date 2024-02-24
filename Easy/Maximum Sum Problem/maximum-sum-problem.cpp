//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
    public:
    int solve(int n){
         if(n<=0)return 0;
            int sum=n;
            int f=solve(n/2);
            int s=solve(n/3);
            int t=solve(n/4);
            int res=max(sum,f+s+t);
            return res;

    }
        int maxSum(int n)
        {
            //code here.
          return solve(n);
          }
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        Solution ob;
        cout<<ob.maxSum(n)<<"\n";
    }
    return 0;
}
// } Driver Code Ends