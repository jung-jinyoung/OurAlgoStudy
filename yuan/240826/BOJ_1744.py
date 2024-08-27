N = int(input())

pos_num = []
neg_num = []
res = 0
is_zero = False

for _ in range(N):
    num = int(input())
    if num == 1:
        res+=num # 1은 그냥 더하는게 이득
    elif num == 0:
        is_zero = True
    elif num >1:
        pos_num.append(num)
    elif num <= -1 : # -1은 -끼리 곱하면 +됨
       neg_num.append(num)

pos_num = sorted(pos_num, reverse=True)
neg_num = sorted(neg_num) # 절대값 기준으로 정렬

p_len = len(pos_num)
n_len = len(neg_num)

if p_len == 1:
    res+=pos_num[0]
elif p_len %2 == 0: # 짝수개일떄
    for idx in range(0,p_len,2):
        res+=pos_num[idx]*pos_num[idx+1]
else:
    for idx in range(0,p_len-1,2): # 홀수개일때
        res+=pos_num[idx]*pos_num[idx+1]
    res+=pos_num[-1] # 마지막수 더해주기

if n_len == 1:
    if not is_zero: # 0없을떄만
        res += neg_num[0]
elif n_len %2 ==0:
    for idx in range(0,n_len,2):
        res+=neg_num[idx]*neg_num[idx+1]
else:
    for idx in range(0,n_len-1,2):
        res+=neg_num[idx]*neg_num[idx+1]
    if not is_zero:
        res+= neg_num[-1]

print(res)
