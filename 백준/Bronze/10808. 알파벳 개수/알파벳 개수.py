import sys

input = sys.stdin.readline

word = input().strip()

arr = [0 for _ in range(0, 26)]

for c in word:
    index = ord(c) - ord('a')
    arr[index] += 1

print(*arr)