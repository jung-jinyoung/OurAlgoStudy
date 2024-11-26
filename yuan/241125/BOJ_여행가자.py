from collections import deque

def find(now, dest, map, n):
    # map에서 now에서 시작해서 dest도착가능한지확인
    # visit = [ [0]*(n) for _ in range(n)]

    # bfs 는 큐에 들어가는 노드 중복 방지라서 2D로 방문처리 가능
    visit = [0] * n
    q = deque([])
    q.append(now)
    while q:
        now = q.popleft()
        if now == dest:
            return True
        for idx, go in enumerate(map[now]):
            # if go == '1' and not visit[now][idx]:
            if go == "1" and not visit[idx]:
                visit[idx] = 1
                q.append(idx)
                # visit[now][idx] = 1

    print("NO")
    exit()
    # return False

# 도시, 여행계획 도시
n = int(input())
m = int(input())

# n개 도시의 연결상태 (0부터시작)
map = [list(input().split()) for _ in range(n)]
plan = list(input().split())

for i in range(len(plan) - 1):
    find(int(plan[i]) - 1, int(plan[i + 1]) - 1, map, n)

print("YES")
