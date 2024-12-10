# 트럭
# 트럭들 무게가 L(최대하중)초과하면 안돼
from collections import deque

N, W, L = map(int, input().split()) # N: 총 차량, W:다리길이, L: 최대하중
truck = deque(list(map(int, input().split())))

cnt = 0 # 다리위 차량 수
weight = 0 # 다리위 차량 무게

w = truck.popleft()
weight += w
time = 1
cnt += 1
on_truck = deque()
on_truck.append((w, time+W)) # (무게, 내릴 시간)
time += 1
while on_truck:
    if on_truck[0][1] == time: #트럭이 내릴 시간인가
        w, t = on_truck.popleft()
        # print(w,t)
        weight -= w
        cnt -= 1
    add = False
    # 차 추가
    if truck and weight + truck[0] <= L and cnt < W: #
        w = truck.popleft() 
        cnt += 1
        weight += w
        on_truck.append((w, time+W))
        add = True
        
    if add:
        if truck:
            time += 1
    else:
        if on_truck:
            # 바로 시간 조정
            time = on_truck[0][1]
print(time)
    