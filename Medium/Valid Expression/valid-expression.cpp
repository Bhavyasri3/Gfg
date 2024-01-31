//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;
bool valid(string str);
int main()
{
    int t;
    cin>>t;
    cin.ignore();
    while(t--)
    {
        string str;
        getline(cin,str);
        cout<<valid(str)<<endl;
    }
    return 0;
}
// } Driver Code Ends


bool valid(string s)
{
    // code here
    stack<char>st;
    if(s.size()%2!=0)return false;
    for(char i :s){
        if(i=='(' or  i=='{' or i=='[')
        {
            st.push(i);
        }
        else if(!st.empty() and ((st.top()=='(' && i==')')or (st.top()=='{' && i=='}')or (st.top()=='[' && i==']'))){
            st.pop();
        }
        else return false;
    }
    return(st.empty());
}