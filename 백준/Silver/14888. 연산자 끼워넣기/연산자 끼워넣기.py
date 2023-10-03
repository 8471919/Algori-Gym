import sys

# sys.stdin.readline()
# + - * /
input = sys.stdin.readline

n = int(input())
n_arr = list(map(int, input().split()))
op = list(map(int, input().split()))

max_value = int(-1e9)
min_value = int(1e9)


def dfs(index, total, plus, minus, mul, div):
    global max_value, min_value
    if index == n - 1:
        max_value = max(max_value, total)
        min_value = min(min_value, total)
        return

    if plus:
        dfs(index + 1, total + n_arr[index + 1], plus - 1, minus, mul, div)

    if minus:
        dfs(index + 1, total - n_arr[index + 1], plus, minus - 1, mul, div)

    if mul:
        dfs(index + 1, total * n_arr[index + 1], plus, minus, mul - 1, div)

    if div:
        dfs(index + 1, int(total / n_arr[index + 1]), plus, minus, mul, div - 1)


dfs(0, n_arr[0], *op)
print(max_value)
print(min_value)
