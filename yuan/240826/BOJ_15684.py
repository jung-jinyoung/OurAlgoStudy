from itertools import permutations
import sys
input = sys.stdin.readline

def check(arr,lv):
    check_lst = [0]*(n+1)
    # 현재 어레이에서 1층부터 h층까지 확인
    fisidx = 0 # 사다리 시작열 저장
    for idx in range(1,n+1): # 각 열마다 확인
        fisidx = idx # 시작열 업데이트
        floor = 1 # 층
        while floor <= h:
            if idx >n:
                return
            if arr[floor][idx]: # 우측 이동 가능여부 확인
                idx +=1 # 우측 이동
                floor +=1 # 아래층 이동
            elif arr[floor][idx-1]: # 좌측이동 가능여부 확인
                idx -=1
                floor +=1
            else:
                floor +=1
        # idx 확인. fixidx 가 idx와 같으면 check_lst[idx] = 1
        if idx == fisidx:
            check_lst[idx] = 1
        else:
            return # 같은 인덱스에 도착못하면 리턴때림
    if check_lst[-1] ==1:
        print(lv)
        # print(check_lst)
        exit()

# 열, 가로선갯수, 행
n, m, h = map(int, input().split())
arr = [[0]*(n+1) for _ in range(h+1)]


# n은 층, m은 가로선 있는 인덱스
for i in range(m):
    f, l = map(int,(input().split()))
    arr[f][l] = 1

locations = []
for x in range(1,h+1):
    for y in range(1,n+1):
        if arr[x][y] == 0:
            # 앞뒤도 0 아니어야함
            if 1<= y-1 <n+1 and arr[x][y-1] == 1:
                continue
            if 1<= y+1 <n+1 and arr[x][y+1] == 1:
                continue
            locations.append([x,y])

# 로케이션에서 1~3넣어서 확인

lv = 0
check(arr,lv) # 0일떄 체크
while True:
    lv+=1 # lv 더해주기
    if lv >3:
        print(-1)
        exit()
    loc_lst = list(permutations(locations, lv))
    for loc in loc_lst:
        for lc in loc: # [x,y]
            # 바꿀때도 앞뒤가 1이면 다음 loc로 넘어감
            if 1<= lc[1]-1 <n+1 and arr[lc[0]][lc[1]-1] == 1:
                break
            if 1<= lc[1]+1 <n+1 and arr[lc[0]][lc[1]+1] == 1:
                break
            arr[lc[0]][lc[1]] = 1 # 좌표 바꿔주기
        check(arr,lv)
        for loc in loc_lst:
            for lc in loc: # [x,y]
                arr[lc[0]][lc[1]] = 0 # 좌표 돌려놓기
