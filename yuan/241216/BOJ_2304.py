n = int(input())
loc = dict()
for _ in range(n):
    idx, h = map(int, input().split())
    loc[idx] = h

max_idx = [k for k, v in loc.items() if v == max(loc.values())]
top = max_idx[0]

l = min(loc)
r = max(loc)

res = 0
now = loc[l]
while l <= top:
    if l in loc:
        nxt = loc[l]
        if nxt > now:
            res += nxt
            now = nxt
        else:
            res += now
    else:
        res += now
    # print(l, now, res)
    l += 1

now = loc[r]
while r > top:
    if r in loc:
        nxt = loc[r]
        if nxt > now:
            res += nxt
            now = nxt
        else:
            res += now
    else:
        res += now
    # print(r,now,res)
    r -= 1

print(res)
