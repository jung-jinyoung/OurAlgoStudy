def dfs(jump,c,ni,nj,v):
    global check
    if check:
        return
    for nx, ny in ((ni + 1, nj), (ni, nj + 1), (ni - 1, nj), (ni, nj - 1)):
        if 0 <= nx < N and 0 <= ny < M and v[nx][ny]==2:
            if jump>=4:
                check = True
            return
        elif 0 <= nx < N and 0 <= ny < M and v[nx][ny] == 0 and arr[nx][ny] == c:
            v[nx][ny]^=1
            dfs(jump+1,c,nx,ny,v)
from sys import stdin
input = stdin.readline
N,M = map(int,input().split())
arr = list(input().rstrip() for _ in range(N))
check = False
for i in range(N):
    for j in range(M):
        cnt = 0
        for x,y in ((i+1,j),(i,j+1),(i-1,j),(i,j-1)):
            if 0<=x<N and 0<=y<M and arr[i][j]==arr[x][y]:
                cnt+=1
        if cnt>=2:
            visited =[[0]*M for _ in range(N)]
            visited[i][j]=2
            dfs(1,arr[i][j],i,j,visited)
            if check:
                break
    if check:
        break
print("Yes" if check else "No")