from collections import deque

def solution(land):
    
    
    n = len(land)
    m = len(land[0])
    
    visited = [ [0] * m for _ in range(n)]
    # 인접한 항목 찾아서 visited 확인 후 석유가 있으면 저장
    
    
    
    # 각 칼럼에 뽑을 수 있는 석유 양 저장 
    def save_info(arr,cnt,my_result):
        for column in arr:
            if column not in my_result:
                my_result[column] = [cnt]
            else:
                my_result[column].append(cnt)
        return 

    # 인접한 칸 조사
    def bfs(row, col, n, m, visited):
        que = deque()
        que.append((row,col))

        save_column = set()
        save_column.add(col)

        count = 1

        while que:
            row, col = que.popleft()
            for dr, dc in [(0,1), (1,0),(0,-1),(-1,0)]:
                nr = row + dr
                nc = col + dc
                # 범위가 넘어가지 않고 
                if 0<=nr<n and 0<=nc<m:
                    # 방문하지 않은  석유가 있으면
                    if land[nr][nc] == 1 and not visited[nr][nc]:
                        que.append((nr,nc))
                        save_column.add(nc)
                        count+=1
                        visited[nr][nc] = 1
        save_info(save_column, count,my_result)
        
    
    my_result= {}
    
    for i in range(n):
        for j in range(m):
            if not land[i][j] :
                continue
            if land[i][j] == 1 and not visited[i][j] :
                # 방문 표시
                visited[i][j] = 1 
                bfs(i, j, n, m, visited)
    
    max_total = 0
    for key in my_result:
        temp_total = sum(my_result[key])
        max_total = max(max_total, temp_total)
        
    
    return max_total