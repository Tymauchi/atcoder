N = int(input())
S = list(input())

vec = [[1,0], [0,-1], [-1,0], [0,1]]

ans = [0,0]
ind = 0
for i in S:
    if i == "S":
        ans[0] += vec[ind][0]
        ans[1] += vec[ind][1]
    else:
        ind += 1
        ind %= 4

print(*ans)
