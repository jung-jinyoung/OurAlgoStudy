# [다리를 지나는 트럭](https://school.programmers.co.kr/learn/courses/30/lessons/42583)

## 초기 풀이
92.9/100
시간 초과
```python
from collections import deque

def solution(bridge_length, weight, truck_weights):
    N = len(truck_weights)
    # 트럭이 이동해야 하는 거리 쉽게 생각하기 위해 없는 부분 0으로 채우기
    bridge = deque([0]*bridge_length) 
    idx = 0 # 현재 트럭 인덱스
    time = 0
    while idx < N:
        # 일단 현재 트럭을 뺀다(그냥 공기일 수도 있음)
        bridge.popleft()
        if sum(bridge) + truck_weights[idx] <= weight:
            bridge.append(truck_weights[idx])
            idx += 1
        else:
            bridge.append(0)
        time += 1
    
    # 다리 위 가장 마지막 트럭이 오는 시간까지 추가
    for i, truck in enumerate(bridge):
        if truck:
            last = i+1
    time += last
    
    return time
```

## 다시 푼 방법

time을 1초씩 증가시키면서 확인하는 것은 시간초과가 발생하므로 차가 더 못 들어가는 상황에서는 바로 차가 나올 수 있는 시간대로 이동해서 시간을 줄였음

```python
from collections import deque

def solution(bridge_length, weight, truck_weights):
    N = len(truck_weights)
    bridge = deque() 
    idx = 0 # 현재 트럭 인덱스
    exit_time = deque()
    time = 1
    while idx < N:
        
        # 나갈 수 있는 트럭 있으면 나가기
        if exit_time:
            if time >= exit_time[0]:
                truck = bridge.popleft()
                et = exit_time.popleft()
                print('truck =', truck, 'exit_time =',et)
                
        if sum(bridge) + truck_weights[idx] <= weight:
            bridge.append(truck_weights[idx])
            exit_time.append(time + bridge_length)
            time += 1
            idx += 1
        else:
            time = exit_time[0]
        
    # 다리 위 가장 마지막 트럭이 오는 시간까지 추가
    answer = exit_time[-1]
    
    return answer
```