//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++

class Solution{
    public:
    void maze(vector<vector<int>>&m,vector<string>&vc,int i,int j,string s,vector<vector<int>>&vis){
        if(i<0 || j<0 || i >= m.size() || j >= m[i].size() || vis[i][j]==1 || m[i][j]==0){
            return ;
        }
        if(i==m.size()-1 and j==m.size()-1)
        {
            //cout << s << endl;
            vc.push_back(s);
            return;
        }
        vis[i][j]=1;
        maze(m,vc,i+1,j,s+'D',vis);
        maze(m,vc,i-1,j,s+'U',vis);
        maze(m,vc,i,j+1,s+'R',vis);
        maze(m,vc,i,j-1,s+'L',vis);
        vis[i][j]=0;
    }
    vector<string> findPath(vector<vector<int>> &m, int n) {
        // Your code goes here
        vector<string>vc;
        vector<vector<int>>vis(n,vector<int>(n,0));
        maze(m,vc,0,0,"",vis);
        return vc;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<vector<int>> m(n, vector<int> (n,0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> m[i][j];
            }
        }
        Solution obj;
        vector<string> result = obj.findPath(m, n);
        sort(result.begin(), result.end());
        if (result.size() == 0)
            cout << -1;
        else
            for (int i = 0; i < result.size(); i++) cout << result[i] << " ";
        cout << endl;
    }
    return 0;
}
// } Driver Code Ends