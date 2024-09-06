# 수 묶기
import sys

input = sys.stdin.readline
N = int(input())

plus = []   #1이상 양수 저장할 리스트
minus = []  #마이너스와 0 저장할 리스트
one = 0 #1은 그냥 무조건 혼자 더해지는게 최고임

for _ in range(N):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num <= 0:
        minus.append(num)
    else:
        one += 1

plus.sort()
minus.sort(reverse=True)

result = one

while len(plus)//2 > 0:
    a = plus.pop()
    b = plus.pop()
    result += a*b

if plus:
    result += sum(plus)

while len(minus)//2 > 0:
    a = minus.pop()
    b = minus.pop()
    result += a*b

if minus:
    result += sum(minus)

print(result)