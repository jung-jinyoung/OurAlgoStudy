'''
dfs vs bfs vs dp vs dijkstra 
1) dfs: 재귀로 문제 풀어야 할때 
    -> 문제의 최적해가 하위문제들의 최적해일때 dp
2) bfs: 최단거리 최적해 찾을때 
    -> 거리별 가중치가 있는 경우 다익스트라 

'''
import heapq

t = 1
dx,dy=[1,-1,0,0],[0,0,1,-1]
def diek(arr,cost,visit,heap):
    while heap:
        c, now = heapq.heappop(heap)
        x,y = now[0],now[1]
        # 다음 갈 수 있는 노드 확인
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny]:
                # 비교할필요도 없으면
                if cost[nx][ny] < arr[nx][ny]:
                    continue
                # 비교해야하는 경우
                if cost[nx][ny] > c+arr[nx][ny]:
                    cost[nx][ny] = c+arr[nx][ny]
                    heapq.heappush(heap,(c+arr[nx][ny], (nx,ny)))
                visit[nx][ny] = 1

while True:
    n = int(input())
    if n ==0:
        exit()
    arr = [ list(map(int,input().split())) for _ in range(n)]
    cost = [ [1e9]*n for _ in range(n)]
    visit = [[0]*n for _ in range(n)]
    heap = [(arr[0][0],(0,0))] # 현재노드까지의 c, 현재 노드

    diek(arr,cost,visit,heap)

    print(f'Problem {t}: {cost[n-1][n-1]}')
    t+=1


