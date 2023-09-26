row, col = map(int, input().split(" "))
board = []
for _ in range(row):
    board.append(list(input()))

#
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

visited = set()
visited.add(board[0][0])

res = 0

def in_range(y, x):
    return 0 <= y < row and 0 <= x < col

def dfs(y, x, cnt):
    global res
    
    if res < cnt:
        res = cnt
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
    
        if not in_range(ny, nx):
            continue
        if board[ny][nx] in visited:
            continue
    
        visited.add(board[ny][nx])
        dfs(ny, nx, cnt+1)
        visited.remove(board[ny][nx])

    
dfs(0, 0, 1)
print(res)