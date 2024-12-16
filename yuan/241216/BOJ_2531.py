from collections import deque
# 접시수, 초밥수, 연속접시수, 쿠폰번호
n, d, k, c = map(int, input().split())
count = [0] * (d+1)  # 초밥 종류
q = deque([]) # 윈도우
lst = []

for _ in range(n):
    lst.append(int(input()))
# 초기 윈도우 설정
for i in range(k):
    count[lst[i]] += 1
    q.append(lst[i])

count[c] +=1
idx = k-1 # (idx) % N
answer = len([ i for i in count if i!=0])
count[c] -=1

# 윈도우가 한바퀴 돌면 n 번체크 하면 됨
for _ in range(n):
    bf = q.popleft()
    count[bf] -=1

    now_idx = (idx+1) % n
    count[lst[now_idx]] += 1
    q.append(lst[now_idx])

    count[c] += 1
    # print(bf,lst[now_idx])
    # print(count)
    answer = max (answer, len([ i for i in count if i!=0]))
    count[c] -=1
    idx+=1
print(answer)