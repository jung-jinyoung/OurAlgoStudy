
def solution(m, n, puddles): #col, row 
    c = m 
    r = n 
    dp = [[-1 for _ in range(c)] for _ in range(r)]
    dp[0][0] = 1 

    for coord in puddles:
        coord_r = coord[1]-1
        coord_c = coord[0]-1
        dp[coord_r][coord_c] = 0 # 웅덩이는 무조건 dp 0  
    
    #1,1부터 row,col까지의 합 
    def check_root(row, col):
          # 범위 벗어난 경우 
        if row<0 or row>=r or col<0 or col>=c:
            return 0 
        else:
            if dp[row][col] != -1: # dp값 있는경우
                return dp[row][col] 
            else:
                return check_root(row-1,ccol) + check_root(row,col-1)

    for x in range(r):
        for y in range(c):
            if dp[x][y] == -1:
                dp[x][y] = check_root(x-1,y) + check_root(x,y-1)
            
    answer = dp[r-1][c-1] % 1000000007
    return answer