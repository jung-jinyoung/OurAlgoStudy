# 카드 놓기

def dfs(depth, now_card):
    if depth == k:
        if not my_cards.get(now_card):
            my_cards[now_card] = 1
        return
        
    for card in basic_card:
        if cards[card] >=1: #카드가 남았다면
            cards[card] -= 1
            dfs(depth+1, now_card+card) # 현재 카드 사용
            cards[card] += 1



n = int(input())
k = int(input())

cards = dict()
for _ in range(n):
    card = input() # 그냥 문자열로 받기
    if cards.get(card): # 이미 존재하는 카드라면
        cards[card] += 1
    else:
        cards[card] = 1

basic_card = list(cards.keys())
my_cards = dict()
dfs(0, '')
    
print(len(my_cards))