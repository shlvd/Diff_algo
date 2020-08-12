def S(seq, i=0):
    if i == len(seq): return 0
    return S(seq, i+1) + seq[i]


if __name__ == '__main__':
    print(S(range(101)))
