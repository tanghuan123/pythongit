def test(n):
    if n == 1:
        return n
    else:
        return n + test(n - 1)

print(test(5))






def test2(n,m=0):
    if n==0:
            return m
    else:
        return test(n-1,m+n)








