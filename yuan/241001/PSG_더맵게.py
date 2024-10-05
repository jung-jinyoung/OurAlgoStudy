# heap 비면 인덱스에러(런타임에러) 발생

import heapq


def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    n = len(scoville)
    cnt = 0
    while heap:
        fis_num = heapq.heappop(heap)
        if fis_num >= K:
            return cnt

        elif cnt > n or len(heap) <= 0:
            return -1
        sec_num = heapq.heappop(heap)
        new_num = fis_num + 2 * sec_num
        heapq.heappush(heap, new_num)
        cnt += 1
