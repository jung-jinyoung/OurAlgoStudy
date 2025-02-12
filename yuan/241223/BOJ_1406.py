from collections import deque
import sys

input = sys.stdin.readline


strs = list(input().strip())
front_st = deque(strs) # deque(['d', 'm', 'i', 'h'])
back_st = deque([])

n = int(input())
log = [input().split() for _ in range(n)]
# print(log)[['B'], ['B'], ['P', 'x'], ['L'], ['B'], ['B'], ['B'], ['P', 'y'], ['D'], ['D'], ['P', 'z']]
for l in log:

    if l[0] == 'L':
        if front_st:
            s = front_st.pop()
            back_st.appendleft(s)
    elif l[0] == 'D':
        if back_st:
            s = back_st.popleft()
            front_st.append(s)
    elif l[0] == 'B':
        if front_st:
            front_st.pop()
    else:
        front_st.append(l[1])

print(''.join(front_st)+''.join(back_st))
