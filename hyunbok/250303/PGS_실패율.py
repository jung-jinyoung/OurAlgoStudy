from collections import Counter
def solution(N, stages):
    answer = []
    stage_arived = Counter(stages)
    player = len(stages)
    for stage in range(1,1+N):
        if player == 0:
            answer.append((0,stage))
        else:
            answer.append((-1 * stage_arived[stage] /player,stage))
            player -= stage_arived[stage]
    answer.sort()
    return [i[1] for i in sorted(answer)]