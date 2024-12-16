from collections import defaultdict


def find(str, k):
    dict = defaultdict(list)
    n = len(str)
    mincnt = len(str) + 1
    maxcnt = -1
    check = False
    for idx, i in enumerate(str):
        dict[i].append(idx)
    # print(dict)
    for values in dict.values():
        # print(values) # [1, 7]
        len_v = len(values)
        if len_v >= k:
            for i in range(len_v):
                if (i + k - 1) < len_v:
                    s, e = values[i], values[i + k - 1]
                    # print(str[s:e+1], e-s+1)
                    mincnt = min(mincnt, e - s + 1)
                    maxcnt = max(maxcnt, e - s + 1)
                    check = True

    if check:
        return mincnt, maxcnt
    else:
        return [-1]


t = int(input())
for _ in range(t):
    w = list(input())
    k = int(input())
    print(*find(w, k))
