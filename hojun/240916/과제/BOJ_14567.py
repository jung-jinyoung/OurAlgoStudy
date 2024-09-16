# 선수 과목
import sys
from collections import defaultdict, deque
input = sys.stdin.readline
N, M = map(int, input().split()) # N: 과목 수, M: 선수 조건의 수

subject = defaultdict(list) #key가 현재 과목, value가 현재과목 이수를 위해 필요한 선이수과목
result = [0]*(N+1) # 결과
pre = [0]*(N+1) # 선수과목 수
for _ in range(M):
    A, B = map(int, input().split())
    subject[A].append(B)
    pre[B] += 1

queue = deque()
for i in range(1, N+1):
    if pre[i] == 0: # 선수 과목 없는 경우
        queue.append((i, 1)) # (과목, 학기)
    
while queue:
    node, cnt = queue.popleft()
    result[node] = cnt
    for i in subject[node]: #현재 노드가 선수과목인 과목들
        pre[i] -= 1 #선수과목 개수 줄이기
        if pre[i] == 0:
            queue.append((i, cnt+1))

print(*result[1:]) #첫번째 과목부터 출력