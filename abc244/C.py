N = int(input())

li = [0]*(2*N+1)

print(1)
li[0] = 1
for i in range(N):
    a = int(input())-1
    li[a] = 1

    for j in range(2*N+1):
        if li[j] == 0:
            print(j+1)
            li[j] = 1
            break
