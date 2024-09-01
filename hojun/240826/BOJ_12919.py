# A와 B 2

S = list(map(str, input().strip()))
T = list(map(str, input().strip()))
N = len(S)

def dfs(now):
    if len(now) == N:
        if now == S:
            print(1)
            exit()
        return

    if now[-1] == "A":
        dfs(now[:-1])        # 마지막 문자(A) 빼기
    if now[0] == "B":
        dfs(now[::-1][:-1])  # 뒤집어서 마지막 문자(B) 빼기

dfs(T)
print(0)