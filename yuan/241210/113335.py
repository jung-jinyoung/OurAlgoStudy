from collections import deque

# 트럭수1000,다리길이100, 다리 최대하중1000
n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))  # 트럭무게리스트

q = deque()
for _ in range(w):
    q.append(0)  # 다리 길이
t = 0

idx = 0
while idx < n:
    t += 1
    q.popleft()
    if sum(q) + trucks[idx] <= l:
        q.append(trucks[idx])
        idx += 1
    else:
        q.append(0)
print(len(q) + t)
