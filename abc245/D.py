import numpy as np

N, M = [int(i) for i in input().split()]
A = np.poly1d([int(i) for i in input().split()][::-1])
C = np.poly1d([int(i) for i in input().split()][::-1])

B = C/A

ans = [int(i) for i in B[0].c][::-1]
print(*ans)
