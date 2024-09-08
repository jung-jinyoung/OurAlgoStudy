import sys
from collections import deque


# 최대 걸을 수 있는 거리 : 50m * 맥주 20병 == 1000m
# 1000m 내 편의점이 있으면 계속 갈 수 있음 -> 편의점 좌표로 이동
# 현재 위치에서 롹 페스티벌 위치가 1000 m 이내면 도착 가능


sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def calc(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)


def bfs():
    global sx, sy

    que = deque()
    que.append((sx, sy))

    while que :
        x, y = que.popleft()
        # 현재 위치에서 바로 롹 페스티벌 갈 수 있으면 리턴
        if calc(x,y,ex,ey) <= 1000 :
            print("happy")
            return

        # 편의점 확인
        for idx in range(n):
            if not visited[idx] :
                cx, cy = conveniences[idx]
                # 현재 위치에서 이동할 수 있는 편의점 모두 확인
                if calc(x,y,cx,cy) <= 1000:
                    visited[idx] = 1
                    que.append((cx,cy))
    print("sad")
    return



T = int(input())

for _ in range(T):
    # 편의점 개수
    n = int(input())

    # 편의점 방문 저장 리스트
    visited = [0] * n
    # 시작 위치
    sx, sy = map(int, input().split())
    # 편의점 좌표 저장 리스트
    conveniences = [[*map(int, input().split())] for _ in range(n)]
    # 도착 위치
    ex, ey = map(int, input().split())

    if calc(sx,sy,ex,ey) <= 1000:
        print("happy")
        continue

    bfs()




