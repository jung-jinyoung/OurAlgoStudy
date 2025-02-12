"""
게임이 정상적으로 끝난 상태가 True
그 외는 다 False
    총 개수는 x가 o 보다 한개 더 많거나 동일하거나
    3이 0개 : '.'이 있으면 False
    3이 1개 : True
    3이 2개 이상인 경우 : 하나 빼면 3이 전부 사라지는지 확인
"""

import sys

input = sys.stdin.readline
numbers = [
    {0, 1, 2},
    {3, 4, 5},
    {6, 7, 8},
    {0, 3, 6},
    {1, 4, 7},
    {2, 5, 8},
    {0, 4, 8},
    {2, 4, 6},
]


def check(strs):
    idx_o = set()
    idx_x = set()

    dot = 0
    for idx, s in enumerate(strs):
        if s == "O":
            idx_o.add(idx)
        elif s == "X":
            idx_x.add(idx)
        else:
            dot += 1
    total = 0  # 3개수 확인
    num_o = 0
    num_x = 0
    lst = []
    # 가로 세로 대각선 중 3 있으면
    # 연속 3개:012,345,678 / 036, 147, 258 / 048, 246 /
    for number in numbers:
        if number.issubset(idx_o):
            total += 1
            num_o += 1
            lst.append(number)
        elif number.issubset(idx_x):
            total += 1
            num_x += 1
            lst.append(number)

    if len(idx_o) > len(idx_x) or (len(idx_x) - len(idx_o)) > 1:
        return False
    elif total == 0:
        if dot > 0:
            return False
        return True
    elif total == 1:
        if num_o == 1 and len(idx_x) > len(idx_o):
            return False
        elif num_x == 1 and len(idx_x) == len(idx_o):
            return False
        return True
    else:
        if num_x > 0 and num_o > 0:
            return False
        inters = set.intersection(*lst)
        if inters:
            return True
    return False
    # 집합들의 전체 교집합이 있는지 확인
    # return False : 3이 둘이상 있어서 불가능한 경우 , 꽉차있지 않은경우


while True:
    arr = input().strip()
    if arr == "end":
        exit()
    if check(arr):
        print("valid")
    else:
        print("invalid")
