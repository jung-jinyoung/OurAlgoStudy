def find(x):
    if x == p[x]:
        return x
    else:
        p[x] = find(p[x])
        return p[x]

def union(x,y):
    p[find(x)] = find(y)

N = int(input())
M = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]    # N개 도시의 연결 상태
todo = list(map(int,input().split()))                       # M개의 여행 계획

p = [i for i in range(N)]

for i in range(N):
    for j in range(i,N):
        if arr[i][j]:
            union(i,j)

start_city = find(todo[0]-1)
for city in todo[1:]:
    if find(city-1) != start_city:
        print("NO")
        break
else:
    print("YES")