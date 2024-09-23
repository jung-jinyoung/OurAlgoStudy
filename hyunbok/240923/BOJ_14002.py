import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
dp = [[] for _ in range(n)]
dp[0].append(arr[0])
for i in range(1,n):
    temp = -1
    for j in range(i):
        if arr[i]>arr[j]:
            if temp == -1 or len(dp[temp])<len(dp[j]):
                temp = j
    if temp!=-1:
        dp[i] = dp[temp]+ [arr[i]]
    else:
        dp[i].append(arr[i])
ans = max(dp,key = len)
print(len(ans))
print(*ans)