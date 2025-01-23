import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

dp = [[0] * n for _ in range(n)]

# 길이 1인 경우
for i in range(n):
    dp[i][i] = 1

# 길이 2인 경우
for i in range(n-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1

# 길이 3 이상인 경우
for length in range(3, n+1):
    for start in range(n-length+1):
        end = start + length - 1
        if arr[start] == arr[end] and dp[start+1][end-1]:
            dp[start][end] = 1

for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])