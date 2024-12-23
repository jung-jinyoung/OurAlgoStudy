h, w = map(int, input().split())
block = list(map(int, input().split()))
# 가장 큰거 중심으로 l,r 겉 덮기 - block
blocks = sum(block)
max_idx = [idx for idx, x in enumerate(block) if x == max(block)]
# print(max_idx[0])
top = max_idx[0]
total = 0
l = 0
now = block[l]
while l < top:
    b = block[l]
    if now >= b:
        total += now
    else:
        total += b
        now = b
    l += 1

r = w - 1
now = block[r]
while r >= top:
    b = block[r]
    if now >= b:
        total += now
    else:
        total += b
        now = b
    r -= 1
print(total - blocks)
