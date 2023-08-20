# ================
# 再帰延ばす
# ================

import sys
sys.setrecursionlimit(10**9)

# ================
# inputを高速化
# ================

import sys
input = sys.stdin.readline

# ================
# map
# ================

# リストのそれぞれの要素に関数を適用

l = [-2, -1, 0]
print(map(abs, l))
# <map object at 0x10651a400>

print(list(map(abs, l)))
# [2, 1, 0]



# ================
# zip
# ================

# 複数のリストのn個目の要素の組を取得

names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]
for name, age in zip(names, ages):
    print(name, age)
# Alice 24
# Bob 50
# Charlie 18

# 複数のイテラブルの要素をタプルにまとめたリストを取得

names = ['Alice', 'Bob', 'Charlie']
ages = (24, 50, 18)
l = list(zip(names, ages))
print(l)
print(type(l))
print(type(l[0]))
# [('Alice', 24), ('Bob', 50), ('Charlie', 18)]
# <class 'list'>
# <class 'tuple'>



# ================
# 転置リスト
# ================

A = [[1, 2], [3, 4], [5, 6]]
print(list(zip(*A)))
# [(1, 3, 5), (2, 4, 6)]



# ================
# filter
# ================

# 条件に合うものを抽出

l = [-2, -1, 0, 1, 2]
print(filter(lambda x: x % 2 == 0, l))
# <filter object at 0x10bb38580>

print(list(filter(lambda x: x % 2 == 0, l)))
# [-2, 0, 2]

# 複数条件(and, or)

l = [-2, -1, 0, 1, 2]
print(list(filter(lambda x: x % 2 == 0 and x > 0, l)))
# [2]

print(list(filter(lambda x: x % 2 == 0 or x > 0, l)))
# [-2, 0, 1, 2]

# 同様の動作を内包表記でも可能

l = [-2, -1, 0, 1, 2]
print([x for x in l if x % 2 == 0])
# [-2, 0, 2]



# ================
# join
# ================

# リストの要素(str)を任意の文字列を間に入れて連結

s = ["A", "B", "C", "D"]
print("->".join(s))
# A->B->C->D

# str以外の場合

print("".join(map(str, [0,90,1234,5678])))
# 09012345678

# 文字列の間に文字を入れる

print("・".join("ひみつ"))
# ひ・み・つ

# 文字列をreverse()
def  s_reverse(string):
    s_reversed = ''.join(list(reversed(string)))
    return s_reversed



# ================
# sort
# ================

# keyを指定して任意の要素でソート

a = [
    [1,7,'z'],
    [3,2,'x'],
    [1,8,'r'],
    [2,2,'s'],
    [1,9,'b'],
    [2,2,'a']
    ]
print(sorted(a, key=lambda x:x[2]))
#(文字でソートされる)


# ================
# copy
# ================

# 1次元リストは基本的にコピー

a = [1,2]
b = a
a = []
print(b)
# [1, 2]


# ================
# bisect
# ================

# aにxを追加するとしたらどのindexになるか

import bisect
a = [1, 2, 4, 5, 5, 6]

# bisect
# xがaに元からある数字なら右側に追加したときのindex
# (x以下となる最大のindex)+1 とも解釈可能
print(bisect.bisect(a, 0))
# 0
print(bisect.bisect(a, 2))
# 2
print(bisect.bisect(a, 3))
# 2
print(bisect.bisect(a, 5))
# 5

# bisect_left: xがaに元からある数字なら左側に追加したときのindex
# x以上となる最小のindex とも解釈可能
print(bisect.bisect_left(a, 0))
# 0
print(bisect.bisect_left(a, 2))
# 1
print(bisect.bisect_left(a, 3))
# 2
print(bisect.bisect_left(a, 5))
# 3