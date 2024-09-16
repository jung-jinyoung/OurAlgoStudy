# 패션왕 신해빈
import sys
from collections import defaultdict
from itertools import combinations
input = sys.stdin.readline



T = int(input()) #테스트케이스 수

for _ in range(T):
    cloth = dict()
    N = int(input()) # 의상 수
    type_num = 0
    for _ in range(N): # 의상들 확인
        name, c_type = input().split()
        if cloth.get(c_type):
            cloth[c_type] += 1
        else:
            cloth[c_type] = 1
    result = 1
    for key in cloth.keys():
        result *= cloth[key] + 1
    
    print(result - 1)