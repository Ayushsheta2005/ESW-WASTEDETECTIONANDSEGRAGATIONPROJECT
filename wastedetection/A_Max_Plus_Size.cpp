#include <bits/stdc++.h>
using namespace std;

#define MOD 1000000007
#define ll long long
#define ld long double
#define vec vector<int>
#define vll vector<ll>
#define pii pair<int, int>
#define pll pair<ll, ll>
#define umap unordered_map
#define uset unordered_set
#define fast_io ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sz(x) (int)x.size()
#define rep(i, a, b) for (int i = a; i < b; ++i)
#define repr(i, a, b) for (int i = a; i >= b; --i)
#define trav(a, x) for (auto &a : x)
#define endl '\n'

template <typename T>
void print_vec(const vector<T>& v);
template <typename T1, typename T2>
void print_pair(const pair<T1, T2>& p);
ll mod_exp(ll x, ll y, ll m);
ll mod_inv(ll n, ll m);
ll nCr(ll n, ll r, ll m);
bool is_prime(ll n);
void sieve(vector<bool>& primes, int n);
ll sum_of_digits(ll n);
ll factorial(ll n);
bool is_power_of_two(ll n);
ll binary_to_decimal(string s);
string decimal_to_binary(ll n);
vector<string> split_string(const string& s, char delimiter);
ll merge_mod(ll a, ll b, ll m);
ll mul_mod(ll a, ll b, ll m);
ll sub_mod(ll a, ll b, ll m);
ll sum(vector<ll>& v);
vector<ll> prefix_sum(vector<ll>& v);

int main() {
    fast_io

    int t;
    cin >> t;
    while (t--) 
    {
        int a;
        cin >> a;
        vector<vector<int>> v(a, vector<int>(a));
    }
    return 0;
}

// Function Definitions

template <typename T>
void print_vec(const vector<T>& v) {
    for (const auto& el : v) {
        cout << el << ' ';
    }
    cout << endl;
}

template <typename T1, typename T2>
void print_pair(const pair<T1, T2>& p) {
    cout << p.ff << ' ' << p.ss << endl;
}

ll mod_exp(ll x, ll y, ll m) {
    ll res = 1;
    x = x % m;
    while (y > 0) {
        if (y & 1) res = (res * x) % m;
        y = y >> 1;
        x = (x * x) % m;
    }
    return res;
}

ll mod_inv(ll n, ll m) {
    return mod_exp(n, m - 2, m);
}

ll nCr(ll n, ll r, ll m) {
    if (r > n) return 0;
    ll p = 1, k = 1;
    r = min(r, n - r);
    while (r) {
        p = (p * n) % m;
        k = (k * r) % m;
        n--; r--; 
    }
    return (p * mod_inv(k, m)) % m;
}

bool is_prime(ll n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (ll i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    return true;
}

void sieve(vector<bool>& primes, int n) {
    primes.assign(n + 1, true);
    primes[0] = primes[1] = false;
    for (int i = 2; i * i <= n; i++) {
        if (primes[i]) {
            for (int j = i * i; j <= n; j += i) {
                primes[j] = false;
            }
        }
    }
}

ll sum_of_digits(ll n) {
    ll sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

ll factorial(ll n) {
    ll result = 1;
    for (ll i = 2; i <= n; ++i) {
        result = (result * i) % MOD;
    }
    return result;
}

bool is_power_of_two(ll n) {
    return n && (!(n & (n - 1)));
}

ll binary_to_decimal(string s) {
    ll result = 0;
    ll base = 1;
    for (int i = s.length() - 1; i >= 0; --i) {
        if (s[i] == '1') {
            result += base;
        }
        base *= 2;
    }
    return result;
}

string decimal_to_binary(ll n) {
    string result;
    while (n > 0) {
        result.pb((n % 2) + '0');
        n /= 2;
    }
    reverse(all(result));
    return result;
}

vector<string> split_string(const string& s, char delimiter) {
    vector<string> result;
    stringstream ss(s);
    string item;
    while (getline(ss, item, delimiter)) {
        result.pb(item);
    }
    return result;
}

ll merge_mod(ll a, ll b, ll m) {
    return (a % m + b % m) % m;
}

ll mul_mod(ll a, ll b, ll m) {
    return ((a % m) * (b % m)) % m;
}

ll sub_mod(ll a, ll b, ll m) {
    return ((a % m - b % m) + m) % m;
}

ll sum(vector<ll>& v) {
    ll result = 0;
    for (const auto& el : v) {
        result += el;
    }
    return result;
}

vector<ll> prefix_sum(vector<ll>& v) {
    vector<ll> result;
    result.pb(v[0]);
    for (int i = 1; i < sz(v); ++i) {
        result.pb(result[i - 1] + v[i]);
    }
    return result;
}