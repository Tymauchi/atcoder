N,M,K = [int(i) for i in input().split()]

dp = [[0]*(K+M+1) for _ in range(N)]

for i in range(1,K+1):
    if i <= M:
        dp[0][i] = 1

for i in range(N-1):
    for j in range(K+1):
        for k in range(1,M+1):
            dp[i+1][j+k] += dp[i][j]

print(sum(dp[N-1][:K+1])%998244353)
