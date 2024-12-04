# 절댓값 힙

import sys
import heapq
input = sys.stdin.readline

N = int(input())
hq = []
for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(hq, (abs(x), x))
    else:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)