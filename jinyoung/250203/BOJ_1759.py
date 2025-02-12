import sys
from itertools import combinations

sys.stdin = open("input.txt","r")



## 유효한 경우인가 확인하는 함수 생성

def is_valid(password, l):
    arr = ['a','e','i','o','u']
    v_count = sum(1 for char in password if char in arr)
    c_count = l - v_count

    return v_count >= 1 and c_count >= 2

# 모든 조합의 경우의 수 확인 
def check(l, c, my_letters) : 

    for password in combinations(my_letters, l) :
        if is_valid(password, l):
            print("".join(password))


l, c = map(int, input().split(" "))
my_letters = input().split(" ")

# 오름차순 정렬
my_letters.sort()

check(l,c, my_letters)