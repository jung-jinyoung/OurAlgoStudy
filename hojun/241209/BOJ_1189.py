# 컴백홈 
# 왼쪽 아래 현수 위치, 오른쪽 위 집

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]
N, M, K = map(int, input().split()) # K : 도착 거리
data = [list(input()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
visited[N-1][0] = True

answer = 0


def dfs(i,j,d):
    global answer
    # print(i,j,d)
    if d == K:
        if (i,j) == (0, M-1):
            answer += 1
        return

    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and data[ni][nj] == '.' :
            visited[ni][nj] = True
            dfs(ni, nj, d+1)
            visited[ni][nj] = False
    
dfs(N-1, 0, 1)
print(answer)
