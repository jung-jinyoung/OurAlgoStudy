from collections import deque

n, k = map(int, input().split())
q = deque([])
check = [-1] * (100001)

q.append(n)
check[n] = 0  # 시작점

while q:
    now = q.popleft()

    if 0 <= now * 2 <= 100000 and (check[now * 2] == -1 or check[now * 2] > check[now]):
        check[now * 2] = check[now]
        q.append(now * 2)

    if 0 <= now + 1 <= 100000 and (
        check[now + 1] == -1 or check[now + 1] > check[now] + 1
    ):
        check[now + 1] = check[now] + 1
        q.append(now + 1)

    if 0 <= now - 1 <= 100000 and (
        check[now - 1] == -1 or check[now - 1] > check[now] + 1
    ):
        check[now - 1] = check[now] + 1
        q.append(now - 1)

print(check[k])
