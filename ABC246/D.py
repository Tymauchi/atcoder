N = int(input())

a = 1
while a**3 < N:
    a += 1

b = 0
ans = a**3
while a != 0:
    a -= 1
    while (a**2+b**2)*(a+b) < N:
        b += 1
    ans = min(ans, (a**2+b**2)*(a+b))

print(ans)
