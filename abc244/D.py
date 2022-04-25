S = input().split()
T = input().split()

c = 0
for i,j in zip(S,T):
    if i == j:
        c += 1

if c in [0,3]:
    print("Yes")
else:
    print("No")
