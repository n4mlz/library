# n進法展開 O(log n)

# numを基数rで表す
def radix(num, rad):
    ret_list = []
    q = num
    while q:
        q, r = divmod(q, rad)
        ret_list.append(r)
    return ret_list

# 使用法
# print(radix(27, 4))
# [3, 2, 1]  # ※n番目は4^nの桁 27 = 3*1 + 2*4 + 1*16