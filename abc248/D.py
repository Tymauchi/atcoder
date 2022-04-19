import bisect

N = int(input())
A_li = [int(i)-1 for i in input().split()]
Q = int(input())
d = [[] for _ in range(N+1)]

for i in range(N):
    d[A_li[i]].append(i)

for _ in range(Q):
    L,R,X = [int(i)-1 for i in input().split()]
    li = d[X]
    l_ind = bisect.bisect_right(li, L-1)
    r_ind = bisect.bisect_right(li, R)
    print(r_ind-l_ind)
