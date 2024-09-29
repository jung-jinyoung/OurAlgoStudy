# 최소비용 구하기

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N = int(input())  # 도시의 개수
M = int(input())  # 버스의 개수
costs = {i:{} for i in range(1, N+1)}
for _ in range(M):
  a, b, c = map(int, input().split())
  if b in costs[a]:
    costs[a][b] = min(costs[a][b], c) # a에서 b로 가는 비용 최소화
  else:
    costs[a][b] = c

def dijkstra(s, e):
  distance = {node:INF for node in costs}
  distance[s] = 0 # 초기 비용 0
  hq = [(0, s)]
  while hq:
    cost, node = heapq.heappop(hq)
    if node == e:
      return cost
    
    if cost <= distance[node]: 
      distance[node] = cost
      for next_node, c in costs[node].items():
        # 도착 가능 비용 낮은 경우에만
        if cost + c < distance[next_node]:
          distance[next_node] = cost + c
          heapq.heappush(hq, (cost+c, next_node))

start, end = map(int, input().split())
print(dijkstra(start, end))