import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
# 나무의 수 N개와 필요한 나무의 길이 M

trees = [*map(int, input().split())]
trees.sort()

# 자른 나무 길이의 합 
start, end = 1, max(trees)

while start < end :
    mid = (start + end) // 2
    total = 0

    for tree in trees : 
        if tree <= mid :
            continue
        
        total += tree - mid
    
    if total < M :
        end = mid -1
    else:
        start = mid + 1
print(end)

