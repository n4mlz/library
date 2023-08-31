# this code is incomplete as template.
n, m = [int(x) for x in input().split()]
g = [[] for _ in range(n)]

for _ in range(m):
    st, gl, ds = [int(x) for x in input().split()]
    g[st].append([ds, gl])
    g[gl].append([ds, st])

import heapq
def dijkstra(u):
    distances = [10**10] * n
    distances[u] = 0
    q = [[0, u]]
    while q:
        n_d, n_v = heapq.heappop(q)
        if n_d > distances[n_v]:
            continue
        for v in g[n_v]:
            d_tmp = n_d + v[0]
            if distances[v[1]] > d_tmp:
                distances[v[1]] = d_tmp
                heapq.heappush(q, [d_tmp, v[1]])
    return distances