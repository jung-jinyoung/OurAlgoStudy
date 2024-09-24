# bfs이므로 먼저나온 값의 시간을 답으로 쓴다 -> 따라서 시간 0 소모인 순간이동은 왼쪽에 넣는다!

# 4 6 이라는 인풋을 돌리면 4->5->6으로 2가 나왔음
# 근데 4->3->6 이 1로 올바른 값임
# append 순서를 -1 이후 +1로 배치 하여 해결
from collections import deque
def bfs():
    q = deque()
    q.append((N, 0))
    while q:
        now, t = q.popleft()
        if now == K:
            print(t)
            break
        if now * 2 <= 100000 and not v[now * 2]:
            v[now * 2] = 1
            q.appendleft((now * 2, t))
        if now - 1 >= 0 and not v[now - 1]:
            v[now - 1] = 1
            q.append((now - 1, t + 1))
        if now + 1 <= 100000 and not v[now + 1]:
            v[now + 1] = 1
            q.append((now + 1, t + 1))

N, K = map(int, input().split())
v = [0] * 100001
v[N] = 1
bfs()
