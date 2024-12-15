from collections import defaultdict, deque

# 입력 받기
N, K = map(int, input().strip().split())

# 초기화
my_info = defaultdict(int)
my_arr = deque([N])

# 방문 시간 저장
my_info[N] = 0
while my_arr:
    now_pos = my_arr.popleft()

    # 동생을 찾은 경우 처리
    if now_pos == K:
        # 첫 번째 발견 시 최단 시간 저장
        print(my_info[now_pos])
        break
    # 순간 이동 확인
    double_pos = now_pos * 2
    if 0<= double_pos <= 100000:
        if double_pos not in my_info :
            my_arr.appendleft(double_pos)
            my_info[double_pos] = my_info[now_pos]


    # 다음 위치 탐색
    for next_pos in (now_pos - 1, now_pos + 1):
        if 0 <= next_pos <= 100000:
            # 아직 방문하지 않았거나, 동일 최단 시간으로 방문 가능한 경우
            if next_pos not in my_info :
                my_arr.append(next_pos)
                my_info[next_pos] = my_info[now_pos] + 1