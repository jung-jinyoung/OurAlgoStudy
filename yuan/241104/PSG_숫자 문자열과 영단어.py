def check(place):
    seats = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                seats.append([i, j])
            # print(place[i][j])
    n = len(seats)
    for x in range(n):
        for y in range(x + 1, n):
            # print(seats[x],seats[y])
            x1, y1, x2, y2 = seats[x][0], seats[x][1], seats[y][0], seats[y][1]
            dis = abs(x1 - x2) + abs(y1 - y2)
            if dis <= 2:
                if dis == 1:
                    return 0
                elif (x1 == x2) or (y1 == y2):
                    p, q = (x1 + x2) // 2, (y1 + y2) // 2
                    if place[p][q] == "O":
                        return 0
                else:
                    if place[x1][y2] == "O" or place[x2][y1] == "O":
                        return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        now = check(place)
        answer.append(now)
    return answer
