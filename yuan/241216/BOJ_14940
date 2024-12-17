from collections import deque

def bfs(q,dist,map):
    while q:
        # map을 -1 방문처리 해가면서 visit 대신 쓰기
        x, y = q.popleft()
        dx,dy = [0,0,1,-1],[1,-1,0,0]

        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<r and 0<=ny<c:
                if map[nx][ny] == 1:
                    map[nx][ny] = -1
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))


q = deque([])
r,c = map(int, input().split())

map = [list(map(int,input().split()))for _ in range(r)]
dist = [[-1]*c for _ in range(r)]

for x in range(r):
    for y in range(c):
        if map[x][y] == 2:
            q.append((x,y))
            dist[x][y] = 0
            map[x][y] = -1
        elif map[x][y] ==0:
            dist[x][y] = 0
bfs(q,dist,map)

for i in dist:
    print(*i)