# this code is incomplete as template.

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
n, m = map(int, input().split())
g = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append([b, c])
    g[b].append([a, c])

used = [False] * n
ans = 0
# sはパスの長さ
def dfs(v, s):
    global used, ans
    used[v] = True
    for i in g[v]:
        if not used[i[0]]:
            dfs(i[0], s+i[1])
    ans = max(s, ans)
    used[v] = False

for i in range(n):
    used = [False] * n
    dfs(i,0)

print(ans)
