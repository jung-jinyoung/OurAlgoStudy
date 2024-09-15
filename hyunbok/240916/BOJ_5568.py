from itertools import permutations
from collections import defaultdict
N = int(input())
K = int(input())
arr=[input() for _ in range(N)]
ans = defaultdict(int)
for case in permutations(arr,K):
    temp = "".join(case)
    ans[temp]+=1
print(len(ans.keys()))