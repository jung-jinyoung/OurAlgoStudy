import sys

sys.stdin = open("input.txt","r")
input = sys.stdin.readline


n =int(input())
# 더미 생성
info = [[0,0]]

for _ in range(n):
    t, p = map(int, input().split(" "))
    info.append([t, p])

dp = [0] * (n+2)

for i in range(n, -1, -1):
    if i + info[i][0] > n + 1 :
        dp[i] = dp[i+1]
    else : 
        dp[i] = max(dp[i+1], info[i][1]+dp[i + info[i][0]])

print(dp[0])