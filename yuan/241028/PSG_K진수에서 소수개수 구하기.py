from collections import defaultdict

def find_prime(digit):
    if digit <2:
        return False
    if digit ==2:
        return True 
    i = 2
    target_num = digit//2
    while i< target_num:
        v,e = divmod(digit,i)
        if e == 0:
            return False # 나머지 0이면 소수아님 
        i+=1
        target_num = v
    return True 

def solution(n, k):
    e_strs = ''
    while n > k:
        v, e = divmod(n,k)
        e_strs = str(e) + e_strs
        n = v
    e_strs = str(v) + e_strs
    e_lst = e_strs.split('0')
    answer = 0
    dict = defaultdict(int)
    for e in e_lst:
        if e!= '':
            digit = int(e)
            dict[digit]+=1
            # print(dict)
    for key in dict:
        res = find_prime(key)
        # print(key,res,dict[key])
        if res:
            answer+=dict[key]
    return answer

'''

def is_prime(n):
    """
    최적화된 소수 판별 함수
    - 2는 즉시 True 반환
    - 2보다 작거나 짝수는 즉시 False 반환
    - 제곱근까지만 홀수로 나누어 확인
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # 제곱근까지 홀수만 체크
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    """
    n을 k진수로 변환하고 조건에 맞는 소수의 개수를 반환
    
    최적화 포인트:
    1. 문자열 변환과 분할을 한 번의 순회로 처리
    2. 제너레이터 표현식으로 메모리 사용 최소화
    3. 불필요한 임시 변수 제거
    """
    # n을 k진수로 변환하면서 바로 처리
    digits = []
    while n:
        n, mod = divmod(n, k)
        digits.append(str(mod))
    
    # 역순으로 결합하고 0으로 분할
    k_num = ''.join(digits[::-1])
    
    # 0으로 분할하고 소수 판별
    return sum(
        is_prime(int(num))
        for num in k_num.split('0')
        if num and num != '0'
    )

'''
