def gnomesort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1


def mergesort(seq):
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1: mergesort(lft)
    if len(rgt) > 1: mergesort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res


if __name__ == '__main__':
    lst = [99, 2, 65, 0, 999, 4, 652, 10, 11, 9, 4]
    print(gnomesort(lst))
    print(mergesort(lst))
