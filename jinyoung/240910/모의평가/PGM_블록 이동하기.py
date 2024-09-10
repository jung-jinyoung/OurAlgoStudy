from collections import deque
board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]	


def solution(board):
    
    # 이동 방향 : (좌표1)(좌표2) => (좌표2)(좌표2의 상하) * 2
    directions = [(-1,1), (1,1)]
    check = [1, -1]
    
    N = len(board)
    
    # 로봇의 시작 위치 
    robot = [(0,0), (0,1)]
    
    visited = [[0] * N for _ in range(N)]
    
    que = deque()
    
    # 현재 시작 위치 저장
    que.append(robot+[0])
    # 현재 시작 위치 방문 표시
    visited[0][0] =1
    visited[0][1] = 1
    
    result = int(1e9)
    while que:
        position = que.popleft()
        pos1 = position[0]
        pos2 = position[1]
        count = position[2]
        if count >= result:
            continue
        
        if pos1 == (N-1,N-1) or pos2 == (N-1,N-1):
            result = min(result, count)
        
        for _ in range(2):
            # 왼쪽 친구가 이동 
            for idx in range(2) :
                di, dj = directions[idx]
                # 이동할 좌표
                ni = pos1[0] + di
                nj = pos1[1] + dj

                # 벽 확인 좌표
                ci = pos1[0] + di
                cj = pos1[1]
              # 도착 위치 와 대각선 위치에 벽 확인
                if 0<=ni<N and 0<=nj<N and 0<=ci<N and 0<=cj<N :
                    if not visited[ni][nj] and not board[ci][cj]:
                        # 90도 회전 
                        temp1 = pos2
                        temp2 = (ni,nj)
                        que.append([temp1,temp2,count+1])
                        visited[ni][nj] = 1
                directions[idx] = -di, -dj
            
            print(directions)
            


    return result
