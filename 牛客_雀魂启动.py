
def IShepai(ss):
    lenth = ss.__len__()
    if lenth == 0:
        return True
    count1 = ss.count(ss[0])

    if lenth % 3 != 0 and count1 >= 2 and IShepai(ss[2:]):
        return True
    if count1 >= 3 and IShepai(ss[3:]):
        return True
    if ss[0] + 1 in ss and ss[0] + 2 in ss:
        str1 = ss[1:]
        str1.remove(ss[0] + 1)
        str1.remove(ss[0] + 2)
        if IShepai(str1):
            return True
    return False


if __name__ == '__main__':
    a = input().split(" ")
    a = [int(x) for x in a]

    for i in range(1, 10):
        al = sorted(a + [i])
        if al.count(i) > 4:
            continue
        else:
            if IShepai(al):
                print(i, end=" ")
    print()
