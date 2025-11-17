'''
给一个整数 n,(n <= 10^12)，找出 n 的所有因数中，不包含任何平方数因子（除了1） 的最大那个因数。
(也就是说，找出最大的 Square-free (无平方因子) 因数)。
'''
def max_square_free_divisor(n):
    if n == 1:
        return 1
    result = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            result *= d
            while n % d == 0:
                n //= d
        d += 1
    
    if n > 1:
        result *= n
    
    return result