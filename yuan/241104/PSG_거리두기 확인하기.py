def solution(s):
    dict = { 'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    answer = ''
    # print(numbers)
    now_s=''
    for i in s:
        if i.isdigit(): # 숫자일떄
            if now_s !='':
                answer+=dict[now_s]
                now_s = ''
            answer+=i
        else: #문자일떄
            if now_s in dict:
                answer+=dict[now_s]
                now_s = ''
            now_s += i
    if now_s !='':
        answer+=dict[now_s]
    return int(answer)