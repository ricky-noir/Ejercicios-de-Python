#include <bits/stdc++.h>
using namespace std;

int n;
long long k;
vector<long long> a, b, c;

__int128 superficie(int i, int j, int kk) {
    __int128 ai = a[i], bj = b[j], ckk = c[kk];
    return 2 * (ai*bj + bj*ckk + ckk*ai);
}

long long N;
long long codigo(int i, int j, int kk) {
    return ((long long)i * N + j) * N + kk;
}

struct Estado {
    __int128 superficie;
    long long cod; 
    int i, j, kk;
};


struct Comparador {
    bool operator()(const Estado& x, const Estado& y) const {
        if (x.superficie != y.superficie) return x.superficie < y.superficie;
        return x.cod < y.cod;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> k;
    N = n + 1;

    a.resize(n);
    b.resize(n);
    c.resize(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> b[i];
    for (int i = 0; i < n; i++) cin >> c[i];

    
    int si = n - 1, sj = n - 1, sk = n - 1;

    priority_queue<Estado, vector<Estado>, Comparador> heap;
    set<long long> visitados;

    long long codInicial = codigo(si, sj, sk);
    visitados.insert(codInicial);
    heap.push({superficie(si, sj, sk), codInicial, si, sj, sk});

    int ri = -1, rj = -1, rk = -1;

    for (long long paso = 0; paso < k; paso++) {
        Estado actual = heap.top();
        heap.pop();

        ri = actual.i;
        rj = actual.j;
        rk = actual.kk;

        if (ri > 0) {
            int ni = ri - 1;
            long long nuevoCod = codigo(ni, rj, rk);
            if (visitados.find(nuevoCod) == visitados.end()) {
                visitados.insert(nuevoCod);
                heap.push({superficie(ni, rj, rk), nuevoCod, ni, rj, rk});
            }
        }
        if (rj > 0) {
            int nj = rj - 1;
            long long nuevoCod = codigo(ri, nj, rk);
            if (visitados.find(nuevoCod) == visitados.end()) {
                visitados.insert(nuevoCod);
                heap.push({superficie(ri, nj, rk), nuevoCod, ri, nj, rk});
            }
        }
        if (rk > 0) {
            int nk = rk - 1;
            long long nuevoCod = codigo(ri, rj, nk);
            if (visitados.find(nuevoCod) == visitados.end()) {
                visitados.insert(nuevoCod);
                heap.push({superficie(ri, rj, nk), nuevoCod, ri, rj, nk});
            }
        }
    }

    cout << ri + 1 << " " << rj + 1 << " " << rk + 1 << "\n";

    return 0;
}