def find(x,y,target,level,fin,DP):
    global ans
    if level == fin:                # 성공적으로 도달하면 1리턴
        return 1

    if dp[x][y][level]:             # 이번 자리에 해당 level에서부터 가능한게 저장되어 있으면!
        return dp[x][y][level]

    cnt = 0
    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)):   # 사방 팔방 조사
        nx, ny = (x+dx+n) % n, (y+dy+m) % m                                 # 환형이라고 했으니
        if arr[nx][ny]==target[level]:
            cnt += find(nx,ny,target,level+1,fin,DP)
    dp[x][y][level] = cnt
    return cnt

import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
arr = [input().rstrip() for _ in range(n)]
to_find = [input().rstrip() for _ in range(k)]

# 찾아야하는 단어 순회
for word in to_find:
    ans = 0
    dp = [[[0] * len(word) for __ in range(m)] for _ in range(n)]   # 각 단어 마다 dp만들어서 사용

    # 시작점 돌아
    for i in range(n):
        for j in range(m):
            if word[0]==arr[i][j]:
                ans+=find(i,j,word,1,len(word),dp)
    print(ans)