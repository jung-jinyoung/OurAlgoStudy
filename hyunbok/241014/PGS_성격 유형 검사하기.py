# 1번이 왼쪽 7번이 오른쪽
# 1,2,3 을 마이너스로 5,6,7을 플러스로
# x를 1~7 이면  (x-4) 하면
from collections import defaultdict
def solution(survey, choices):
    N = len(choices)
    ans = defaultdict(int)
    for i in range(N):
        ans[survey[i]]+=(choices[i]-4)
    ans = ans.items()
    arr = defaultdict(int)
    
    for Type,score in ans:
        if Type[0]<Type[1]:
            arr[Type]+=score
        else:
            tmp = Type[1]+Type[0] 
            arr[tmp]-=score
            
    answer = ''
    if arr['RT']<=0:
        answer+='R'
    else:
        answer+='T'
    if arr['CF']<=0:
        answer+='C'
    else:
        answer+='F'
    if arr['JM']<=0:
        answer+='J'
    else:
        answer+='M'
    if arr['AN']<=0:
        answer+='A'
    else:
        answer+='N'
    print(ans)
    
    return answer