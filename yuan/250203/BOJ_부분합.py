'''
부분합 문제였음

풀이 관련 noti
 
1) 처음에 윈도우로 풀려고 했는데 투포인터가 맞음 
   윈도우는 윈도우의 사이즈가 정해져있을때 쓸 것.
   
2) 투포인터로 풀 때 포인터가 배열 내의 모든 인덱스를 제대로 다 도는지 확인할 것
   + 
   이번 문제의 경우 제일 끝 인덱스를 제대로 안돌아서 문제였음
   + 
   배열 범위를 맞추는 것보다 인덱스 에러가 나는 위치를 찾아서 에러가 안나게만 break 걸어주는게 훨씬 빠름

3) 반례는 0, 100 등등 으로 만드는 연습하기 
'''

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
min_res = 1e9  # 불가능한 최대값

l, r = 0, 0
now_sum = sum(arr[l : r + 1])
while 0 <= l <= r < n:
    if now_sum < s:
        r += 1
        # r이 n-1일때 여기서 인덱스 에러나기 떄문에 if문걸어주기
        if r < n:
            now_sum += arr[r]
        else:
            break
    else:
        now_len = r - l + 1
        min_res = min(now_len, min_res)
        now_sum -= arr[l]
        l += 1
    # print('l',l,'r',r,'sum',now_sum)

if min_res == 1e9:
    print(0)
else:
    print(min_res)
~