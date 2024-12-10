def dfs(now, e, cnt, arr):
    global dx, dy, res, k
    if cnt > k:
        return
    if now == e:
        if cnt == k:
            res += 1
        # for i in arr:
        #     print(i)
        # print()
        return
    x, y = now[0], now[1]

    for p in range(4):
        nx, ny = x + dx[p], y + dy[p]
        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != "T":
            arr[nx][ny] = "T"
            dfs([nx, ny], e, cnt + 1, arr)
            arr[nx][ny] = "."


r, c, k = map(int, input().split())
arr = [list(input()) for _ in range(r)]
res = 0
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

# s = [r-1,0]
e = [0, c - 1]
# arr[s[0]][s[1]] = 's'
# arr[e[0]][e[1]] = 'e'
# s 에서 시작해서 e 로 끝내기
arr[r - 1][0] = "T"
dfs([r - 1, 0], e, 1, arr)
print(res)
