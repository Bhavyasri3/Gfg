//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends
class Solution{
    public:
    // You need to complete this function

    // avoid space at the starting of the string in "move disk....."
    long long c = 0;
    void fun(int N,int from,int aux,int to)
    {
        if(N==0)
        {
            return;
        }
        fun(N-1,from,to,aux);
        cout << "move disk " << N << " from rod " << from << " to rod " << to << endl;
        c++;
        fun(N-1,aux,from,to);
    }
    long long toh(int N, int from, int to, int aux) {
        // Your code here
        fun(N,from,aux,to);
        return c;
        
    }

};

//{ Driver Code Starts.

int main() {

    int T;
    cin >> T;//testcases
    while (T--) {
        
        int N;
        cin >> N;//taking input N
        
        //calling toh() function
        Solution ob;
        
        cout << ob.toh(N, 1, 3, 2) << endl;
    }
    return 0;
}



// } Driver Code Ends