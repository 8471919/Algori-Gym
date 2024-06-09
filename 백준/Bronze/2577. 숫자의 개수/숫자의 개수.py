import sys
input = sys.stdin.readline

res = 1
arr = [0 for _ in range(10)]

for _ in range(3):
    res *= int(input().strip())

for a in str(res):
    index = ord(a) - ord('0')
    arr[index] += 1

for i in arr:
    print(i)
    