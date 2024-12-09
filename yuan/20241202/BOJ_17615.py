import sys


n = int(sys.stdin.readline())
m = list(map(str, sys.stdin.readline().strip()))
answer = []
blue = 0
red = 0
cnt = 0

# 우측으로 레드 보내기
for i in range(n):
    if m[i] == "R":
        red += 1

    if m[i] == "B" and red:
        cnt += red
        red = 0

answer.append(cnt)

# 우측으로 블루 보내기
cnt = 0
for i in range(n):
    if m[i] == "B":
        blue += 1

    if m[i] == "R" and blue:
        cnt += blue
        blue = 0

answer.append(cnt)

# 좌측으로 레드 보내기
m.reverse()
cnt = 0
red = 0
for i in range(n):
    if m[i] == "R":
        red += 1

    if m[i] == "B" and red:
        cnt += red
        red = 0

answer.append(cnt)


# 좌측으로 블루 보내기
blue = 0
cnt = 0
for i in range(n):
    if m[i] == "B":
        blue += 1

    if m[i] == "R" and blue:
        cnt += blue
        blue = 0

answer.append(cnt)
print(min(answer))
