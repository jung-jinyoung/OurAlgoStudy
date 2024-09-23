import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
dp = [[0]*N for _ in range(N)]
for i in range(N):
    dp[i][i]^=1
    if i+1 != N and arr[i]==arr[i+1]:
        dp[i][i+1]^=1

for length in range(3,1 + N):
    for start in range(1+N-length):
        if arr[start] == arr[start+length-1] and dp[start+1][start+length-2]:
            dp[start][start+length-1] = 1
ans = []
for tc in range(int(input())):
    S,E = map(int,input().split())
    ans.append(dp[S-1][E-1])
print(*ans,sep='\n')