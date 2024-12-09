import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def bfs(x, y, t) :
    global total, visited
    if x == 0 and y == c-1 :
        if t == k:
            total += 1
        return
    
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 0<= nx < r and 0<=ny<c and not visited[nx][ny]:
            if my_map[nx][ny] == '.':
                visited[nx][ny] = 1
                bfs(nx,ny,t+1)
                visited[nx][ny] = 0
    return
r, c, k = map(int, input().strip().split())
# rxc 맵 거리 k 
my_map = [list(input().strip()) for _ in range(r)]
total = 0 

positions = deque()
visited = [[0]* c for _ in range(r)]
positions.append([r-1, 0, 0])
visited[r-1][0] = 1


directions = [(0,1), (-1,0),(1,0),(0,-1)]
bfs(r-1, 0, 1)

print(total)