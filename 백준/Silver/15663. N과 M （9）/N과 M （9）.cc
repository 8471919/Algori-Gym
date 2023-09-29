#include <bits/stdc++.h>
#define endl "\n"
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define rrep(i, a, b) for(auto i = a; i > b; --i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
#define RREP(i, a, b) for(auto i = a; i >= b; --i)
#define pii pair<int, int>
#define tii tuple<int, int, int>
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define INF numeric_limits<int>::max()
#define PIV (1 << 20)
using namespace std;

#ifdef ONLINE_JUDGE
constexpr bool ndebug = true;
#else
constexpr bool ndebug = false;
#endif
#define FAST_IO \
    if constexpr (ndebug) { cin.tie(nullptr); ios::sync_with_stdio(false); }
#define debug(x) \
    if constexpr (!ndebug) cout << "[DEBUG] " << #x << " == " << x << '\n';
#define debugf(...) \
    if constexpr (!ndebug) { cout << "[DEBUG] "; printf(__VA_ARGS__); }
#define debugc(c) \
    if constexpr (!ndebug) { cout << "[DEBUG] "<< #c << ": "; for (const auto& elem : c) cout << elem << ", "; cout << '\n'; }

typedef long long ll;
typedef unsigned long long ull;

int n, m;
vector<int> vec;
vector<int> temp;
bool visited[10]; // false index에 해당하는 숫자를 사용하지 않음

void f() {
    if (vec.size() == m) {
        rep (i, 0, m) {
            cout << vec[i] << ' ';
        }

        cout << endl;
        return;
    }

    int last = -1;

    rep (i, 0, temp.size()) {
        if (visited[i]) continue;
        // if (!vec.empty() && vec.back() > temp[i]) continue;
        if (last == temp[i]) continue;
        visited[i] = true;
        vec.pb(temp[i]);
        last = temp[i];
        f();
        visited[i] = false;
        vec.pop_back();
    }
}

int main(){
    FAST_IO;
#ifndef ONLINE_JUDGE
    clock_t start = clock();
    freopen("input.txt", "r", stdin);
#endif

    cin >> n >> m;
    temp.resize(n);
    for (auto& e : temp) cin >> e;
    
    sort(temp.begin(), temp.end());
    
    
    f();
    
#ifndef ONLINE_JUDGE
    cout << endl << "elapsed time: " << static_cast<double>(clock() - start) / CLOCKS_PER_SEC << "ms" << endl;
#endif
    return 0;
}
