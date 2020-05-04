def stair_count(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    x1 = 1
    x2 = 2
    x3 = 4
    i = 4
    while i <= n:
        res = x1 + x2 + x3
        x1 = x2
        x2 = x3
        x3 = res
        i+=1
    return res

    ######
    # if n == 1:
    #     return 1
    # if n ==2: 
    #     return 2
    # return stair_count(n-1) + stair_count(n-2)
    #####
    # def fac(n):
    #     if n == 0:
    #         return 1
    #     return fac(n-1) * n

    
    # res = (fac(n))/(fac(3)*fac(n-3))
    # res += (fac(n))/(fac(2)*fac(n-2))
    # return res

print(stair_count(5))



