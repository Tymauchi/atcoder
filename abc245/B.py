N = int(input())
A = [int(i) for i in input().split()]

check_li = [0]*2001
for i in range(N):
    check_li[A[i]] = 1

for i in range(2001):
    if check_li[i] == 0:
        print(i)
        break
