from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n  # 各要素の親要素の番号を格納するリスト. 要素が根(ルート)の場合は-(そのグループの要素数)を格納する

    def find(self, x):  # 要素xが属するグループの根を返す ほぼ O(1)
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):  # 要素xが属するグループと要素yが属するグループとを併合する ほぼ O(1)
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):  # 要素xが属するグループのサイズ(要素数)を返す
        return -self.parents[self.find(x)]

    def same(self, x, y):  # 要素x, yが同じグループに属するかどうかを返す
        return self.find(x) == self.find(y)

    def members(self, x): # 要素xが属するグループに属する要素をリストで返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):  # すべての根の要素をリストで返す
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):  # グループの数を返す
        return len(self.roots())

    def all_group_members(self):  # {ルート要素: [そのグループに含まれる要素のリスト], ...}のdefaultdictを返す
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):  # print()での表示用. ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


# uf = UnionFind(6)
# print(uf.parents)
# # [-1, -1, -1, -1, -1, -1]
