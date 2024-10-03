# 최단경로
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
start = int(input())
graph = {node:{} for node in range(1, V+1)}
for _ in range(E):
    a, b, c = map(int, input().split())
    if b in graph[a]:
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c

distance = [INF]*(V+1) 

def dijkstra(start):
    distance[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))
    while hq:
        cost_sum, node = heapq.heappop(hq)
        if distance[node] >= cost_sum:
            distance[node] = cost_sum
            for next_node in graph[node]:
                cost = graph[node][next_node]
                if distance[next_node] > cost + cost_sum:
                    distance[next_node] = cost + cost_sum
                    heapq.heappush(hq, (cost+cost_sum, next_node))

dijkstra(start)

for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])