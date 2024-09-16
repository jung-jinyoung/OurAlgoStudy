# 수강신청
import sys
input = sys.stdin.readline

K, L = map(int, input().split()) #K: 수강가능인원, L : 대기목록의 길이

sequence = dict()
for i in range(L):
    sequence[input().strip()] = i

result = sorted(sequence.items(), key=lambda x : x[1])

N = len(result)
if N < K:
    K = N

for i in range(K):
    print(result[i][0])
