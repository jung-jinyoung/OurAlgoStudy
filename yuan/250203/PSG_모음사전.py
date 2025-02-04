"""
자리수개념으로 푸는것 맞음. 앞자리일수록 5의 거듭제곱 개수만큼 이전에 오는 문자들이 있음(가중치)  
단 현재 자리 기준 앞자리들이기때문에 현재자리까지 +1 해줘야함

실수하면 안되는 부분은
AA와 AAA를 (11000, 11100)로 뒀을때 매자리수에 똑같이 가중치 주면안됨

char가 있는부분에만 계산하기때문에
AA 는 : [0] 이전의 거듭제곱 +1, [1]이전의 거듭제곱 +1이고

AAA는 [0],[1],[2] 이전의 거듭제곱 +1 임 
그래서

    for i, char in enumerate(word):
        result += vowels[char] * weights[i] + 1  # +1은 자기 자신 포함
    
이렇게 풀면 word 길이안에서만 돌기때문에 실수할일이없음음

"""

dict = {"A": 1, "E": 2, "I": 3, "O": 4, "U": 5}


def multiple(x, i):  # mutiple: 0번째를 0,1,2,3,4(i)까지더함
    res = 0
    c = 0
    while c <= i:
        res += 5**c
        c += 1
    return res * x + 1


def solution(word):
    check = [-1] * 5
    n = len(word)
    for i in range(n):
        check[i] = dict[word[i]] - 1

    print(check)
    answer = 0

    for i in range(5):
        if check[i] >= 0:
            res = multiple(
                check[i], 4 - i
            )  # mutiple: 뒤에서부터 check[i]의 가중치 구하기
            answer += res

    return answer
