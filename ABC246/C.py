N, K, X = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

A_div = [i//X for i in A]
A_mod = [i%X for i in A]

if sum(A_div) >= K:
    ans = sum(A) - K*X
else:
    A_mod.sort()
    ans = sum(A_mod[:sum(A_div)-K])

print(ans)
