# 逆元のmod

const = 998244353
def frac(num1, num2): # num1 / num2
    global const
    return num1 * pow(num2, -1, const) % const