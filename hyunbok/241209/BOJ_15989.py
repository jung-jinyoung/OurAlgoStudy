T = int(input())
for tc in range(T):
    n = int(input())
    ans = 1+n//2+n//3
    for i in range(1,n//3+1):
        ans+=(n-3*i)//2
    print(ans)