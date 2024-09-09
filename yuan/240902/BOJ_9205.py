from collections import deque


def bfs(start,end,convs):
    my_pos = deque([])
    my_pos.append(start)
    visit = [0 for _ in range(len(convs))]
    while my_pos:
        now = my_pos.popleft()
        now1,now2 = now[0],now[1] # 현재좌표 기준 end까지 거리 확인
        dist = abs(now1-end[0])+abs(now2-end[1])
        if dist <= 1000:
            print('happy')
            return

        for idx,nxt in enumerate(convs):
            if not visit[idx] and (abs(now1 - nxt[0]) + abs(now2 - nxt[1])) <= 1000:
                visit[idx] = 1
                my_pos.append([nxt[0],nxt[1]]) # 위치 이동

    print('sad')
    return



tc = int(input())
for _ in range(tc):
    n = int(input())# 편의점 갯수
    convs = []
    start = list(map(int, input().split()))
    for _ in range(n):
        conv = list(map(int, input().split()))
        convs.append(conv)
    end = list(map(int, input().split()))

    bfs(start,end,convs)