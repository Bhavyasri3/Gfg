//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution
{
    
    public:
    //Function to check if brackets are balanced or not.
    bool ispar(string x)
    {
        stack<char>st;
        //Your code here
        if(( x.size())%2!=0) {
            return false;
            
        }
        for(char i:x){
            if(i=='{'|| i=='('|| i=='[')
            {
                st.push(i);
            }
            else if((!st.empty()) and ((st.top()=='{' and i=='}') || (st.top()=='(' and i==')')|| (st.top()=='[' and i==']'))){
                st.pop();
            }
            else return false;
        }
        if(st.empty()) return true;
        return false;
    }

};

//{ Driver Code Starts.

int main()
{
   int t;
   string a;
   cin>>t;
   while(t--)
   {
       cin>>a;
       Solution obj;
       if(obj.ispar(a))
        cout<<"balanced"<<endl;
       else
        cout<<"not balanced"<<endl;
   }
}
// } Driver Code Ends