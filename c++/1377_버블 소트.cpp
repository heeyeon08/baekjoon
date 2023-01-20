#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<pair<int, int>> v;
    int val;

    for (int idx = 0; idx < n; idx++) {
        cin >> val;
        v.push_back(pair<int, int>(val,idx));
    }

    sort(v.begin(), v.end());

    int r = 0;
    for (int i = 0; i < n; i++) {
        if (v[i].second - i > r) {
            r = v[i].second - i;
        }
    }
    
    cout << r + 1 << '\n';

    return 0;
}
