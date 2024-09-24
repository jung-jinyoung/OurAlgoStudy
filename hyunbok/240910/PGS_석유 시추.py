def func(arr,N,M,now,check):
    cnt = 0
    for i in range(N):
        if arr[i][now]!=0 and check[arr[i][now][1]]==0:
            check[arr[i][now][1]]^=1
            cnt+=arr[i][now][0]
    return cnt

def solution(land):
    tag=0
    ans = 0
    n,m=len(land),len(land[0])
    visited=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if land[i][j] and visited[i][j]==0:
                visited[i][j]=1
                q=[(i,j)]
                p=0
                while p<len(q):
                    x,y=q[p]
                    p+=1
                    for nx,ny in ((x+1,y),(x-1,y),(x,y-1),(x,y+1)):
                        if 0<=nx<n and 0<=ny<m and land[nx][ny] and visited[nx][ny]==0:
                            visited[nx][ny]=1
                            q.append((nx,ny))
                for xxx,yyy in q:
                    land[xxx][yyy]=(len(q),tag)
                tag+=1
    for j in range(m):
        ans = max(ans,func(land,n,m,j,[0]*tag))

    return ans