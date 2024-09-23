# 두 수의 합

n = int(input())  # 숫자 개수
nums = list(map(int, input().split()))

# dp[0]은 제거 없이 연속으로 큰 경우, dp[1]은 한 개를 제거한 경우
dp = [[0] * n for _ in range(2)]

dp[0][0] = nums[0]
dp[1][0] = nums[0]

# 연속해서 더해보기 
for i in range(1, n):
    dp[0][i] = max(nums[i], dp[0][i-1] + nums[i])  # 제거 없이 연속
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + nums[i])  # 하나 제거

# 결과 출력
print(max(max(dp[0]), max(dp[1])))
