# 逆元のmod

const = 998244353
def frac(a, b): # a/b
    global const
    return a*pow(b, -1, const)%const