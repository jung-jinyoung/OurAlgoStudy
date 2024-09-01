# 수 묶기
import sys
input = sys.stdin.readline

N = int(input())
nums = sorted([int(input()) for _ in range(N)])  # 오름 차순 정렬
a = -1001
b = -1001
result = 0

while nums:
  if a == -1001:
    a = nums.pop()
  elif b == -1001:
    b = nums.pop()
    if a*b >= a+b:
      result += a*b
      a, b = -1001, -1001
    else:
      result += a + b
      a, b = -1001, -1001
if a != -1001:
  result += a
  print(result)