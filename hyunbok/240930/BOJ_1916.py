import heapq,sys
input = sys.stdin.readline
t = int(input())
printf = ['EMPTY']*t
for tc in range(t):
    k = int(input())
    ans = [0]*k
    Q1,Q2 = [],[]
    idx = 0
    for _ in range(k):
        c,n = input().split()
        n = int(n)
        if c == "I":
            heapq.heappush(Q1, (-n, idx))
            heapq.heappush(Q2, (n, idx))
            ans[idx]^=1
            idx+=1
        else:
            if n>0:
                while Q1:
                    num,i = heapq.heappop(Q1)
                    if ans[i]:
                        ans[i]^=1
                        break
            else:
                while Q2:
                    num, i = heapq.heappop(Q2)
                    if ans[i]:
                        ans[i] ^= 1
                        break
    answer = []
    while Q1:
        num, i = heapq.heappop(Q1)
        if ans[i]:
            answer.append(-num)
            ans[i] ^= 1
            break
    while Q2:
        num, i = heapq.heappop(Q2)
        if ans[i]:
            answer.append(num)
            break
    if len(answer):
        printf[tc] = f'{answer[0]} {answer[-1]}'
print('\n'.join(printf))