arr = [-1, -2, 1, -5]

le = len(arr)
su = 0
ma = 0
for i in range(le):
    ma = max(su, su+arr[i])
    su += arr[i]
    if su < 0:
        su = 0

print(ma)


