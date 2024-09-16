import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M, K = map(int,input().split())
matrix = [ [*input().strip()] for _ in range(N)]
result = {}
keys = []
l, L = int(1e9), 0
for _ in range(K):
    temp = input().strip()
    if len(temp) < l :
        l = len(temp)
    if len(temp) > L :
        L = len(temp) 
    
    keys.append(temp)
    result[temp] = 0


def check(i,j,cnt,now_str):
    global visited
    if cnt > L :
        return
    if cnt >= l and now_str in result:
        result[now_str] +=1
    
    for di, dj in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
        ni = di + i
        nj = dj + j 
        if ni < 0 :
            ni = N-1
        if nj < 0 :
            nj = M-1
        if ni >= N :
            ni = 0
        if nj >= M :
            nj = 0
        check(ni,nj,cnt+1,now_str+matrix[ni][nj])

for i in range(N):
    for j in range(M):
        check(i,j,1,matrix[i][j])

for key in result:
    print(result[key])