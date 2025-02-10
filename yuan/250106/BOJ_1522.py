strs = input()
n = len(strs)  # 2
size = strs.count("a")

ss = strs + strs  # 원형처리 위해 두배
mincnt = ss[:size].count("b")
nowcnt = mincnt  # 현재 슬라이딩윈도우의 'b'개수
for i in range(2 * n - size):  #
    # 슬라이딩 윈도우: 하나씩 뒤로 이동
    if ss[i] == "b":
        nowcnt -= 1
    if ss[i + size] == "b":
        nowcnt += 1
    if nowcnt < mincnt:
        mincnt = nowcnt

print(mincnt)
