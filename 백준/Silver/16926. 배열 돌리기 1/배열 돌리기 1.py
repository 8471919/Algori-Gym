import sys

input = sys.stdin.readline

row, col, R = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(0, row)]

# R번 회전
for _ in range(0, R):
  # 바깥쪽부터 안쪽까지 하나씩 회전
  for depth in range(0, min(row, col) // 2):
    x = depth
    y = depth
    selected = table[y][x]

    # 왼쪽
    for i in range(depth+1, row-depth):
      y = i
      temp = table[y][x]
      table[y][x] = selected
      selected = temp
    
    # 아래
    for i in range(depth+1, col-depth):
      x = i
      temp = table[y][x]
      table[y][x] = selected
      selected = temp
        
    # 오른쪽
    for i in range(depth+1, row-depth):
      y = row - i - 1
      temp = table[y][x]
      table[y][x] = selected
      selected = temp
    
    # 위
    for i in range(depth+1, col-depth):
      x = col - i - 1
      temp = table[y][x]
      table[y][x] = selected
      selected = temp

for i in range(0, row):
  for j in range(0, col):
    print(table[i][j], end=" ")
  print()

