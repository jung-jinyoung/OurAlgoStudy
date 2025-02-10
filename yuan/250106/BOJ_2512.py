'''
도시 예산 정렬
어디부터 어디까지 상한액으로 줅건지
[150] 140 120 110 일때
l=0 r= 0
현재 윈도우 n= 1  윈도우s = 150
req = 520  > total 485 , over= 35

(윈도우의 합 - over )나누기 n이 다음의 값(r+1)보다 커야함

l=0 r=1
윈도우 2 / 합 = 290
290 - 35 = 255 255/2 = 127.5 가 다음값(r+1)보다 크니까 상한액 127
'''

n = int(input())
# 도시 십만이하
cities = list(map(int,input().split()))
total = int(input())

cities = sorted(cities, reverse=True)
over = sum(cities) - total

def check():
    '''
    현재 윈도우 n= 1  윈도우s = 150
    req = 520  > total 485 , over= 35
    (윈도우의 합 - over )나누기 n이 다음의 값(r+1)보다 커야함
    l=0 r=1
    윈도우 2 / 합 = 290
    290 - 35 = 255 255/2 = 127.5 가 다음값(r+1)보다 크니까 상한액 127
    '''
    idx = 0
    num = 1
    now = cities[0]
    while idx<n-1:
        if (now - over) // num >= cities[idx+1]:
            print((now-over)//num)
            exit()
        else:
            idx+=1
            num+=1
            now +=cities[idx]
    print(total//n)
    exit()

if over <=0:
    print(cities[0])
else:
    check()