n, m = [int(x) for x in input().split()] # nは頂点の数、mは辺の数
g = [[] for _ in range(n)] # 隣接リスト

for _ in range(m):
    a, b = [int(x) for x in input().split()]
    g[a].append(b)
    g[b].append(a)


# uからの各頂点の距離をreturn
from collections import deque
def bfs(u):
    queue = deque([u])
    d = [None] * n
    d[u] = 0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d


# 0からの各頂点の距離(たどり着けない頂点はNone)
d = bfs(0)
print(d)