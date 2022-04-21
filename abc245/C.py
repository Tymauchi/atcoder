N, K = [int(i) for i in input().split()]

A_li = [int(i) for i in input().split()]
B_li = [int(i) for i in input().split()]

use_a = [0]*N
use_b = [0]*N

use_a[0] = 1
use_b[0] = 1

for i in range(N):
    if use_a[i-1]:
        if abs(A_li[i-1]-A_li[i]) <= K:
            use_a[i] = 1
        if abs(A_li[i-1]-B_li[i]) <= K:
            use_b[i] = 1
    if use_b[i-1]:
        if abs(B_li[i-1]-A_li[i]) <= K:
            use_a[i] = 1
        if abs(B_li[i-1]-B_li[i]) <= K:
            use_b[i] = 1

    if use_a[i]+use_b[i] == 0:
        print("No")
        exit()


print("Yes")
