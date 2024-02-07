//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// Function to return minimum number of jumps to end of array

class Solution{
  public:
    int minJumps(int arr[], int n){
        // Your code here
        int i=0;
        int mx=0;
        int r=0;
        int c=0;
        if(arr[0]==0)
        {
            return -1;
        }
        if(n==1)
        {
            return 0;
        }
        while(i<n){
            mx=max(mx,i+arr[i]);
            if(i==r){
                //cout << r << endl;
                r=mx;
                
                c+=1;
                //cout << r << endl;
                if(r>=n-1){
                    return c;
                }
            }
            i+=1;
        }
        return -1;
    }
};


//{ Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,i,j;
        cin>>n;
        int arr[n];
        for(int i=0; i<n; i++)
            cin>>arr[i];
        Solution obj;
        cout<<obj.minJumps(arr, n)<<endl;
    }
    return 0;
}

// } Driver Code Ends