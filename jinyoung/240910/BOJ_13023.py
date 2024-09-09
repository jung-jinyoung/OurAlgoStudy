import sys


#sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N, M = map(int, input().split())

checked = [[] for _ in range(N)]

for _ in range(M):
    p1, p2 = map(int,input().split())
    checked[p1].append(p2)
    checked[p2].append(p1)

# 방문 표시
visited = [0] * 2000

# 정답 표시
ans = False


# dfs 확인
def dfs(idx,depth):
    global ans
    # 조건 : 친구 관계가 4번 이상 연결되어 있다면
    if depth == 4:
        ans = True
        return

    for friend in checked[idx]:
        # 아직 확인하지 않은 친구라면
        if not visited[friend] :
            visited[friend] = 1
            dfs(friend, depth +1)
            visited[friend] = 0

for i in range(N):
    visited[i] = 1
    # 친구 관계 탐색
    dfs(i, 0)
    if ans:
        break
    visited[i] = 0
if ans:
    print(1)
else:
    print(0)