from collections import defaultdict
from itertools import combinations
import bisect


def solution(info, query):
    answer = []
    info_dict = defaultdict(list)

    for i in info:
        i = i.split()
        condition = i[:-1]
        score = int(i[-1])

        for r in range(5):
            combos = combinations(range(4), r)
            for c in combos:
                #               key는 해당조건or-로 치환한 스트링
                key = "".join([condition[j] if j in c else "-" for j in range(4)])
                info_dict[key].append(score)

    for value in info_dict.values():
        value.sort()  # 숫자 sort

    for q in query:
        q = q.replace("and ", "").split()
        key = "".join(q[:-1])  # and없애고 합침
        score = int(q[-1])

        if key in info_dict:  # key가 있으면 scores에서 score가 몇번쨰인지 확인
            scores = info_dict[key]
            # bisect.bisect_left(scores,score): lowerbound구하는 함수
            answer.append(len(scores) - bisect.bisect_left(scores, score))
        else:
            answer.append(0)

    return answer
