'''
투포인터 문제
이 경우 포인터 두개가 동시에 움직일 떄의 결과가 최적해일 수 있음

따라서 포인터가 멈춘 시점이 아니라 포인터로 가능한 경우의 수를 조회하며
최적해를 찾아나가는 코드(now<prev) 부분이 필요함

'''

n = int(input())
numbers = list(map(int, input().split()))

l = 0
r = n-1
prev = abs(numbers[l]+numbers[r])
ans = (l,r)
while l<r:
    now = numbers[l] + numbers[r]
    if abs(now) < prev:
        prev = abs(now)
        ans = (l,r)

    elif now > 0:
        r-=1
    elif now < 0:
        l+=1
    else:
        break
print(numbers[ans[0]],numbers[ans[1]])

# dic = dict()
# for i in range(0,n-1):
#     for j in range(i+1,n):
#         # print(lst[i],lst[j])
#         now = lst[i]+lst[j]
#         if now>0:
#             if now<ans:
#                 ans = now
#                 dic[ans] = (lst[i],lst[j])
#         else:
#             if -1*now<ans:
#                 ans = -1*now
#                 dic[ans] = (lst[i],lst[j])
# # print(dic)
# res = [v for k,v in dic.items() if k==ans]
# print(*res[0])