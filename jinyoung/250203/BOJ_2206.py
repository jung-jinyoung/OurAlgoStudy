# 코드를 작성해주세요
import sys
from collections import deque

def my_bfs() : 
    my_queue = deque([(0, 0, 1, 1)]) # i, j, distance, 벽을 부술 수 있는 기회
    visited[0][0][1] = 1 # 벽을 부술 수 있는 상태에서 방문

    while my_queue : 
        i, j, dist, cnt = my_queue.popleft()

        # 목적지 도착했으면 거리 반환
        if (i, j) == (n-1, m-1) :
            return dist
        
        # 4 방향 탐색
        for (di, dj) in [(-1,0), (1,0), (0,-1), (0,1)] :
            ni = i + di
            nj = j + dj

            # 범위 확인
            if (0 <= ni < n) and (0<= nj < m):
                #  벽이 아니고 방문하지 않은 경우
                if my_map[ni][nj] == "0" and visited[ni][nj][cnt] == 0:
                    visited[ni][nj][cnt] = 1
                    my_queue.append((ni, nj, dist+1, cnt))
                
                # 벽인데 방문하지 않았고 부술 기회가 남아 있는 경우
                if my_map[ni][nj] == "1" and cnt == 1 and visited[ni][nj][cnt] == 0 :
                    cnt -= 1
                    visited[ni][nj][cnt] = 1
                    my_queue.append((ni, nj, dist+1, cnt))

                    cnt+=1
    # 도착하지 못했을 경우 
    return -1



    


n, m = map(int, input().split(" "))
my_map = [list(input()) for _ in range(n)]
# 방문한 경우와 벽을 부순 경우 모두 저장 
visited = [ [[0] * 2 for _ in range(m)] for _ in range(n)]

print(my_bfs())