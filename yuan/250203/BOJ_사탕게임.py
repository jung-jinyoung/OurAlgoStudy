"""
c,p,z,y

1. 인접한 수가 다른색일떄 바꿔서
모든경우의 수 체크

2. 바꾼상태에서
가로한번 세로한번 연속 길이 체크

noti
cnt 갱신시점 체크해야함.. 
한줄의 끝까지 갔을때 if문에 안걸리고
index 넘어서 그냥 for문 돌아버림림

"""

import sys

input = sys.stdin.readline


def checkhorizontal(arr, n):
    global maxv
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > maxv:
                maxv = cnt


def checkvertical(arr, n):
    global maxv
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > maxv:
                maxv = cnt


n = int(input())
arr = [list(input().strip()) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
maxv = -1

# 중복처리 더 할 수 있는지 확인
for x in range(n):
    for y in range(n):
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
                checkhorizontal(arr, n)
                checkvertical(arr, n)
                arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
print(maxv)