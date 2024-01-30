//{ Driver Code Starts
//Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function template for C++
class Solution {
public:
 void combsum(int ind,int n,vector<int>& candidates, int target,vector<int>&ds,vector<vector<int>>&res){
    if(ind==n){
        if(target==0){
            res.push_back(ds);
            return;
        }
        return;
    }
    //pick
    if(candidates[ind]<=target){
        ds.push_back(candidates[ind]);
        combsum(ind,n,candidates,target-candidates[ind],ds,res);
        ds.pop_back();
    }
    combsum(ind+1,n,candidates,target,ds,res);

    return;
}
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        //to obtain unique and ascending order elements we need to first sort and then again convert it into vector.
        vector<int>ds;
        sort(candidates.begin(),candidates.end());
        set<int>s1;
        for(int i=0;i<candidates.size();i++){
            s1.insert(candidates[i]);
        }
        vector<int>v1;
        for(auto it :s1){
            v1.push_back(it);
        }
        vector<vector<int>>res;
        combsum(0,v1.size(),v1,target,ds,res);
        return res;
    }
};


//{ Driver Code Starts.
int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int> A;
        for(int i=0;i<n;i++){
            int x;
            cin>>x;
            A.push_back(x);
        }   
        int sum;
        cin>>sum;
        Solution ob;
        vector<vector<int>> result = ob.combinationSum(A, sum);
   		if(result.size()==0){
   			cout<<"Empty";
   		}
        for(int i=0;i<result.size();i++){
            cout<<'(';
            for(int j=0;j<result[i].size();j++){
                cout<<result[i][j];
                if(j<result[i].size()-1)
                    cout<<" ";
            }
            cout<<")";
        }
        cout<<"\n";
    }
}	
// } Driver Code Ends