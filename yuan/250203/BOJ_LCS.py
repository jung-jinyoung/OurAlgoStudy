"""
현재 중복 수열의 최대값은
str1 - 1글자 & str2 와 str1&str2 - 1글자 중
더 큰 중복 수열 값

str1의 길이만큼 str2 의 길이만큼 n*m 순회하면서
dp 배열 작성
하나 늘어날때마다 체크

"""

import sys

input = sys.stdin.readline


def find(str1, str2):
    n, m = len(str1), len(str2)
    # n,m 2차원 배열 만들기
    # str1의 i, str2 의 j번째 까지의 lcs저장
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            if str1[i] == str2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:  # 다를때는 한쪽 문자열 줄였을때 값 중 큰거
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

    return dp[n][m]


str1 = list(input().strip())
str2 = list(input().strip())

res = find(str1, str2)
print(res)
