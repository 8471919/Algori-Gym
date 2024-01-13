import sys

input = sys.stdin.readline

N = int(input())
distances = list(map(int, input().split()))
station = list(map(int, input().split()))

answer = 0

last = station[0]
dist = 0

# 첫 번째 주유소를 기준으로 보다 싼 주요소가 있는지 확인
for i in range(0, len(station)):
  if last > station[i]:
    answer += last*dist
    dist = 0
    last = station[i]

  if i != len(station)-1:
    dist += distances[i]

  if i == len(station)-1 and last <= station[-1]:
    answer += last*dist
  
print(answer)