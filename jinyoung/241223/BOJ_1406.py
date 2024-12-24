import sys

sys.stdin = open('input.txt','r')
input = sys.stdin.readline

my_strs = list(input().rstrip())
N = len(my_strs)
M = int(input())

left_stacks = my_strs
right_stacks = []
for _ in range(M):
    command = input().split()
    c = command[0]

    if c == 'L':
        if left_stacks:
            temp = left_stacks.pop()
            right_stacks.append(temp)
    elif c == 'D':
        if right_stacks:
            temp = right_stacks.pop()
            left_stacks.append(temp)
    elif c == 'B':
        if left_stacks:
            left_stacks.pop()
    else :
        left_stacks.append(command[1])

answer = left_stacks + right_stacks[::-1]
print(''.join(answer))
