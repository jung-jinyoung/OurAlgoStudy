'''
이분탐색할때 
구해야하는 값이 리스트 내부에 있는 값인지 
or
조건에 따라 리스트 내부에 없어도 되는지 확인하기 

h-index는 조건에 맞는 결과가 리스트 내부의 값이 아닐수도 있음
괜히 l과 r 나눠서 조건 나누지 말고
while l<=r 로 하나의 값을 찾으면 쉽게 해결가능함함


'''

def solution(citations):
    n = len(citations)
    cit = sorted(citations)
    l,r = 0,n
    # mn,mx = cit[0],cit[-1]
    while l<=r:
        m = (l+r)//2 
        quote_num = 0
        for i in cit:
            if i >=m:
                quote_num+=1 
        if quote_num >=m:
            l = m+1
        else:
            r = m-1
    return r
