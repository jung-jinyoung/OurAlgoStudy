n = int(input())
lst = list(map(int, input().split()))
answer = [0] * n
for i in range(1, n + 1):
    cnt = lst[i - 1]
    # print(i,cnt)
    # i = 1, cnt = 6
    for idx, j in enumerate(answer):
        if cnt != 0 and (j == 0 or j > i):
            cnt -= 1
            continue
        if cnt == 0 and answer[idx] == 0:
            answer[idx] = i
            # print(answer)
            break
print(*lst)
