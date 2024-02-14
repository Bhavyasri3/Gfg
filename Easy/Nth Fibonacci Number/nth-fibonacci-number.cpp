//{ Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++
class Solution {
  public:
    long long m = 1000000007;
    long long func(vector<long long> &dp, int n){
        if(n<=1){
            return n;
        }
        if(dp[n]!=-1){
            return dp[n];
        }
        dp[n] = (func(dp, n-1)%m + func(dp, n-2)%m)%m;
        return dp[n];
    }
  
    int nthFibonacci(int n){
        // code here
        vector<long long> dp(n+1, -1);
        dp[0] = 0;
        dp[1] = 1;
        func(dp, n);
        return dp[n];
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        Solution ob;
        cout << ob.nthFibonacci(n) << endl;
    }
    return 0;
}

// } Driver Code Ends