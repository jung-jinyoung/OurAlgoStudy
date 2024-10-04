import sys
import heapq
input = sys.stdin.readline

V,E = map(int,input().split())
graph = [ [] for _ in range(V+1)]
root = int(input()) # 시작노드
ans = [ 1e9 for _ in range(V+1)] # 최단거리 저장할 배열
ans[root] = 0 # 시작노드는 0
heap = [[0,root]]# heap에 cost, 시작노드 저장
for _ in range(E):
    s,e,cost = map(int, input().split())
    graph[s].append([cost,e])
    # heapq.heappush(heap,[cost,(s,e)])

while heap:
    cost , now = heapq.heappop(heap) #최단거리 가는 노드
    for next in graph[now]: # 현재 노드 기준으로 갈수있는 노드 확인
        next_cost, next_node = next[0], next[1]
        if next_cost > ans[next_node]:
            continue # 가중치부터 커버리면 pass
        if ans[now]+next_cost < ans[next_node]:
            mincost = ans[now]+next_cost
            ans[next_node] = mincost
            heapq.heappush(heap,[mincost,next_node])

for num in range(1,V+1):
    if ans[num] == 1e9:
        print('INF')
    else:
        print(ans[num])