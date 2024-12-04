import heapq

# heapq 에 [0,0] 넣기
# 지름길 확인하기
# 지름길 / 일반길 heapq에 넣어주기
n, d = map(int, input().split())
shortcut = [[] for _ in range(10001)]
total_cost = [(d + 1)] * (10001)

for _ in range(n):
    s, e, c = map(int, input().split())
    shortcut[s].append([e, c])
q = []
heapq.heappush(q, (0, 0))
total_cost[0] = 0  # 시작 cost

while q:
    cost, node = heapq.heappop(q)
    # 지름길 있는경우
    if shortcut[node]:
        for s in shortcut[node]:
            nxt_node, nxt_cost = s[0], s[1]
            # 도착지 벗어나는 지름길은 체크안함 , 현재 total보다 작아야함
            if nxt_node <= d and nxt_cost < total_cost[nxt_node]:
                # 더했을때 작아야함
                if total_cost[node] + nxt_cost <= total_cost[nxt_node]:
                    total_cost[nxt_node] = total_cost[node] + nxt_cost  # 갱신
                    heapq.heappush(
                        q, (total_cost[node] + nxt_cost, nxt_node)
                    )  # 노드 이동
    # 지름길 말고 그냥 길도 추가해주기
    if node < d:
        nxt_node, nxt_cost = node + 1, 1
        # 그냥 길 값 확인
        if total_cost[node] + nxt_cost <= total_cost[nxt_node]:
            total_cost[nxt_node] = total_cost[node] + nxt_cost  # 갱신
            heapq.heappush(q, (total_cost[node] + nxt_cost, nxt_node))  # 노드 이동

print(total_cost[d])
