//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends
class Solution{
    public:
    // You need to complete this function
    
        int count = 0;
    
    // Function to solve Tower of Hanoi problem
    long long toh(int N, int from, int to, int aux) {
        if (N == 0) {
            return count; // Return 0 if there are no disks to move
        }
        
        toh(N-1, from, aux, to); // Move N-1 disks from 'from' to 'aux' using 'to' as auxiliary
        cout << "move disk " << N << " from rod " << from << " to rod " << to << endl;
        count++; // Increment the count for each move made
        toh(N-1, aux, to, from); // Move N-1 disks from 'aux' to 'to' using 'from' as auxiliary
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