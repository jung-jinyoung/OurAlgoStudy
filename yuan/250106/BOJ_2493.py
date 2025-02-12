'''
st에 현재의 나보다 큰수만 계속 남기기
다음수 갱신할떄
나보다 작으면  내가 결과값이고
나보다 크면 st에서 찾으면 됨
'''
from collections import deque
st = deque([])
n = int(input())
arr = list(map(int,input().split()))
res = [0] * n

# st에 (idx, arr[idx]) 저장
for i in range(n):
    # st 에서 계속 pop
    while st and st[-1][1] < arr[i]:
        st.pop()
    if st:
        res[i] = st[-1][0] +1
    else:
        res[i] = 0
    st.append((i,arr[i]))

print(*res)