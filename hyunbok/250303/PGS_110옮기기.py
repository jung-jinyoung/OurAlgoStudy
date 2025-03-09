def solution(s):
    answer = []

    for x in s:
        stack = []
        cnt = 0
        for n in x:
            if n == '0' and len(stack) >= 2 and stack[-1] == stack[-2] == '1':
                stack.pop()
                stack.pop()
                cnt += 1
            else:
                stack.append(n)
        remaining = ''.join(stack)  # 남은 문자열
        pos = remaining.rfind('0')  # 삽입은 마지막 '0'의 뒤

        if pos == -1:  # 문자가 없으면 -1 을 반환
            new_str = "110" * cnt + remaining
        else:
            new_str = remaining[:pos + 1] + "110" * cnt + remaining[pos + 1:]

        answer.append(new_str)

    return answer
