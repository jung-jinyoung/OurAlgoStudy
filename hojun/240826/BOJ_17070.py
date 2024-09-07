# 파이프 옮기기 1
import sys
input = sys.stdin.readline

# 아래쪽 갈 수 있는 확인
def down_check(i,j):
  if 0 < i < N and not data[i][j]:
    return True
  return False

# 오른쪽 아래 갈 수 있는지 확인
def down_right_check(i,j):
  if 0 < i < N and 0 < j < N and not (data[i][j] or data[i-1][j] or data[i][j-1]):
    return True
  return False

# 오른쪽 갈 수 있는지 확인
def right_check(i,j):
  if 0 < j < N and not data[i][j]:
    return True
  return False


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0,0,0] for _ in range(N)] for _ in range(N)] # 3차원 배열 dp 생성 0:오른쪽, 1: 오른쪽아래, 2: 아래
dp[0][1][0] = 1 # 초기 케이스 : 0행 1열 오른쪽 방향으로 가는 경우
for i in range(N):
  for j in range(2, N): #1열까지는 쓸모없음..
    if right_check(i, j):
      dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][1] #왼쪽 위치에서 올 수 있는 경우의 수 더하기

    if down_right_check(i, j):
      dp[i][j][1] += sum(dp[i-1][j-1]) #이전의 모든 경우 가능

    if down_check(i, j):
      dp[i][j][2] += dp[i-1][j][1] + dp[i-1][j][2]

print(sum(dp[N-1][N-1]))