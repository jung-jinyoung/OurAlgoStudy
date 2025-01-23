from collections import defaultdict


def money(sum, fees):
    if sum <= fees[0]:
        return fees[1]
    else:
        n, k = divmod(sum - fees[0], fees[2])
        if k > 0:
            return fees[1] + (n + 1) * fees[3]
        else:
            return fees[1] + n * fees[3]


def cal(t1, t2):
    # print(t1,t2)
    h1, m1 = t1.split(":")
    h2, m2 = t2.split(":")
    res = (int(h2) - int(h1)) * 60 + (int(m2) - int(m1))
    return res


def solution(fees, records):
    dict = defaultdict(list)
    answer = []

    for record in records:
        time, num, x = record.split(" ")
        dict[num].append(time)

    for k, v in dict.items():
        res_sum = 0
        n = len(v)
        # n이 짝수/ 홀수
        if n % 2 == 0:  # 짝수
            for i in range(1, n, 2):
                res = cal(v[i - 1], v[i])
                res_sum += res
        else:  # 홀수
            if n == 1:
                res = cal(v[0], "23:59")
                res_sum += res
            else:
                for i in range(1, n - 1, 2):
                    res1 = cal(v[i - 1], v[i])
                    res_sum += res1
                res2 = cal(v[n - 1], "23:59")
                res_sum += res2

        # print(k,res_sum)
        res_mon = money(res_sum, fees)
        # print(res_sum,res_mon)
        answer.append([k, res_mon])  # parint(k,res_mon)
    answer_sorted = sorted(answer, key=lambda x: x[0])

    ans = []
    for x in answer_sorted:
        ans.append(x[1])
    return ans
