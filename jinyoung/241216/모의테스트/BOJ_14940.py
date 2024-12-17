import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().strip().split())

my_map = [ list(map(int,input().strip().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

my_arr = deque()

def find_start(arr):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                return i, j
            
si, sj = find_start(my_map)

my_arr.append([si, sj])
visited[si][sj] = 0 
directions = [(1,0),(0,1),(-1,0),(0,-1)]
while my_arr:
    i, j = my_arr.popleft()
    for di, dj in directions : 
        ni = i + di
        nj = j + dj 
        # 범위에 벗어나지 않고 방문하지 않았으면 
        if (0<=ni<n and 0<=nj<m) and visited[ni][nj] < 0 :
            if my_map[i][j] != 0:
                visited[ni][nj] = visited[i][j] + 1
                my_arr.append([ni,nj])

for i in range(n):
    for j in range(m):
        if my_map[i][j] == 0 :
            visited[i][j] = 0 
    print(*visited[i])