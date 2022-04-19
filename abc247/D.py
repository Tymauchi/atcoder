Q = int(input())

li = []
indx = 0
for _ in range(Q):
    ans = 0
    query = [int(i) for i in input().split()]
    if query[0] == 1:
        li.append(query[1:])
    else:
        while query[1] > 0:
            if query[1] < li[indx][1]:
                li[indx][1] -= query[1]
                ans += li[indx][0]*query[1]
                break
            else:
                ans += li[indx][0]*li[indx][1]
                query[1] -= li[indx][1]
                indx += 1
        print(ans)
