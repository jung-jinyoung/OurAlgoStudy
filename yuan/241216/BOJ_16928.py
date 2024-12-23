from collections import deque

"""
set은 참조 타입이므로 
dfs에서 매번 다른 visit 을 가져가는게 의미 없음
예를 들어 
for i in range(5):
    visit.add(i)
    dfs(visit)
의 경우 visit은 (0,1,2,3,4,5.. )같이 모두 포함됨

따라서 다른 visit을 주려면
    visit.add(i)
    dfs(visit)
    visit.remove(i)  // remove 는 메모리 많이듦
가 되어야 함 

bfs의 경우 
우선순위 큐를 쓰지 않아도 
한번의 이동 시의 node를 pop 하므로 
이동 가중치가 동일한 이상 
여러 경우 비교하지 않아도 최단거리를 도출 할 수 있음

중복 확인으로 set vs list 
검색 속도는 o(1) vs o(n) 
단 set은 해시테이블을 유지하기 위해 추가 메모리를 사용함

중복 확인할 데이터가 n 개로 고정되어 있으며 정수인 경우
리스트가 용이함 (110064	112)
그에 비해 데이터 갯수가 고정되어 있지 않고 문자열 등인 경우
set가 용이(110064	124)

"""

n, m = map(int, input().split())
laddar = dict()
snake = dict()
for _ in range(n):
    x, y = map(int, input().split())
    laddar[x] = y
for _ in range(m):
    x, y = map(int, input().split())
    snake[x] = y

# visit = set()
visit = [0] * 1000
visit[1] = 1
q = deque([(1, 0)])  # now, cnt
while q:
    now, cnt = q.popleft()
    if now > 100:
        continue
    if now == 100:
        print(cnt)
        break
    for i in range(1, 7):
        nxt = now + i
        # 사다리 뱀 확인
        if nxt in laddar:
            nxt = laddar[nxt]
        elif nxt in snake:
            nxt = snake[nxt]
        # 중복 확인
        if not visit[nxt]:
            visit[nxt] = 1
            q.append((nxt, cnt + 1))
