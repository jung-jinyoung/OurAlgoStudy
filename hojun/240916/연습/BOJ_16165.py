# 걸그룹 마스터 준석이
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
team_mem, mem_team = {}, {}

for i in range(n):
    team = input().rstrip()
    num = int(input())
    team_mem[team] = []
    for j in range(num):
        member = input().rstrip()
        team_mem[team].append(member)
        mem_team[member] = team

for i in range(m):
    quiz, q = input().rstrip(), int(input())
    if q == 0:  # 팀 이름으로 퀴즈
        for mem in sorted(team_mem[quiz]):
            print(mem)
    else:  # 멤버 이름으로 퀴즈
        print(mem_team[quiz])