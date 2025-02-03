from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    trucks = deque(truck_weights)
    bridge = deque([0] * bridge_length) 
    
    current_weight = 0
    while bridge :
        time += 1
        # 무게 만큼 빼기
        current_weight -= bridge.popleft()
        
        if trucks :
            if current_weight + trucks[0] <= weight :
                truck = trucks.popleft()
                bridge.append(truck)
                current_weight += truck
            else :
                bridge.append(0)
        
    return time