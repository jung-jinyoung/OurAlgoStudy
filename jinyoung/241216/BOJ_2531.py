import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, d, k, c = map(int, input().strip().split())
# 접시의 수 n, 초밥 가짓수 d 연속해서 먹는 접시의 수 k, 쿠폰 번호 c

sushies = [int(input()) for _ in range(n)]
max_result = 0
for i in range(n):
    if i <= n-k :
        cnt = len(set(sushies[i:i+k] + [c]))
    else:
        now = set()
        cnt = len(set(sushies[i:n] + sushies[:(i+k)%n] + [c]))
    if cnt > max_result:
        max_result = cnt
print(max_result)   

