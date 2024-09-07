def func(T,S):
    global ans
    if ans or len(T) == len(S):
        if T == S:
            ans = 1
        return
    if T[0] == "A" and T[-1] == "A":
        func(T[:-1], S)
    elif T[0] == "A" and T[-1] == "B":
        return
    elif T[0] == "B" and T[-1] == "B":
        func(T[1:][::-1], S)
    else:                       # B - A 형태는 두가지 케이스 존재
        func(T[:-1], S)
        func(T[1:][::-1], S)

s = input()
t = input()
ans = 0
func(t,s)                       # 재귀를 돌려서 확인해보자
print(ans)