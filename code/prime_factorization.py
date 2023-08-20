def factorization(num):
    if num == 2:
        return [2]
    tmp_num = num
    ret = []
    for i in range(2, int(num**0.5)+1):
        while tmp_num % i == 0:
            tmp_num //= i
            ret.append(i)
    if tmp_num != 1:
        ret.append(tmp_num)
    return ret