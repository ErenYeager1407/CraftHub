#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define ff first
#define ss second
#define pb push_back
#define vl vector<long long>
#define vi vector<int>
#define vvi	vector<vector<int>>
#define vvl	vector<vector<long long>>
#define all(a) (a.begin(), a.end())
#define nl	endl
#define dbg(x)	cout << #x << "->" << x << endl
#define dbgloop(a)  for(auto&x : a) cout << x << " ";
#define pi pair<int,int>
#define pl pair<long long , long long>
#define um unordered_map

int main()
{
    int test;
    cin >> test;
    while(test--){
		int n;
		cin >> n;
		int ans =  0;
		ans = ans + n/10 + n%10;
		cout << ans << endl;
	}
}
