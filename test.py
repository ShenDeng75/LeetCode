
def solu(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return solu(n-1) + solu(n-2)


print(solu(4))
