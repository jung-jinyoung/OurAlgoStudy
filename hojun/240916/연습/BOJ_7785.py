# 회사에 있는 사람

N = int(input())

is_in = dict()

for _ in range(N):
    name, log = input().split()
    is_in[name] = log
    if log == "leave":
        del is_in[name] 


result = sorted(is_in.keys(), reverse=True)
[print(i) for i in result]