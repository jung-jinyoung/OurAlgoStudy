import sys
from collections import deque

input = sys.stdin.readline

def check_seperate(newarr, last, year) :
    visit = [[0 for _ in range(m)] for _ in range(n) ]
    ice = deque([last])

    if last == [-1,-1]:
        print(0)
        return # 다 녹아서 남은 빙산 없으면 0출력

    # last 시작점으로 이어진 빙산 체크
    while ice:
        x,y = ice.popleft()
        visit[x][y] = 1 #방문체크
        for k in range(4):
            nx, ny = x+di[k], y+dj[k]  # 범위안, 빙산안녹음, 아직 방문안함
            if 0<=nx<n and 0<=ny<m and newarr[nx][ny]>0 and not visit[nx][ny]:
                visit[nx][ny] = 1
                ice.append([nx,ny])

    #첫번째 빙산 방문 후 안방문 빙산 있는지 체크
    for i in range(n):
        for j in range(m):
            if newarr[i][j] >0 and not visit[i][j]:#빙산있지만방문x 면 분리된거
                print(year)
                return

    #분리 안됐으면 다시녹이기
    melt(newarr, year)


def melt(arr,year):
    last = [-1,-1]# 마지막으로 들어간 0아닌 좌표 저장
    newarr = [[0 for _ in range(m)] for _ in range(n) ]
    for i in range(n):
        for j in range(m):
            if arr[i][j] !=0: # 0아닌 좌표 기준 4방향 확인
                near = 0
                for k in range(4):
                    ni,nj = i+di[k], j+ dj[k]
                    if 0<=ni<n and 0<=nj<m and arr[ni][nj] ==0: # 주변에 0있을때
                        near+=1
                newarr[i][j] = max(arr[i][j]-near,0) # 0보다 작으면 0넣기
                if newarr[i][j] !=0:
                    last = [i,j] # 다 안녹은 마지막 빙산으로 업데이트 해주기

    check_seperate(newarr, last, year+1)#녹은 빙산, 직전 빙산좌표, 시간



n, m = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n) ]
di, dj = [1,-1,0,0],[0,0,1,-1]

melt(arr,0)#배열, 녹은 시간