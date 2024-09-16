# 스네이크 버드

N, L = map(int, input().split())

fruits = list(map(int, input().split()))

fruit_cnt = dict()
for fruit in fruits:
    if fruit_cnt.get(fruit): #이미 존재 확인한 과일이라면
        fruit_cnt[fruit] += 1
    else:
        fruit_cnt[fruit] = 1

height_list = sorted(fruit_cnt.keys())

for h in height_list:
    if h <= L:
        L += fruit_cnt[h]
    else:
        break
print(L)