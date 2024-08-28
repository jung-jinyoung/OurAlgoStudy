
s = input()
t = input()
s_len = len(s)
def check(t):
    if len(t) < s_len:
        return
    if len(t)<0:
        return

    if t == s:
        print(1)
        exit()

    if t[-1] == 'A':
        check(t[:-1])
    elif t[-1] == 'B':
        check(t[:-1][::-1])


check(t)
print(0)