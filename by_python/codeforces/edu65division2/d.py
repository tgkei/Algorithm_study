"""
https://codeforces.com/problemset/problem/1167/D
"""

input()

brackets = list(input())

a = 0
b = 0
result =[]

for bracket in brackets:
    if bracket == '(':
        if a == b:
            a+=1
            result.append("1")
        else:
            b+=1
            result.append("0")
    else:
        if a>b:
            a-=1
            result.append("1")
        else:
            b-=1
            result.append("0")
print("".join(result))





















































"""
#include <set>
#include <string>
#include <vector>
#include <iostream>
using namespace std;
int N; string s; vector<set<pair<int, int> > > sx, sy;
void add(int x, int y) {
	set<pair<int, int>>::iterator it1 = sx[y].lower_bound(make_pair(x + 1, 0));
	set<pair<int, int>>::iterator it2 = it1;
	if (it2 == sx[y].begin()) it2 = sx[y].end();
	else it2--;
	if (it1 != sx[y].end() && it1->first == x + 1) {
		if (it2 != sx[y].end() && it2->second == x) {
			sx[y].insert(make_pair(it2->first, it1->second));
			sx[y].erase(it2);
		}
		else sx[y].insert(make_pair(x, it1->second));
		sx[y].erase(it1);
	}
	else if (it2 != sx[y].end() && it2->second == x) {
		sx[y].insert(make_pair(it2->first, x + 1));
		sx[y].erase(it2);
	}
	else sx[y].insert(make_pair(x, x + 1));
	it1 = sy[x].lower_bound(make_pair(y + 1, 0));
	it2 = it1;
	if (it2 == sy[x].begin()) it2 = sy[x].end();
	else it2--;
	if (it1 != sy[x].end() && it1->first == y + 1) {
		if (it2 != sy[x].end() && it2->second == y) {
			sy[x].insert(make_pair(it2->first, it1->second));
			sy[x].erase(it2);
		}
		else sy[x].insert(make_pair(y, it1->second));
		sy[x].erase(it1);
	}
	else if (it2 != sy[x].end() && it2->second == y) {
		sy[x].insert(make_pair(it2->first, y + 1));
		sy[x].erase(it2);
	}
	else sy[x].insert(make_pair(y, y + 1));
}
int main() {
	int Q;
	cin >> Q;
	for (int rep = 1; rep <= Q; ++rep) {
		int R, C, sr, sc;
		cin >> N >> R >> C >> sr >> sc >> s;
		int x = N, y = N;
		sx.clear();
		sy.clear();
		sx.resize(2 * N + 1); sx[N].insert(make_pair(N, N + 1));
		sy.resize(2 * N + 1); sy[N].insert(make_pair(N, N + 1));
		for (int i = 0; i < N; i++) {
			if (s[i] == 'N' || s[i] == 'S') {
				set<pair<int, int> >::iterator it = --sx[y].lower_bound(make_pair(x + 1, 0));
				if (s[i] == 'S') x = it->second;
				if (s[i] == 'N') x = it->first - 1;
			}
			if (s[i] == 'E' || s[i] == 'W') {
				set<pair<int, int> >::iterator it = --sy[x].lower_bound(make_pair(y + 1, 0));
				if (s[i] == 'E') y = it->second;
				if (s[i] == 'W') y = it->first - 1;
			}
			add(x, y);
		}
		cout << "Case #" << rep << ": " << x - N + sr << ' ' << y - N + sc << endl;
	}
	return 0;
}
"""