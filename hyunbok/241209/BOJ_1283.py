from collections import defaultdict

check = defaultdict(int)
N = int(input())
for _ in range(N):
    temp = list(input().split())
    ans = ''
    flag = 1
    lll = len(temp)
    for i in range(lll):
        if check[temp[i][0].upper()]==0:
            check[temp[i][0].upper()]^=1
            for idx in range(lll):
                for j in range(len(temp[idx])):
                    if j==0 and idx == i:
                        ans += '['
                        ans += temp[i][0]
                        ans += ']'
                    else:
                        ans += temp[idx][j]
                ans+=' '
            break
    else:
        for s in temp:
            for c in s:
                if flag and check[c.upper()]==0:
                    ans += '['
                    ans += c
                    ans += ']'
                    flag^=1
                    check[c.upper()] ^=1
                else:
                    ans += c
            ans += ' '
    print(ans)