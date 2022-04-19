N = int(input())

name = [input().split() for _ in range(N)]

for i in range(N):
    flag = [0, 0]
    for k in range(2):
        for j in range(N):
            if name[i][k] in name[j] and i != j:
                flag[k] = 1


    if flag == [1, 1]:
        print('No')
        exit()

print('Yes')
