import sys

input = sys.stdin.readline

row, col, r = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(row)]

for _ in range(r):
    for depth in range(min(row, col) // 2):
        y = depth
        x = depth
        # 행렬의 왼쪽 위 가장 자리 요쇼
        first = mat[y][x]

        # 왼쪽
        for i in range(depth + 1, row - depth):
            y = i
            temp = mat[y][x]
            mat[y][x] = first
            first = temp

        # 아래
        for i in range(depth + 1, col - depth):
            x = i
            temp = mat[y][x]
            mat[y][x] = first
            first = temp

        # 오른쪽
        for i in range(depth + 1, row - depth):
            y = row - i - 1
            temp = mat[y][x]
            mat[y][x] = first
            first = temp

        # # 위
        for i in range(col - depth - 2, depth - 1, -1):
            x = i
            temp = mat[y][x]
            mat[y][x] = first
            first = temp

for i in range(row):
    for j in range(col):
        print(mat[i][j], end=" ")
    print()
