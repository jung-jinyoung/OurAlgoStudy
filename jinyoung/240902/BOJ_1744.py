import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())


positive_nums = []
other_nums = []

for _ in range(N):
    my_nums = int(input())
    if my_nums > 0 : # 0보다 크면 
        positive_nums.append(my_nums)
    else: # 그 외
        other_nums.append(my_nums)

# 정렬
positive_nums.sort()
other_nums.sort(reverse=True)


result = 0

while len(positive_nums) > 1 : 
    num1 = positive_nums.pop()
    num2 = positive_nums.pop()

    result += max(num1 * num2, num1+num2)

while len(other_nums) > 1:
    num1 = other_nums.pop()
    num2 = other_nums.pop()
    result += max(num1 * num2, num1+num2)

# 남은 숫자들 확인
if positive_nums :
    result += positive_nums.pop()
if other_nums :
    result += other_nums.pop()

print(result)



