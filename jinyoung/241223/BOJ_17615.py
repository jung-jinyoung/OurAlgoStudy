import sys

sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
my_balls = input().rstrip()

### 4 가지 전략
### 1. 빨간 공을 모두 오른쪽으로 이동
### 2. 파란 공을 모두 오른쪽으로 이동
### 3. 빨간 공을 모두 왼쪽으로 이동
### 4. 파란 공을 모두 왼쪽으로 이동

## 위의 네 가지 경우의 수 중 가장 작은 값이 정답 

red_balls = my_balls.count('R')
blue_balls = len(my_balls) - red_balls

### 첫번째 경우 
temp1 = red_balls - my_balls[::-1].find('B')
### 두번째 경우
temp2 = blue_balls - my_balls[::-1].find('R')
### 세번째 경우 
temp3 = red_balls - my_balls.find('B')
### 네번째 경우 
temp4= blue_balls - my_balls.find('R')

ans = min(temp1,temp2,temp3,temp4)
print(ans)