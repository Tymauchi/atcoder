from collections import defaultdict
import bisect
from sys import stdin; input = stdin.readline

N = int(input())
A_li = [int(i)-1 for i in input().split()]
Q = int(input())

dp = [[0]*(N+1) for _ in range(N)]

d = defaultdict(list)
for i in range(N):
    d[A_li[i]].append(i)

for _ in range(Q):
    L,R,X = [int(i)-1 for i in input().split()]
    li = d[X]
    l_ind = bisect.bisect_right(li, L-1)
    r_ind = bisect.bisect_right(li, R)
    print(r_ind-l_ind)
