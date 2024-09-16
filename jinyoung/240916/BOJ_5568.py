import sys
from itertools import permutations


sys.stdin = open("input.txt", "r")
input= sys.stdin.readline

n = int(input())
k = int(input())

nums = [int(input()) for _ in range(n)]
result = {}
cnt = 0
for comb in permutations(nums,  k):
    now_num = list(comb)
    now = ''.join(map(str,now_num))

    if now in result:
        continue
    result[now] = True


print(len(result.keys()))

