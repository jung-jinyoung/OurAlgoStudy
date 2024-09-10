from collections import deque
def bfs_check(data,x,y,cnt):
    q= deque()
    q.append((x,y))
    v = [[0]*M for _ in range(N)]
    v[x][y]^=1
    num = 1
    while q:
        xxx,yyy=q.popleft()
        for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
            nx,ny=xxx+dx,yyy+dy
            if data[nx][ny] and v[nx][ny]==0:
                num+=1
                v[nx][ny]^=1
                q.append((nx,ny))
    if cnt == num:
        return False        # 덩어리 한개
    else:
        return True         # 덩어리 여러개


N, M= map(int,input().split())     # N x M
arr = [list(map(int,input().split())) for _ in range(N)]
Time = 0
zeros = [[0]*M for _ in range(N)]
count=0
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if arr[i][j]:
            count+=1
            iii, jjj =i,j
if bfs_check(arr,iii,jjj,count):
    print(0)
else:
    while True:
        Time+=1
        count=0
        iii,jjj=False,False
        temp = [[0] * M for _ in range(N)]
        for i in range(1,N-1):
            for j in range(1, M-1):
                if arr[i][j]:
                    zero_check = 0
                    for dx,dy in ((1,0),(-1,0),(0,-1),(0,1)):
                        if arr[i+dx][j+dy]==0:
                            zero_check+=1
                    if arr[i][j]-zero_check > 0:
                        temp[i][j] = arr[i][j]-zero_check
                        iii,jjj=i,j
                        count+=1

        arr = temp[:]
        if arr == zeros:
            print(0)
            break
        elif bfs_check(arr,iii,jjj,count):
            print(Time)
            break
        else:
            arr = temp[:]