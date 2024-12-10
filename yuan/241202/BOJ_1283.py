n = int(input())
sc = set()
for _ in range(n):
    first = input()
    word = first.split()
    check = False
    for idx, w in enumerate(word):
        if w[0].capitalize() not in sc:
            word[idx] = "[" + w[0] + "]" + w[1:]
            sc.add(w[0].capitalize())
            print(*word)
            check = True
            break
        if idx == len(word) - 1:
            for i, f in enumerate(first):
                if f != " " and f.capitalize() not in sc:
                    sc.add(first[i].capitalize())
                    first = first[:i] + "[" + first[i] + "]" + first[i + 1 :]
                    print(first)
                    check = True
                    break
            if not check:
                print(*word)
