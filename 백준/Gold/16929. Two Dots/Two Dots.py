import sys
from collections import deque

input = sys.stdin.readline

# 일단 든 생각. 대각선으로 이루어진 사이클도 존재하는가?




# 약간 미로찾기와 동일한 형식이라고 생각한다. 고로 bfs로 접근

N, M = list(map(int, input().split()))

table = []

for i in range(0, N):
  
  table.append(list(input())[:-1])
  

# 일단 모든 점을 대상으로 bfs 돌려보고, bfs를 돌릴 때 이미 방문한 녀석은 bfs를 돌리지 않도록

visited = [[0 for _ in range(0, M)] for _ in range(0, N)]

def bfs(y, x):
  dq = deque()
    
  # 방문 체크
  visited[y][x] = 1
  
  dq.append({"x": x, "y": y})
  
  # 위부터 시계방향, 위 > 오른 > 아래 > 왼
  dx = [0, 1, 0, -1]
  dy = [-1, 0, 1, 0]
  
  # 바로 직전 탐색한 노드를 저장하기 위한 변수
  before_que = deque()
  before_que.append({"x": x, "y": y})
  while dq:
    cur = dq.popleft()
    before = before_que.popleft()
    
    visited[cur["y"]][cur["x"]] = 1
    
    # print(cur)
    # print(f"before: {before}")

    for i in range(0, 4):
      # print(f"i : {i}")
      next_y = cur["y"]+dy[i]
      next_x = cur["x"]+dx[i]
      # 예외처리
      if next_y < 0 or next_x < 0 or next_y >= N or next_x >= M:
        # print(f"{next_y} {next_x} 예외")
        continue
      # 방문한 적이 있는 노드라면, 싸이클 형성 o
      if visited[next_y][next_x]:
        # 바로 직전 노드라면, 무시한다.
        if next_y == before["y"] and next_x == before["x"]:
          # print("무시")
          continue
        # 싸이클이 생성된 경우
        return True
      
      # 현재 노드와 다음 노드의 알파벳이 같고, 다음 노드를 방문한 적이 없다면
      if table[cur["y"]][cur["x"]] == table[next_y][next_x] and not visited[next_y][next_x]:
        # print(f"{next_y} {next_x} 다음")
        dq.append({"x": next_x, "y": next_y})
        before_que.append({"x": cur["x"], "y": cur["y"]})

is_break = 0
for row in range(0, N):
  if is_break == 1:
    break
  for col in range(0, M):
    if not visited[row][col]:
      # print()
      # print()
      # print(f"x : {col} y: {row}")
      visited = [[0 for _ in range(0, M)] for _ in range(0, N)]
      answer = bfs(row, col)
      
      if answer == True:
        print("Yes")
        is_break = 1
        break

if is_break == 0:
  print("No")