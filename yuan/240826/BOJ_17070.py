import sys
sys.setrecursionlimit(10*6)
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# dp 테이블 초기화
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
# dp = [[[0]*3]*N for _ in range(N)] # 이렇게 하면 dp 초기화가 제대로 안됨
# dp[0],dp[1],dp[2]가 같은 값 참조하기 때문
# 따라서 for _ 문으로 dp[0,0,0]을 각각 생성해줘야 함

# dp로 풀경우 [r][c] 에 도착하는 방법수 누적. 가로,세로,대각선 나눠서 계산해줘야함
dp[0][1][0] = 1 # 가로

for r in range(N):
    for c in range(2,N):
        if arr[r][c] ==0:
            if 0<=r-1<N : # 세로: 1
                dp[r][c][1] = dp[r-1][c][1] + dp[r-1][c][2]

            if 0<=r-1<N and 0<=c-1<N and arr[r][c-1]!=1 and arr[r-1][c] !=1 : # 대각선
                dp[r][c][2] = dp[r - 1][c - 1][0] + dp[r - 1][c - 1][1] + dp[r - 1][c - 1][2]

            if 0<=c-1<N : # 가로
                dp[r][c][0] = dp[r][c - 1][0] + dp[r][c - 1][2]

print(sum(dp[N-1][N-1]))

'''
90%에서 통과못함
import sys
sys.setrecursionlimit(10*6)
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

end = [N-1,N-1]
res = 0

# 끝좌표 s=[a,b]
# 가로 이동가능한지 -> 좌표 이동은 s기준
def checkmove0(s):
    # 이동할 가로 좌표
    s_r, s_c = s[0], s[1]+1
    if 0<= s_r < N and 0<= s_c <N:
        if arr[s_r][s_c] ==0: # 빈칸 확인
            return True
    return False

#세로이동 가능한지
def checkmove1(s):
    # 이동할 세로 좌표
    s_r, s_c = s[0]+1,s[1]
    if 0<= s_r < N and 0<= s_c <N:
        if arr[s_r][s_c] ==0: # 빈칸 확인
            return True
    return False

# 대각선 이동가능한지
def checkmove2(s):
    # 이동할 대각선 좌표
    s_r, s_c = s[0]+1,s[1]+1
    if 0<= s_r < N and 0<= s_c <N:
        if arr[s[0]+1][s[1]] == 0 and arr[s[0]][s[1]+1] ==0 and arr[s_r][s_c] ==0: # 빈칸 확인
            return True
    return False


# state 0:가로 1:세로 2: 대각선
# f는 앞좌표 s는 뒷좌표
def find(state, s):
    global res

    # 도달했을때 방법 추가
    if s == end:
        res +=1
        return
    else:
        if state ==0: # 가로일때 가로,대각 이동
            if checkmove0(s):
                find(0,[s[0],s[1]+1] )
            if checkmove2(s):
                find(2, [s[0]+1, s[1] + 1])
        elif state ==1: # 세로일때 세로, 대각이동
            if checkmove1(s):
                find(1, [s[0]+1, s[1]])
            if checkmove2(s):
                find(2, [s[0] + 1, s[1] + 1])
        else: # 대각선일때 가로,세로,대각 이동
            if checkmove0(s):
                find(0, [s[0], s[1]+1])
            if checkmove1(s):
                find(1, [s[0] + 1, s[1]])
            if checkmove2(s):
                find(2, [s[0] + 1, s[1] + 1])
    return
find(0,[0,1])
print(res)
'''