import sys

sys.stdin = open("input.txt" ,"r")
input = sys.stdin.readline

N= int(input())
my_map = [[*map(int,input().split())] for _ in range(N)]
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]

# dp[0][row][col] : 가로로 이동
# dp[1][row][col] : 세로로 이동
# dp[2][row][col] : 대각선으로 이동 

# 첫째줄 미리 처리 
dp[0][0][1] = 1
for j in range(2,N):
    if my_map[0][j] == 0:
        # 벽이 아니라면 가로로 이동 가능
        dp[0][0][j]= dp[0][0][j-1]
        # dp[0][0][j] = 1 
        # 첫째줄에 벽이 있는 경우의 수 생각 못해서 틀렸음 

for r in range(1,N):
    for c in range(1,N):
        if my_map[r][c] == 0:
            # 대각선 파이프 추가
            if my_map[r-1][c-1]==0 and my_map[r][c-1] == 0 and my_map[r-1][c] == 0:
                # 4칸 모두 벽이 아닐 경우 : r-1,c-1 를 파이프 끝으로 두는 모든 경우의 수 
                dp[2][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]

            if my_map[r][c-1] == 0 :
                # 가로 파이프 : r,c-1를 파이프 끝으로 두는 가로 + 대각선
                dp[0][r][c] = dp[0][r][c-1] + dp[2][r][c-1]
            if my_map[r-1][c] ==0 :
                # 세로 파이프 : r-1, c를 파이프 끝으로 두는 세로 + 대각선
                dp[1][r][c] = dp[1][r-1][c] + dp[2][r-1][c]
    
result = dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1]
print(result)

