# 완전 탐색


# 피보나치 수열 마냥, 팰린드롬의 범위를 배열에 넣어서 비교하면 어떨까?

# 혹시 모를 중복을 위해 set으로 pal과 not_pal을 만들자.

# 만약 팰린드롬 범위보다 index가 작다면?
# 양쪽을 같은 개수만큼 떼어내면 팰린드롬임 (length 1인경우 고려)
# 이때는, pal에 append안해도됨

# 만약 팰린드롬 범위보다 index가 크다면?
# 양쪽이 같은 개수만큼 더해질 때, 그 수들이 팰린드롬이라면 팰린드롬임.
# 이 때는 pal에 현재 참고한 팰린드롬을 갱신하면됨.

# 팰린드롬 아닌 집합은 일단 보류.

# 만약 팰린드롬이 아닌 놈보다 index가 작다면?
# 양쪽을 같은 개수만큼 떼어내면 얘도 팰린드롬 아님.
# -> 이 때는 not pal에 append 안해도됨
# 다른 개수만큼 떼어내면 연산해야함.
# -> 이 때는 append하는게 좋긴함.


# 만약 팰린드롬이 아닌 놈보다 index가 크다면?
# 양쪽을 같은 개수만큼 더하면 얘도 팰린드롬 아님.
# -> 이 때는 현재 참고한 팰린드롬을 갱신.
# 다른 개수만큼 떼어내면 연산해야함.
# 

# 근데 이렇게 하면 연산 개많을거같은데... 질문이 100만개인데..

# dp로 접근하면?
# dp[시작 index][끝 index] 로 접근
# dp[equal][equal] = 1 무조건 팰린드롬.
# 
# dp[a][b] = dp[a+1][b-1] == 0 ? 0 : int(arr[a:b+1] == arr[a:b+1][::-1])
# dp[a][b] = dp[a-1][b+1] == 1 ? 1 : int(arr[a:b+1] == arr[a:b+1][::-1])
# dp[]

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

arr = input().split()

M = int(input())

dp = [[3 for _ in range(0, N)] for _ in range(0, N)]

# 아래서부터 위 순서로 탐색하면...?
for i in range(0, N):
    dp[i][i] = 1
    for dr in range(0, i):
        r = i-dr-1
        if dp[r+1][i-1] == 1:
            if arr[r] == arr[i]:
                dp[r][i] = 1
            else:
                dp[r][i] = 0
        elif dp[r+1][i-1] == 0:
            dp[r][i] = 0
        else:
            dp[r][i] = int(arr[r:i+1] == arr[r:i+1][::-1])

for _ in range(0, M):
    a, b = list(map(int, input().split()))    
    print(dp[a-1][b-1])
