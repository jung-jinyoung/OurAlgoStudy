import sys

input = sys.stdin.readline
S = input().strip()
T = input().strip()

while len(S) < len(T):
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[:-1][::-1]

if S == T:
    print(1)
else:
    print(0)