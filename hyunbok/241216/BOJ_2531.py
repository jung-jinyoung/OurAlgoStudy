from collections import defaultdict
N,D,K,C = map(int,input().split())
arr = [int(input()) for _ in range(N)]
check = defaultdict(int)
check[C]+=1
cnt = 1
for i in range(K):
    if check[arr[i]] == 0:
        cnt+=1
    check[arr[i]]+=1
idx = 1
ans = cnt
for idx in range(1,N):
    check[arr[idx - 1]] -= 1
    if check[arr[idx-1]] == 0:
        cnt-=1

    if check[arr[(idx + K - 1)%N]] == 0:
        cnt+=1
    check[arr[(idx + K - 1)%N]] += 1

    ans = max(ans,cnt)
    if ans == D:
        break
print(ans)