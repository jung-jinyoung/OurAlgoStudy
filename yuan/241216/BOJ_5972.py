import heapq

"""
다익스트라 (우선순위큐, 가중치 있는 노드) 

1. 중복 처리 문제 
같은 노드라도 더 짧은 cost 가질 수 있음 
특히 경로 저장할때 중복 경로를 생각하지 않고 모두 가능 경롤 저장했다면
경로나 노드의 중복 처리를 아예 없애고 cost 만 비교함 

2. heap 에 넣는 기준 
다익스트라(우선순위 큐)는 가능한 모든 거리 가는것 x 
시작위치 기준 "최소비용" 거리를 가는 것. 
따라서 저장된 값과 비교해서 비용이 더 적을때만 heapq에 넣어줘야함. 

"""


# 5만 5만
n, m = map(int, input().split())
road = [[] for _ in range(n + 1)]
for _ in range(m):
    # 노드, 가중치 # 양방향
    x, y, c = map(int, input().split())
    # if not road[x] or road[x][0][0]>c:
    road[x].append((c, y))
    # if not road[y] or road[y][0][0]>c:
    road[y].append((c, x))

q = []
now = (0, 1)  # cost, 시작점
heapq.heappush(q, now)

costs = [(1e9)] * (n + 1)
costs[1] = 0  # 시작시 cost

# 노드 1 부터 n 까지 가는데 최소 비용
while q:
    # 현재위치까지의 비용, 현재 위치
    cost, now = heapq.heappop(q)
    for nxt_cst, nxt in road[now]:
        if nxt_cst + cost >= costs[nxt]:
            continue
        costs[nxt] = nxt_cst + cost
        heapq.heappush(q, (costs[nxt], nxt))

print(costs[n])
