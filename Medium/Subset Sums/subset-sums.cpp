//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std; 

// } Driver Code Ends
class Solution
{
public:
    void fun(int ind,int n,vector<int> &arr,int x,vector<int>&v){
        if(ind==n){
            v.push_back(x);
            return ;
        }
        x=x+arr[ind];
        fun(ind+1,n,arr,x,v);
        x=x-arr[ind];
        fun(ind+1,n,arr,x,v);

    }
    vector<int> subsetSums(vector<int> arr, int N)
    {
        // Write Your Code here
        int x=0;
        vector<int>v;
        fun(0,arr.size(),arr,x,v);
        return v;
    }
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int N;
        cin>>N;
        vector<int> arr(N);
        for(int i = 0 ; i < N ; i++){
            cin >> arr[i];
        }
        Solution ob;
        vector<int> ans = ob.subsetSums(arr,N);
        sort(ans.begin(),ans.end());
        for(auto sum : ans){
            cout<< sum<<" ";
        }
        cout<<endl;
    }
    return 0;
}
// } Driver Code Ends