from collections import deque



di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
def solution(land):
    N = len(land)
    M = len(land[0])
    amount = [0]*M #각 위치의 시추량
    
    for i in range(N):
        for j in range(M):
            if land[i][j]:
                cnt, pos_list = bfs(i, j, land, N, M)
                for pos in pos_list:
                    amount[pos] += cnt
    print(amount)
    return max(amount)

def bfs(x, y, land, N, M):
    queue = deque()
    pos = set()
    queue.append((x,y))
    cnt = 0
    while queue:
        i, j = queue.popleft()
        land[x][y] = 0
        cnt += 1
        pos.add(j)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni <N and 0 <= nj <M and land[ni][nj]:
                land[ni][nj] = 0
                queue.append((ni, nj))
                

    return cnt, pos