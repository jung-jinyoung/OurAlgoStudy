def pass_fail():                    # 출발점과 도착점이 같은지 체크하는 함수
    for start in range(N):          # 시작점들 모두 순회
        now = start
        for y in range(H):          # 층을 진행하며 선 따라서 이동
            if now >= 1 and arr[y][now-1]:
                now -= 1
            elif now < N-1 and arr[y][now]:
                now += 1
        if start != now:
            return False
    return True

def dfs(cnt,r,c):                   # (놓은 다리 개수,행,열)
    global ans
    if ans<=cnt :
        return
    if pass_fail():                 # 조건 만족하므로 종료
        ans = cnt
        return
    if c>=N:                        # 좌표 조정
        r+=1
        c=0
    x = c                           # 첫 시작은 지금 열에서 아닐때는 0으로 마지막에 초기화
    for i in range(r,H):
        for j in range(x,N-1):
            if not arr[i][j] and arr[i][j+1]==0:
                if j==0 or (arr[i][j-1]==0):
                    arr[i][j] ^= 1
                    dfs(cnt+1,i,j+2)
                    arr[i][j] ^= 1
        x = 0

N, M, H = map(int, input().split())  # N: 세로선, M : 가로선
arr = [[0] * N for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())  # a: 가로선, b-b+1 :세로선 연결
    arr[a-1][b-1] = 1

if pass_fail():
    print(0)
else:
    ans = 4
    dfs(0,0,0)
    if ans == 4:
        ans = -1
    print(ans)