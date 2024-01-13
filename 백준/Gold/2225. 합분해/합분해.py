import sys

input = sys.stdin.readline

N, K = list(map(int, input().split()))

# dp[N][K]
dp = [[0 for _ in range(200)] for _ in range(200)]

for row in range(0, len(dp)):
  for col in range(0, len(dp[0])):
    if row == 0:
      dp[row][col] = col+1
    elif col == 0:
      dp[row][col] = 1
    else:
      dp[row][col] = dp[row][col-1] + dp[row-1][col]
      
# print(dp)

print(dp[N-1][K-1] % 1000000000)