S = input()
T = input()
T2 = T[::-1]

N = len(T) #T문자열 크기

stack = [S]

while stack:
  str = stack.pop() # 문자열 빼기
  if str == T:
    print(1)
    break

  case1 = str+'A'
  case2 = str[::-1]+'B'
  if case1 in T or case1 in T2:
    stack.append(case1)
  
  if case2 in T or case2 in T2:
    stack.append(case2)

else:
  print(0)