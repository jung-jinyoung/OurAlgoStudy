'''
일단 자기 위치로 다시 돌아오려면 어떤 위치에서 딱접었을 때 대칭이 돼야해
1. 무조건 같은 세로선의 
'''
import sys
from collections import defaultdict
input = sys.stdin.readline

N, M, H = map(int, input().split())

ladder = defaultdict(list)

for _ in range(M): #사다리 개수만큼 반복
  a, b = map(int, input().split())  # 1<=a<=H, 1<=b<=N-1
  ladder[b].append(a)

is_even = [False] * N #세로선 위에 가로선의 개수가 짝수인지 여부
for i in range(1, N):
  if len(ladder[i])%2 == 0:
    is_even[i] = True
print(ladder)
print(is_even)

