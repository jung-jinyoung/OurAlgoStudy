from collections import defaultdict

def solution(survey, choices):
    value_dict = {1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    score_dict = defaultdict(int)
    for idx, choice in enumerate(choices):
        if choice < 4: # 4보다 작으면 suvey[0] 
            alpha = survey[idx][0]
        else:
            alpha = survey[idx][1]
        score = value_dict[choice]
        score_dict[alpha] += score 
    # print(score_dict)
    answer = ''
    if score_dict['R']>= score_dict['T']:
        answer += 'R'
    else:
        answer+='T'
    if score_dict['C']>= score_dict['F']:
        answer += 'C'
    else:
        answer+='F'
    if score_dict['J']>= score_dict['M']:
        answer += 'J'
    else:
        answer+='M'
    if score_dict['A']>= score_dict['N']:
        answer += 'A'
    else:
        answer += 'N'
        
        
    return answer