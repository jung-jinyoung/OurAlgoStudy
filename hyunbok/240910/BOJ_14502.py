import collections,sys,copy,itertools

def check(array,queue):
    global virus
    cnt = 0
    while queue:
        x,y=queue.popleft()
        for nx,ny in ((x+1,y),(x-1,y),(x,y-1),(x,y+1)):
            if 0<=nx<N and 0<=ny<M and array[nx][ny]==0:
                cnt+=1
                array[nx][ny]=2
                queue.append((nx,ny))
                if cnt > virus:
                    return
    virus = cnt

N,M =map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
q = collections.deque()
todo = []
ans = -3
virus = N*M
for i in range(N):
    for j in range(M):
        if arr[i][j]==2:
            q.append((i,j))
        elif arr[i][j]==0:
            ans+=1
            todo.append((i,j))
for w1,w2,w3 in itertools.combinations(todo,3):
    arr[w1[0]][w1[1]] ^= 1
    arr[w2[0]][w2[1]] ^= 1
    arr[w3[0]][w3[1]] ^= 1
    check(copy.deepcopy(arr),copy.copy(q))
    arr[w1[0]][w1[1]] ^= 1
    arr[w2[0]][w2[1]] ^= 1
    arr[w3[0]][w3[1]] ^= 1
print(ans-virus)