import sys
from collections import defaultdict

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def find(arr, k):
    global min_value, max_value
    # 슬라이딩 윈도우 
    for i in range(len(arr)-k+1):
        now_arr = arr[i : i+k]
        min_value = min(min_value, now_arr[-1] - now_arr[0] + 1)
        max_value = max(max_value, now_arr[-1] - now_arr[0] + 1)
    return 


T = int(input())

for _ in range(T):
    W =  input().strip()
    K = int(input())
    
    if K == 1 :
        print(1,1, sep=' ')
        continue

    my_chars = defaultdict(list)
    
    for idx in range(len(W)):
        char = W[idx]
        my_chars[char].append(idx)

    min_value = int(1e9)
    max_value = 0
    for my_char in my_chars.keys():
        if len(my_chars[my_char]) >= K:
            # K개를 포함하는 짧은 문자열의 길이 
            find(my_chars[my_char],K)


            
    
    if min_value <= 10000 and max_value > 0 :
        print(min_value, max_value, sep=' ')
    else:
        print(-1)