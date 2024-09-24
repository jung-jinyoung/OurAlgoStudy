import sys
input = sys.stdin.readline

def check(length):
    cnt = 1
    last = data[0]
    for datum in data:
        if datum - last >= length:
            last = datum
            cnt += 1
            if cnt >= C:
                return True
    return False

N, C = map(int, input().split())
data = sorted(list(int(input()) for _ in range(N)))

l = 1
r = r = data[-1] - data[0]

result = 1
while l <= r:
    m = (l+r)//2
    if check(m):
        result = m
        l = m + 1
    else:
        r = m - 1

print(result)