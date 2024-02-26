//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{
	public:
	void fun(int ind,string s,vector<string>&ans,string res){
	    if(ind>=s.size()){
	        if(!res.empty())
	        ans.push_back(res);
	        return;
	    }
	    else{
	        fun(ind+1,s,ans,res+s[ind]);
	        fun(ind+1,s,ans,res);
	    }
	}
		vector<string> AllPossibleStrings(string s){
		    // Code here
		    vector<string>ans;
		    fun(0,s,ans,"");
		    sort(ans.begin(),ans.end());
		    return ans;
		}
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		string s;
		cin >> s;
		Solution ob;
		vector<string> res = ob.AllPossibleStrings(s);
		for(auto i : res)
			cout << i <<" ";
		cout << "\n";

	}
	return 0;
}
// } Driver Code Ends