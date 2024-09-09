from collections import deque
import sys

input = sys.stdin.readline

def bfs(visit,q):# 방문처리, q, 이동한 횟수
    res = []
    while q:
        loc, time = q.popleft()
        if loc == k: # n은 시작 수
            while True:
                res.append(loc)
                if loc == n:
                    print(time)
                    print(*res[::-1])
                    return
                loc = visit[loc] #visit에는 직전 수 저장

        # +1
        if 0<=loc+1<=100000 and visit[loc+1] == -1:
            visit[loc+1] = loc
            q.append([loc+1,time+1])
        # -1
        if 0<=loc-1<=100000 and visit[loc-1] == -1:
            visit[loc-1] = loc
            q.append([loc-1,time+1])
        # //2
        if  0<=loc*2<=100000 and visit[loc*2] == -1:
            visit[loc*2] = loc
            q.append([loc*2,time+1])

    return

n , k= map(int, input().split())
visit = [-1 for _ in range(100001)] # 초기화를 0으로 하면 메모리 초과 오류 발생
visit[n] = n
q = deque([[n,0]]) # 위치, 시간
bfs(visit,q)
