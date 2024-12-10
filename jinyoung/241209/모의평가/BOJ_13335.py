import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 다리를 건너는 트럭의 수 n 다리 길이 w 최대 하중 l
n, w, l = map(int, input().strip().split())
# 트럭 하중 리스트
trucks = deque(map(int, input().strip().split()))
bridge = deque([0] * w)
time = 0

while bridge :
    time += 1
    bridge.popleft()
    if trucks:
        if sum(bridge) + trucks[0] <= l :
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
print(time)