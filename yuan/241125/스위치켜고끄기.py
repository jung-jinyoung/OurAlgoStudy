from collections import deque
import sys

input = sys.stdin.readline

def pprint(switch):
    # 20개씩 쪼개기
    size = 20
    for i in range(0, len(switch), size):
        print(*switch[i:i + size])

def change_symmetry(num,switch,n):
    global dict
    l = num - 1
    r = num + 1
    switch[num-1] = dict[switch[num-1]]
    while l-1>=0 and r-1 <n:
        if switch[l-1] == switch[r-1]:
            switch[l-1] = dict[switch[l-1]]
            switch[r-1] = dict[switch[r-1]]
            l -= 1
            r += 1
        else:
            break
    return switch


def find_square(num,switch,n):
    global dict
    # num이 내 숫자, n이 스위치 개수
    # num씩
    i = num
    while i<=n:
        switch[i-1] = dict[switch[i-1]]
        i+=num
    return switch

def change(q,switch,n):
    while q:
        sex, num = q.pop()
        if sex == 1:
            find_square(num,switch,n)
        elif sex == 2:
            change_symmetry(num,switch,n)
    pprint(switch)

n = int(input()) # 스위치 개수
switch = list(map(int, input().split()))
std = int(input()) # 학생
dict = {1:0, 0:1}

lst = deque([])

for _ in range(std):
    sex, num = map(int, input().split())
    lst.appendleft([sex,num])

change(lst,switch,n)