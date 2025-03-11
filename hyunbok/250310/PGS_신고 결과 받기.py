def solution(id_list, report, k):
    answer = [0] * len(id_list)
    arr = [[0] * (len(id_list)) for _ in range(len(id_list) + 1)]
    name = {}
    for idx, user in enumerate(id_list):
        name[user] = idx

    # 행이 신고한 사람 열이 신고 당한 녀석
    for line in report:
        A, B = line.split()
        if arr[name[A]][name[B]] == 0:
            arr[name[A]][name[B]] ^= 1
            arr[-1][name[B]] += 1

    message = []
    for i in range(len(id_list)):
        if arr[-1][i] >= k:
            message.append(i)
    for m in message:
        for user in range(len(id_list)):
            if arr[user][m]:
                answer[user] += 1

    return answer