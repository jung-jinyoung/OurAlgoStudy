# 최악 경우는 3n: q1에서 n빼기, q2에서 n빼기,비교 n?

from collections import deque

def solution(q1, q2):
    n = len(q1)
    q1 = deque(q1)
    q2 = deque(q2)
    s1,s2 = sum(q1), sum(q2)
    cnt = 0
    p1, p2 = 0,0 # 포인터 
    
    while q1 and q2 and cnt <3*n:
        if s1>s2:
            x = q1.popleft()
            q2.append(x)
            s1-=x
            s2+=x 
            cnt+=1
        elif s2>s1:
            x = q2.popleft()
            q1.append(x)
            s2-=x
            s1+=x 
            cnt+=1
        else:
            return cnt 
    return -1 
    
