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

// 벡터 v에 순열의 결과를 담고 출력
vector<int> v;

int visited[10];



void permutation(int n, int m) {
	// 재귀 종료 조건
	if (v.size() == m) {
		for (int i = 0; i < m; i++) {
			cout << v[i] << " ";
		}
		cout << endl;
		return;
	}

	// 순열은 1부터 뽑기 때문에 1부터 n까지 반복
	for (int next = 1; next <= n; next++) {
		// 만약 해당 숫자를 방문했다면, 이미 벡터 v에 들어있는 것이므로 continue;
		if (visited[next]) {
			continue;
		}

		// 방문 안했다면, 지금 방문했으므로 true로 설정
		visited[next] = true;
		// 그리고 v에 현재 값을 push한다.
		v.push_back(next);
		// 그리고 다음 값을 뽑기 위해 재귀
		permutation(n, m);
		// 또 다음 순열을 뽑아야 하기 때문에 현재 방문한 노드를 지워준다.
		visited[next] = false;
		v.pop_back();
	}
	
}


int main(){
    FAST_IO;
    int n, m;
    cin >> n >> m;
    permutation(n, m);
    return 0;
}