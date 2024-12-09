# 볼 모으기

# 빨 오, 빨 왼, 파 오, 파 왼 4가지 경우 최소 찾기
N = int(input())
data = input()
answer = N
red = data.count('R')
blue = N - red

temp1 = red - data.find('B') # 왼쪽으로 옮겨야하는 빨간색 수
temp2 = blue - data.find('R') # 왼쪽으로 옮겨야하는 파란색 수
temp3 = red - data[::-1].find('B')
temp4 = blue - data[::-1].find('R')