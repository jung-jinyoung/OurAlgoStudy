n, k = map(int, input().split())  # 원소 갯수, 중복
lst = list(map(int, input().split()))

# 중복 횟수 저장할 배열
m = max(lst)
idx_cnt = [0] * (m + 1)
result = 0
# 포인터
l, r = 0, 0

while r < n:
    # 개수가 중복이되면 r은 더 가지 않고 그자리에서 멈춰있음
    if idx_cnt[lst[r]] < k:
        idx_cnt[lst[r]] += 1  # 카운트 추가
        r += 1
    # r멈춘 상황에서 l이 쫓아오면서 윈도우 초기화
    else:
        idx_cnt[lst[l]] -= 1
        l += 1
    result = max(result, r - 1)
    # if (r-l) > result:
    #     result = (r-l) #l포함 안함
print(result)
