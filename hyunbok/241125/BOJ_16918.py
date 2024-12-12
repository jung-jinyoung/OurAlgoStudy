import sys,heapq
input = sys.stdin.readlines
data = input()
V,E = map(int,data[0].split())
K = int(data[1])
arr = [[] for _ in range(V)]
ans = [10*V]*V
ans[K-1]=0

for i in range(2,2+E):
    u,v,w = map(int,data[i].split())
    arr[u-1].append((v-1,w))
q = [(0,K-1)]def func1(t):
    if t == 1+N:
        return
    elif t % 2 == 0:  # 폭탄 설치는 짝수 초에
        for r in range(R):
            for c in range(C):
                if data[r][c] == 0:
                    data[r][c] = t + 3  # 3초 뒤에 폭발
    else:
        for r in range(R):
            for c in range(C):
                if data[r][c] == t:  # 폭발
                    for nr, nc in ((r, c + 1), (r, c - 1), (r - 1, c), (r + 1, c)):
                        if 0 <= nr < R and 0 <= nc < C and data[nr][nc] != t:
                            data[nr][nc] = 0
                    data[r][c] = 0
    func1(t + 1)

R, C, N = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]
data = [[0] * C for _ in range(R)]

# 초기 폭탄 상태 설정
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'O':
            data[i][j] = 3  # 초기 폭탄은 3초 후에 폭발

# N이 1일 경우 초기 상태 그대로 출력
if N == 1:
    for row in arr:
        print("".join(row))
else:
    func1(1)
    for i in range(R):
        temp = ''
        for j in range(C):
            if data[i][j] == 0:
                temp += '.'
            else:
                temp += 'O'
        print(temp)

while q:
    dist,node = heapq.heappop(q)
    if dist<=ans[node]:
        for to,weight in arr[node]:
            if ans[to]>dist+weight:
                ans[to]=dist+weight
                heapq.heappush(q,(dist+weight,to))

for i in ans:
    if i == 10*V:
        print("INF")
    else:
        print(i)