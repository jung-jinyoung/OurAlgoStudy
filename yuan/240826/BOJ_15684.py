'''
시간초과 최소화하는 밭법으로
변수 lv = 1,2,3 지정, lv마다 매번 dfs 새로 호출 시작
가로선이 1개 -2개-3개일때 바로 check()를 호출하고 return 해버릴수 있음

그렇지 않고 dfs 를 돌리면서 \
ans = min(ans,cnt)로 업데이트 & cnt>3 return 시
상대적으로 시간 많이 걸림

'''

import sys

input = sys.stdin.readline


def check():
    for start in range(1, n + 1):
        colnum = start # k는 업데이트할 열번호
        for i in range(1, h + 1):
            if ladder[i][colnum]:
                colnum += 1
            elif ladder[i][colnum - 1]:
                colnum -= 1
            # 둘다 아니면 colnum의 변동x, 다음층으로 이동
        # 층 끝났을때 colnum이 처음저장한 start와 동일한지 확인
        if colnum != start:
            return False
    return True


def dfs(cnt, x, y):
    if lv == cnt: # cnt가 1,2,3 일때의 단계에서 멈추기
        if check():
            print(cnt)
            exit()
        return

    # 현재 laddar기준 매 사다리층에 넣을 수 있는 모든 가로선에 대해 넣거나or 말거나로 dfs
    for i in range(x, h + 1): #층 확인
        if i==x: # 현재층인x 층에서는 이전사다리번호에서 쭉 체크(가로선 중복설치 방지)
            startcol = y
        else:
            startcol = 1 # 다음층부터는 1번부터 가로선 놓을수 있는 모든 파트 체크
        for j in range(startcol, n): # 한층에 세열씩 확인
            if not ladder[i][j] and not ladder[i][j - 1] and not ladder[i][j + 1]:
                ladder[i][j] = 1 #가로선 설치
                dfs(cnt + 1, i, j + 2) # 두열 이동해서 다시 가로선 설치가능한 x,y좌표로 이동
                ladder[i][j] = 0 # 가로선 취소


n, m, h = map(int, input().split())
ladder = [[0] * (n + 1) for _ in range(h + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    ladder[a][b] = 1

for lv in range(4):
    dfs(0, 1, 1)

print(-1)
