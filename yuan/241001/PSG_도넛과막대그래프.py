import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)  # 재귀 깊이 

def dfs(node, graph, visited):
    if graph[node]:
        num = len(graph[node])  # 이 노드에서 나가는 간선의 개수
    else:
        return 2  # 도넛 그래프
    
    if num == 2:
        return 3  # 팔자 그래프
    elif num == 1:
        new_node = graph[node][0]
        if new_node in visited:
            return 1  # 도넛 그래프
        else:
            visited.add(new_node)
            return dfs(new_node, graph, visited)

def solution(edges):
    graph = defaultdict(list)
    n = 1000000  # 노드의 최대 크기 (100만으로 설정)
    answer = [0, 0, 0, 0]  # [생성점, 도넛, 막대, 팔자]
    
    # 노드의 최대 번호 찾기
    n = 1000000
    
    # 노드가 받는 간선 개수
    out_cnt = [0] * (n + 1)

    # 그래프 구성
    for a, b in edges:
        graph[a].append(b)
        out_cnt[b] += 1  # b는 받은 간선 증가

    # 생성점 찾기 (출발 간선이 없는 노드 중에서 2개 이상의 간선 나가는 노드)
    start = -1
    for x in graph.keys():
        num = len(graph[x])
        if num >= 2 and out_cnt[x] == 0:
            start = x
            answer[0] = start  # 생성점 설정
            break
    
    if start == -1:
        return answer  # 생성점이 없으면 바로 리턴
    
    # start에서 시작하는 각 노드를 dfs로 탐색
    for v in graph[start]:
        visited = set([v])  # 방문한 노드 집합
        res = dfs(v, graph, visited)
        if res == 1:
            answer[1] += 1  # 도넛 그래프
        elif res == 2:
            answer[2] += 1  # 막대 그래프
        elif res == 3:
            answer[3] += 1  # 팔자 그래프
    
    return answer
