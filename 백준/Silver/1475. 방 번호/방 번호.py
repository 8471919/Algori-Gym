import sys
import math

input = sys.stdin.readline

room_no = input().rstrip()

arr = [0 for _ in range(10)]

for c in room_no:
    index = ord(c) - ord('0')
    if index == 9:
        arr[6] += 1
        continue
    arr[index] += 1

arr[6] = math.ceil(arr[6]/2)

print(max(arr))