### 테케 3개만 맞은 죽지 않은 나의 코딩 실력 ㅋ

def solution(n, costs):
    info = [[0] * n for _ in range(n)]

    min_start = 0  ## 가장 작은 비용이 드는 섬
    min_sum = 0

    for s, t, cost in costs:
        info[s][t] = cost
        info[t][s] = cost

    for idx in range(n):
        if min_sum == 0:
            min_sum = sum(info[idx])
            min_start = idx

        if sum(info[idx]) < min_sum:
            min_start = idx
            min_sum = sum(info[idx])

    ## 가장 작은 다리 건설 비용이 드는 섬
    ## 해당 섬에 최종 비용 answer 에 추가
    answer = min_sum

    # 현재 이어진 섬
    arrival = [idx for idx in range(n) if info[min_start][idx] != 0]
    arrival.append(min_start)

    # 해당 섬에서 도달하지 않는 섬
    not_arrival = [idx for idx in range(n) if idx != min_start and info[min_start][idx] == 0]

    connected = [[0] * n for _ in range(n)]

    for temp in not_arrival:
        arr = []

        for idx in range(n):
            if info[temp][idx] > 0 and idx != temp:
                arr.append([temp, idx, info[temp][idx]])

        arr.sort(key=lambda x: (x[2], x[0], [1]))

        for start, end, cost in arr:
            if connected[start][end] == 0:
                answer += cost
                connected[start][end] = 1
                connected[end][start] = 1
                break
    return answer




