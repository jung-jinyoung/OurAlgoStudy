def dfs(now,visited,cnt):
    global ans
    if ans:
        return
    if cnt == 5:
        ans=1
        return
    for i in arr[now]:
        if visited[i]==0:
            visited[i]^= 1
            dfs(i,visited,cnt+1)
            visited[i]^= 1


N,M = map(int,input().split())
arr = [[] for i in range(N)]
for _ in range(M):
    a,b, = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
ans = 0
v = [0]*N
for node in range(N):
    v[node] ^= 1
    dfs(node,v,1)
    v[node] ^= 1
    if ans:
        break
print(ans)