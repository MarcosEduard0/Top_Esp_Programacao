#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void solve(){
	string s;
	cin >> s;
	int n = s.size();
	int ans = n;
	for(int i=0;i<n;i++){
		for(int j=i+1;j<n;j++) {
			int num = (s[i]-'0')*10 + (s[j]-'0');
			if (num%25 == 0) {
				ans = min(ans, (j-i-1) + (n-1-j));
			}
		}
	}
	cout<<ans<<"\n";
}
                
int main(){
    ios::sync_with_stdio(0);
            cin.tie(0);
            cout.tie(0);
            cout<<fixed;
            cout<<setprecision(10);
            int t=1;
            cin>>t;
            for(int i=1;i<=t;i++){
                solve();
    }
    return 0;
}