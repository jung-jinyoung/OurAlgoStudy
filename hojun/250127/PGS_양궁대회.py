def solution(n, info):
    global gap, answer
    gap, answer = -float('inf'), [0]*11
    
    def shoot(idx, arrow, score, array):
        global gap, answer
        if idx == 11:
            if score > gap:
                array[10] = arrow
                gap = score
                answer = array.copy()
                array[10] = 0
            elif score == gap:
                array[10] = arrow
                for i in range(10, -1, -1):
                    if answer[i] > array[i]:
                        break
                    elif answer[i] < array[i]:
                        answer = array.copy()
                array[10] = 0
                
            return
        now_score = 10-idx
        # 라이언이 점수를 최소한의 횟수로 얻기!
        if arrow >= info[idx]+1:
            array[idx] = info[idx]+1
            shoot(idx+1, arrow - (info[idx]+1), score + now_score, array.copy())
            array[idx] = 0
        
        # 라이언이 포기하기!
        shoot(idx+1, arrow, score - (now_score if info[idx] else 0), array.copy())
        
    shoot(0, n, 0, [0]*11)
    
    
    if gap > 0:
        return answer
    else:
        return [-1]
