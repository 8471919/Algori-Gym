import sys
# from collections import deque

input = sys.stdin.readline

N = int(input())
R = int(input())

recommand = list(map(int, input().split()))

frame = []
# t = 0
for student in recommand:
  is_continue = 0
  # 이미 게시되어 있는지 확인
  for q in frame:
    if q[0] == student:
      q[1] += 1
      is_continue = 1
      break
  
  if is_continue:
    continue
    
  # 만약 게시되어 있지 않다면
  if len(frame) >= N:
    min_r = min(map(lambda x: x[1], frame))
    for i in range(0, len(frame)):
      if frame[i][1] == min_r:
        frame.pop(i)
        break
  
  frame.append([student, 1])

  
print(*sorted(list(map(lambda x: x[0], frame))))


