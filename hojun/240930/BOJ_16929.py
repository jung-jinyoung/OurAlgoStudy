# Two Dots

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [1,0,0,-1]
dy = [0,1,-1,0]

result = []
def dfs(x, y, prex, prey, cnt ): # x,y: 현위치 prex,prey : 이전위치, cnt : 이동횟수
  if visited[x][y] and cnt >= 4:
    result.append("Yes")
    return 
  visited[x][y]=1
  for idx in range(4):
    nx = dx[idx]+x
    ny = dy[idx]+y
    if 0 <= nx < n and 0 <= ny <m and arr[nx][ny] == arr[x][y]:
      if [nx, ny] != [prex, prey]:
        dfs(nx, ny, x, y, cnt + 1)

for i in range(n):
  for j in range(m):
    if not visited[i][j]:
      dfs(i,j,i,j,0)

if result:
  print("Yes")
else:
  print("No")