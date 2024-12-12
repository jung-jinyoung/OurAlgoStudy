switch = int(input())
state = list(map(int,input().split()))
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]    # 남학생은 1, 여학생은 2

for gender,num in arr:
    if gender == 1:
        temp = num
        while temp<=switch:
            state[temp-1]^=1
            temp+=num
    else:
        l,r = num-1,num+1
        state[num - 1] ^= 1
        while l>0 and r<=switch:
            if state[l-1]==state[r-1]:
                state[l - 1]^=1
                state[r - 1]^=1
                l-=1
                r+=1
            else:
                break

idx = 0
while idx+20<switch:
    print(*state[idx:idx+20])
    idx+=20
print(*state[idx:])