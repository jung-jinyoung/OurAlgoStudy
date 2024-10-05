from collections import deque

def dfs(fis_s,fis_e,x,y,cnt):
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0<=nx<r and 0<= ny<c:
            if nx == fis_s and ny==fis_e and cnt>=3:
                print('Yes')
                exit()
            if graph[nx][ny] == graph[x][y] and not visit[nx][ny]:
                visit[nx][ny] = 1
                dfs(fis_s,fis_e,nx,ny,cnt+1)
                visit[nx][ny] = 0

r, c = map(int, input().split())
dx, dy = [0,0,1,-1], [1,-1,0,0]
graph = [list(input()) for _ in range(r)]
visit = [[ 0 for _ in range(c)] for _ in range(r)]

for i in range(r):
    for j in range(c):
        if not visit[i][j]:
            visit[i][j] = 1
            dfs(i,j,i,j,1)
print('No')