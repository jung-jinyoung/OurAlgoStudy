import sys
from copy import deepcopy

input = sys.stdin.readline
N, M = map(int, input().split())
origin_area = [list(map(int,input().split())) for _ in range(N)]

safe_cnt = 0
virus = [] #virus 영역 넣을 리스트
zero_pos = [] #빈칸인 곳들 위치 리스트
for i in range(N):
    for j in range(M):
        if origin_area[i][j] == 0:
            zero_pos.append((i,j))
            safe_cnt += 1
        elif origin_area[i][j] == 2:
            virus.append((i,j))
O = len(zero_pos) #벽을 세울 수 있는 곳의 수

max_safe_area = 0
for a in range(O-2):
    for b in range(a+1, O-1):
        for c in range(b+1, O):
            copied_virus = virus[:]
            copied_safe_cnt = safe_cnt-3
            copied_area = deepcopy(origin_area)

            copied_area[zero_pos[a][0]][zero_pos[a][1]] = 1
            copied_area[zero_pos[b][0]][zero_pos[b][1]] = 1
            copied_area[zero_pos[c][0]][zero_pos[c][1]] = 1

            while copied_virus:
                r, c = copied_virus.pop()
                for nr, nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if 0<=nr<N and 0<=nc<M and copied_area[nr][nc] == 0:
                        copied_area[nr][nc] = 1
                        copied_safe_cnt -= 1
                        copied_virus.append((nr,nc))
            max_safe_area = max(max_safe_area, copied_safe_cnt)
print(max_safe_area)