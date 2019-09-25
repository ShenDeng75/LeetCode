def carry():
    n = int(input())
    for i in range(n):
        s = input()
        res = []
        for e in s:
            if len(res) < 2:
                res.append(e)
                continue
            if len(res) >= 2:
                if e == res[-1] and e == res[-2]:
                    continue
            if len(res) >= 3:
                if e == res[-1] and res[-2] == res[-3]:
                    continue
            res.append(e)
        print("".join(res))


if __name__ == "__main__":
    carry()