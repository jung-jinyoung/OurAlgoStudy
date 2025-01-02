# 단어 길이 10 이하
# 한문자 더하거나,빼거나, 다른 단어로 바꿨을 때 이전단어로 동일한지 카운트
'''
문자열 비교할때 정수(알파벳갯수) 배열이므로 list만들어서 순회
경우의 수 주의
diff_cnt 가 1이면 무조건 알파벳 하나가 다름
diff_cnt가 2일때 알파벳 두개가 다르거나 or "문자열 길이 동일할때" 알파벳 한개가 다름
'''
def check(word):
    cnt_l = [0] * 28
    for w in word:
        n = (ord(w) - ord('A'))
        cnt_l[n] += 1
    return cnt_l

def find(l,diff_cnt,len_l,len_s):
    if diff_cnt ==0:
        return True
    elif diff_cnt ==1:
        return True
    elif diff_cnt==2 and len_l == len_s:
        return True
    return False

    # 같은 종류 문자인지
    # 같은 개수인지
n = int(input())
s = input()
len_s = len(s)
lst = [ input() for _ in range(n-1)]
ans = 0

cnt_s = check(s)

for l in lst:
    cnt_l = check(l)# l의 알파벳 빈도 세기
    len_l = len(l)

    diff_cnt = 0
    for i in range(28):
        diff_cnt += abs(cnt_s[i] - cnt_l[i])
    if find(l,diff_cnt,len_l,len_s):
        ans+=1

print(ans)