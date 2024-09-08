from collections import deque

N, K = map(int, input().split())
limit = 100001
cnt = [0] * limit #해당 위치에 도착하기 위한 카운트
visited = [False] * limit

def bfs(x, end):
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        if x == end: return cnt[x]
        
        if -1 < x*2 < limit and not visited[x*2]:
            queue.appendleft(x*2) #큐의 왼쪽에 넣어주기
            cnt[x*2]=cnt[x]
            visited[x*2]=True
        if -1 < x-1 < limit and not visited[x-1]:
            queue.append(x-1)
            cnt[x-1] = cnt[x]+1
            visited[x-1]=True
        if -1<x+1<limit and visited[x+1]==0 :
            queue.append(x+1)
            cnt[x+1]=cnt[x]+1
            visited[x+1]=True

print(bfs(N, K))