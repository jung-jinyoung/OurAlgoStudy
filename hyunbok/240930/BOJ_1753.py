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
q = [(0,K-1)]
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