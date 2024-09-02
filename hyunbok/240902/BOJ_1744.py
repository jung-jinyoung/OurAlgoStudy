N = int(input())
pos = []                    # 양수 넣는 리스트
neg = []                    # 음수 넣는 리스트
zeros = 0

for _ in range(N):
    num = int(input())
    if num < 0:
        neg.append(num)
    elif num > 0:
        pos.append(num)
    else:
        zeros+= 1           # 0유무 체크

pos.sort(reverse=True)      # 양수는 큰 수 끼리 곱해야 크니 내림차순
neg.sort()                  # 음수는 작은 수 끼리 곱해야 크니 오름차순
# print(pos,neg,[zeros])
ans = 0
i, j = 0, 0
# 양수 파트 => pos
while i < len(pos):
    if i + 1 < len(pos) and pos[i] * pos[i + 1] > pos[i] + pos[i + 1]:  # 남은게 두개 이상이고 곱이 합보다 크면
        ans += pos[i] * pos[i + 1]
        i += 2
    else:
        ans += pos[i]
        i += 1

# 음수 파트 => neg
while j < len(neg):
    if j + 1 < len(neg):                    # 음수는 합보다는 곱이 무조건 크다
        ans += neg[j] * neg[j + 1]
        j += 2
    else:
        if not zeros and j + 1 == len(neg): # 음수가 하나 남으면 0을곱해서 소거
            ans += neg[j]
        j += 1

print(ans)