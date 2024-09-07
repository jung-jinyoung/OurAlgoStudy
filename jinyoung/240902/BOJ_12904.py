import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

### rule
## 1. 문자열 뒤에 A를 추가한다
## 2. 문자열을 뒤집고 뒤에 B를 추가한다.

S = list(input().strip())
T = list(input().strip())

def check(my_long_str, my_short_str):


    while len(my_long_str) > len(my_short_str):

        last_char = my_long_str[-1]

        if last_char == "A":
            my_long_str.pop()
        else:
            my_long_str.pop()
            my_long_str.reverse()
        

    if my_long_str == my_short_str:
        return True
    else:
        return False



if len(S) >= len(T):
    result = check(S,T)
else:
    result = check(T,S)


if result :
    print(1)
else:
    print(0)