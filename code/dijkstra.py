# import heapq

# g = [[] for _ in range(16)]
# for _ in range(24):
#     _s, _g, _d = map(int, input().split())
#     g[_s].append([_d, _g])
#     g[_g].append([_d, _s])

# def dijkstra():
#     d = [10**10] * 16
#     d[0] = 0
#     q = [[0, 0]]
#     while q:
#         n_d, n_v = heapq.heappop(q)
#         if n_d > d[n_v]:
#             continue
#         for v in g[n_v]:
#             tmp = n_d + v[0]
#             if d[v[1]] > tmp:
#                 d[v[1]] = tmp
#                 heapq.heappush(q, [tmp, v[1]])
#     return d

# ans = dijkstra()
# print(f'ans:{ans[15]}')