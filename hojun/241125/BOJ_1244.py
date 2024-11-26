# 스위치 켜고 끄기

import sys
input = sys.stdin.readline

N = int(input()) # 스위치 개수
states = [0] + list(map(int, input().split())) # 스위치 초기상태
M = int(input()) # 변경 횟수
for _ in range(M):
    s, num = map(int, input().split())
    if s == 1: # 남자인 경우
        cnt = N // num # 변경 가능한 숫자 수
        for i in range(1, cnt+1):
            states[i*num] = 1 - states[i*num] # 숫자 변경
    else: #여자인 경우
        d = 1 # 중앙에서의 거리
        while num-d > 0 and num + d <= N:
            if states[num-d] != states[num+d]: # 대칭 못이루는 경우
                break
            d += 1
        d -= 1
        for i in range(num-d, num+d+1):
            states[i] = 1 - states[i]

for i in range(1, N+1):
    print(states[i], end = " ")
    if i % 20 == 0 :
        print()
