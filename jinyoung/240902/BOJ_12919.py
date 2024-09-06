import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# reverse 를 위한 리스트화
S = input().strip()
T = input().strip()
# S -> T 로 바꿈

def dfs(str1, str2):
    global result
    if len(str1) == len(str2) :
        if str1 == str2 :
            result = True
        return

    if str2[-1] == "B":
        str3= str2[::-1]
        dfs(str1,str3[:-1])

    elif str2[-1] == "A":
        # 그냥 A 제거
        str3 = str2[:-1]
        dfs(str1, str3)
        if str2[0] == "B":
            # 뒤집고 제거
            str3 = str2[::-1]
            str3 = str3[:-1]
            dfs(str1,str3)



result = False
dfs(S,T)

if result:
    print(1)
else:
    print(0)