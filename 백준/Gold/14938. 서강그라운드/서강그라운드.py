import sys
from collections import deque

input = sys.stdin.readline

# 모든 정점 간 최단 거리를 구해야함 -> 멘토님 말씀대로, 플로이드 와샬을 사용하면 될 듯
# 거리를 나타내는 인접행렬 -> 100x100 최대 10,000
# 노드의 아이템 개수를 나타내는 배열 -> 최대 100

n, m, r = list(map(int, input().split()))
items = list(map(int, input().split()))

dist = [[float('inf') for _ in range(n)] for _ in range(n)]

for i in range(0, r):
    a, b, d = list(map(int, input().split()))
    dist[a-1][b-1] = d
    dist[b-1][a-1] = d

for k in range(n):
    for row in range(n):
        for col in range(n):
            if row == col:
                dist[row][col] = 0
                continue
            dist[row][col] = min(dist[row][col], dist[row][k] + dist[k][col])

# print(dist)

max_item = [0 for _ in range(0, n)]

for i in range(0, n):
    for j in range(0, n):
        if dist[i][j] <= m:
            max_item[i] += items[j]

print(max(max_item))
