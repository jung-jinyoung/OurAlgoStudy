# 비밀번호 찾기
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) #N:저장사이트수, M:비번찾을 사이트 수

site = dict()
for _ in range(N):
    url, pwd = input().split()
    site[url] = pwd

for _ in range(M):
    print(site[input().strip()])