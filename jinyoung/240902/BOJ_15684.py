import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M, H = map(int,input().strip().split())

# 3개 이내 사다리를 추가해서 자기 자리로 돌아오도록 해야 한다.

laddor = [ [0] * (N+2) for _ in range(H+1)] # 더미 추가
for _ in range(M):
    r, c = map(int,input().strip().split())
    laddor[r][c] = 1 # 사다리 놓기

# 사다리를 둘 수 있는 위치 경우의 수 
arr = [[r, c] for r in range(1, H + 1) for c in range(1, N+1) if laddor[r][c] == 0]


def check():
    for j in range(1, N+1):
        now = j
        for i in range(1, H+1):
            if laddor[i][now] == 1:
                now +=1
            # if 문으로 처리했어서 now 값 변경으로 now 변경 안되서 틀림
            elif laddor[i][now-1] == 1 :
                now -=1
        
        if now != j :
            return False
    return True


def dfs(n,s,cnt): # 현재 놓은 사다리 개수 n개, 현재 s번째 pos 값, 둘 수 있는 경우의 수 cnt
    global ans

    if ans == 1 :
        return

    if n == cnt :
        # 모든 개수 선택 완료 
        if check():
            ans = 1
        return
    
    for j in range(s,len(arr)):
        r, c = arr[j]

        # 왼쪽 사다리, 오른쪽 사다리가 없으면
        if laddor[r][c-1] == 0 and laddor[r][c+1] == 0 :
            laddor[r][c] = 1 
            dfs(n+1,j+1,cnt)
            laddor[r][c] = 0
 

ans = 0 
for cnt in range(4):
    dfs(0,0,cnt)
    if ans == 1 :
        print(cnt)
        break
else:
    print(-1)