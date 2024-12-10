# def f(n):
#     global cnt_arr
#     print(n, cnt_arr[:10])
#     if cnt_arr[n] == -1:
#         cnt_arr[n] = 0 # 초기화
#         if n>1:
#             cnt_arr[n] += f(n-1)
#         if n>2:
#             cnt_arr[n] += f(n-2)
#         if n>3:
#             cnt_arr[n] += f(n-3)
#     return cnt_arr[n]

# 중복 허용 안할 경우
cnt_arr = [1] * 10001
# 1만 표현할때 모두 1가지 가짐
# 이전 수 +2 의 경우
for i in range(2, 1001):
    cnt_arr[i] += cnt_arr[i - 2]
# +3의 경우
for i in range(3, 1001):
    cnt_arr[i] += cnt_arr[i - 3]
t = int(input())
for _ in range(t):
    n = int(input())
    print(cnt_arr[n])
