import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

memory = list(map(int, input().split()))

cost = list(map(int, input().split()))


# 딱 봤을 때, 변수가 2개 이고 최소 비용을 구하는 문제이므로 DP 테이블을 생각.
# 하지만, m이 최대 천만, n이 최대 100이므로 최대 10억번의 연산이 이루어질 수 있다.
# 따라서 DP 테이블로 하면 시간 초과가 뜰 것이라고 판단.
# 비용당 바이트가 높은 녀석부터 처리하자 -> 단편화 문제 발생할 것 같음

col = N*100 + 1
row = N

# 최대 비용은 c의 최대 비용 x 앱의 개수
dp = [[0 for _ in range(0, col)] for _ in range(0, row)]

for r in range(0, row):
  for c in range(0, col):
    # 앱의 비용이 현재 비용보다 작거나 같다면
    if cost[r] <= c:
      # 비교해서 집어넣는다.
      dp[r][c] = max(dp[r-1][c], dp[r-1][c-cost[r]] + memory[r])
    else:
      dp[r][c] = dp[r-1][c]
# 찝찝한거 1. out of index
# 

# 인덱스가 높아질 수록 최적해가 나온다.
# 현재 코스트에서 이전 dp 테이블의 작성한 값이 높냐
# 아니면 현재 앱을 포함한 값이 더 높냐를 비교

# for i in dp:
#   print(i)


# for r in range(0, row):
#   is_finish = 0
#   for c in range(0, col):
#     if dp[r][c] >= M:
#       print(c)
#       is_finish = 1
#       break
#   if is_finish == 1:
#     break


for i in range(0, len(dp[-1])):
  if dp[-1][i] >= M:
    print(i)
    break
  