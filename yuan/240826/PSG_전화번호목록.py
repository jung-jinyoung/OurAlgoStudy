# set 으로 바꾸면 검색속도가 훨씬 빠름. 

from collections import defaultdict


def solution(phone_book):
    dict = defaultdict(set)

    for numb in phone_book:
        dict[len(numb)].add(numb)

    key_list = list(dict.keys())

    for numb in phone_book:
        for key in key_list:
            if len(numb) > key and numb[:key] in dict[key]:
                return False

    return True