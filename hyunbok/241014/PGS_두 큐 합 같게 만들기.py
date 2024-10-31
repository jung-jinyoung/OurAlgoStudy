def solution(queue1, queue2):
    q= queue1+queue2
    N =len(q) 
    total_sum = sum(q)//2
    l,r=0,len(queue1)-1
    cnt = 0
    arr = [0]*N
    arr[0]=q[0]
    for i in range(1,N):
        arr[i]=q[i]+arr[i-1]
    if sum(queue1)==sum(queue2):
        cnt = 0
    else:
        while l<r:
            temp = arr[r-1]-arr[l]
            if l==r:
                temp = q[r]
            if temp==total_sum:
                break
            elif temp >total_sum:
                l+=1
            else:
                r+=1
            if r==N or r<l:
                cnt = -1
                break
            cnt+=1
    return cnt