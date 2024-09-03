from collections import deque
t = int(input())
for tc in range(t):
    n = int(input())                            # 맥주를 파는 편의점의 개수
    arr = [list(map(int,input().split())) for _ in range(n+2)]

    q = deque()
    q.append((arr[0][0],arr[0][1]))             # 집(시작점)
    v = []
    while q:
        x,y = q.popleft()
        if arr[-1]==[x,y]:                      # 도착!
            print('happy')
            break
        for i,j in arr[1:]:                     # 집 이외의 좌표 모두 순회
            if 0<abs(x-i)+abs(y-j)<=1000 and [i,j] not in v:            # 방문한 적 없고 맥주 남아있으면
                q.append([i,j])
                v.append([i,j])
    else:
        print('sad')
