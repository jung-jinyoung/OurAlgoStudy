# 나무 자르기

N, M = map(int, input().split()) # N: 나무 수, M: 필요한 나무 길이
tree = list(map(int, input().split()))
# 가장 많은 양을 베려면 0인 높이에서 베야함
l = 0 
# 가장 적은 양을 베어 내려면 가장 큰 나무의 길이만큼 베야하지만 max(tree)는 시간이 많이 걸릴것 같아 최댓값으로 초기화
r = 2000000000 
result = 0 # 절단기에 설정했을 때 나무를 가져갈 수 있는 높이
while l <= r:
    m = (l+r)//2 #중간 값
    meter = 0 
    for t in tree:
        if t > m: # 나무 높이가 자르는 높이보다 크면
            meter += t - m #나무를 잘라서 윗부분을 더해줌
    if meter >= M: #만약 원하는 만큼의 나무를 잘랐다면?
        l = m + 1 #더 높은 구간에서 잘라봐야 하므로 l을 키워줌
        result = m
    else:   # 아직 원하는 만큼 못 잘라낸 경우
        r = m - 1   # 더 낮은 높이에서 나무를 절단해야하므로 r을 낮춰줌

print(result)