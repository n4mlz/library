def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    pass


def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


# ---------------------------------------------------------------

# ソート済みのリストdataからvalueと一致するものを探す
def binary_search(data, value):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value:
            return mid
        elif data[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return None # 見つからなかった場合(適当に変更する)


# func(x)=valueとなるxを探す(funcが簡単に計算できる場合), rightは答えの取りうる最大値
def binary_search(func, value, right):
    left = 0
    while left <= right:
        mid = (left + right) // 2
        if func(mid) == value:
            return mid
        elif func(mid) < value:
            left = mid + 1
        else:
            right = mid - 1
    return None # 見つからなかった場合(適当に変更する)

