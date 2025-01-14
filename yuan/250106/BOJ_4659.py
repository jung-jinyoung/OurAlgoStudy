'''
높은 품질의 조건들
모음(a,e,i,o,u) 하나를 반드시 포함해야함
    -> 포함 안하면 false
연속인 수 개수 세기
    -> 3개 연속은 false
    -> 2개 연속이면
        -> ee나 oo 면 pass
        -> 다른 수가 연속 2면 false
'''
import sys
input=sys.stdin.readline
alphas = {'a','e','i','o','u'}
def judge(strs):
    n = len(strs)
    word = []
    for s in strs:
        if s in alphas:
            word.append(1) # 모음
        else:
            word.append(0) # 자음
    if word.count(1) == 0: # 모음 한개도 없으면 false
        return False
    '''
    연속인 수 개수 세기
    -> 3개 연속은 false
    -> 2개 연속이면
        -> ee나 oo 면 pass
        -> 다른 수가 연속 2면 false
    '''
    seq = 1
    for i in range(1,n):
        if word[i] == word[i-1]:
            seq +=1
            if seq >=3:
                return False
        else: #else문으로 되어있어서 마지막 글자들이 연속인 경우 체크못함
            if seq == 2:
                if strs[i-1] == strs[i-2]:
                    if strs[i-1] != 'o' and strs[i-1] != 'e':
                        return False
            seq = 1 # 다 아니면 다시 복구
    if seq == 2: # 다 끝났을때 맨뒤 글자들도 체크 해줘야함
        if strs[i] == strs[i - 1]:
            if strs[i - 1] != 'o' and strs[i - 1] != 'e':
                return False
    return True

while True:
    strs = input().strip()
    if strs == 'end':
        exit()
    if judge(strs):
        print(f'<{strs}> is acceptable.')
    else:
        print(f'<{strs}> is not acceptable.')

