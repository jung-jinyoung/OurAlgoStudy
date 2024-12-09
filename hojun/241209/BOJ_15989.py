# 1, 2, 3 더하기 4 

import sys
input = sys.stdin.readline

dp = [0]*10001
dp[1], dp[2], dp[3] = 1,2,3
for i in range(4, 10001):
     # 1. i-3 번째에서 3만 추가하는 경우
     # 2. 오직 2 혹은 2와 1로만 이루어진 경우
     # 3. 1로만 이루어진 경우
     dp[i] = dp[i-3] + i//2 + 1

N = int(input())
for _ in range(N):
    num = int(input())
    print(dp[num])