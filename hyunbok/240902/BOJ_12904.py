S = input()
T = input()
while len(T) > len(S):          # 슬라이싱 하다가 길이같아지면 break 
    if T[-1] == "A":
        T = T[:-1]              # 마지막 A만 버림
    else:
        T = T[:-1][::-1]        # 마지막 B를 버리고 뒤집는다

if T == S:
    print(1)
else:
    print(0)
