X = 0
Y = 0

for _ in range(3):
    x, y = [int(i) for i in input().split()]

    X ^= x
    Y ^= y

print(X, Y)
