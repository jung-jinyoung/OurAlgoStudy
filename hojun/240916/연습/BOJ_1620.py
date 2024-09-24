import sys
input = sys.stdin.readline

N, M = map(int, input().split())

name_to_num = dict()
num_to_name = [0]*(N+1)

names = [input().strip() for _ in range(N)]
problems = [input().strip() for _ in range(M)]


for i, name in enumerate(names):
    num_to_name[i+1] = name
    name_to_num[name] = i+1

for p in problems:
    if p.isdigit():
        print(num_to_name[int(p)])
    else:
        print(name_to_num[p])