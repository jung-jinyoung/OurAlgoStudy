# 문자열 지옥에 빠진 호석
import sys
from collections import defaultdict

input = sys.stdin.readline

dir = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

N, M, K = map(int, input().split())  # 행, 열, 문제 수
data = [input().strip() for _ in range(N)]  # 격자 정보
problems = [input().strip() for _ in range(K)]  # 문제들

pos = defaultdict(list)  # 각 문자가 있는 위치들 리스트

# 각 문자 위치 저장
for i in range(N):
    for j in range(M):
        pos[data[i][j]].append((i, j))

# 이동 위치를 미리 계산
def move(i, j):
    return (i % N + N) % N, (j % M + M) % M

# 문제 탐색을 위한 DFS 함수
def dfs(problem, idx, i, j, memo):
    if idx == len(problem):
        return 1  # 문제 문자열을 완성한 경우

    if (idx, i, j) in memo:
        return memo[(idx, i, j)]

    count = 0  # 현재 탐색에서 찾은 경우의 수

    for di, dj in dir:
        ni, nj = move(i + di, j + dj)  # 이동 위치 계산
        if data[ni][nj] == problem[idx]:  # 다음 문자가 일치하는 경우
            count += dfs(problem, idx + 1, ni, nj, memo)  # 재귀 호출하여 탐색

    memo[(idx, i, j)] = count  # 현재 상태의 결과를 메모리에 저장
    return count

# 모든 문제에 대해 탐색 수행
for problem in problems:
    result = 0  # 문자열을 만들 수 있는 경우의 수
    memo = {}  # 메모이제이션을 위한 딕셔너리
    for i, j in pos[problem[0]]:  # 첫 번째 문자의 위치 순회
        result += dfs(problem, 1, i, j, memo)  # 첫 번째 문자에 대해 DFS 수행
    print(result)  # 최종 결과 출력
