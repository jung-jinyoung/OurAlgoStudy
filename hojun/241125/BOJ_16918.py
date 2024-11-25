# 봄버맨

import sys
input = sys.stdin.readline
R, C, N = map(int, input().split())

data = [list(input().strip()) for _ in range(R)]

pos = {i : [] for i in range(0, N+1)}
for i in range(R):
    for j in range(C):
        if data[i][j] == 'O': #폭탄을 심은 시간으로 대체해주기
            data[i][j] = 0 
            pos[0].append((i,j))

for t in range(1, N+1):
    if pos.get(t-3): # 3초전에 터트릴게 있다면
        for x,y in pos[t-3]: 
            if data[x][y] == t-3: # 터져야할 폭탄이라면!
                data[x][y] = '.'
                for di, dj in ((0,1), (0,-1), (1, 0), (-1, 0)):
                    ni, nj = x+di, y+dj
                    if 0<= ni < R and 0 <= nj < C:
                        if data[ni][nj] != t-3: # 주변에도 지금터질 폭탄 아닌 경우
                            data[ni][nj] = '.'

    if t % 2 == 0: # 봄버맨이 폭탄 설치할때
        for x in range(R):
            for y in range(C):
                if data[x][y] == '.':
                    data[x][y] = t
                    pos[t].append((x,y))
    # for i in range(R):
        # for j in range(C):
            # print(data[i][j], end='')
        # print()
    # print('-------------------')

# 숫자들 다시 'O'로 바꿔서 출력
for i in range(R):
    for j in range(C):
        if data[i][j] == '.':
            print('.', end='')
        else:
            print('O', end='')
    print()