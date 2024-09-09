# ABCDE
from collections import defaultdict, deque

N, M = map(int, input().split()) # N:사람수, M: 친구관계 수
rel = defaultdict(list)          #친구관계
for _ in range(M):
    A, B = map(int, input().split())
    rel[A].append(B)
    rel[B].append(A)


def dfs(now, depth):
    global arrive

    visited[now]=True
    if depth == 5:
        arrive = True
        return
    
    for next in rel[now] :
        if not visited[next]: #방문한적 없으면
            dfs(next, depth+1)
    visited[now]=False

    
arrive = False
visited = [False] * N
for i in range(N): #모든 사람 순회
    dfs(i, 1)
    if arrive:
        print(1)
        break
else:
    print(0)