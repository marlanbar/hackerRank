#include <iostream>
#include <deque>

using namespace std;

void printKMax(int arr[], int n, int k){
    deque<int> d(2);
    for(int i = 0; i < n; i++) {
        int e = arr[i];
        if (d.size() < 2) d.push_back(i);
        if (e >= arr[d.front()]) {
            d.push_front(i);
            if (d.size() > 2) d.pop_back();
        } else if (e >= arr[d.back()]) {
            d.pop_back();
            d.push_back(i);
        }
        if (i + 1 >= k) {
            cout << arr[d.front()] << " ";
            if (i + 1 - k == d.front()) d.pop_front();
            if (i + 1 - k == d.back()) d.pop_back(); 
        }
        
    }
    cout << endl;
}

int main(){
   int t;
   cin >> t;
   while(t>0) {
      int n,k;
       cin >> n >> k;
       int i;
       int arr[n];
       for(i=0;i<n;i++)
            cin >> arr[i];
       printKMax(arr, n, k);
       t--;
     }
     return 0;
}
