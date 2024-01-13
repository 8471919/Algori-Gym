import sys

input = sys.stdin.readline

N = int(input())
B = list(map(int, input().split()))

# 처음 생각 : 이진트리를 만들면 되는거 아닌가?

def binary_tree(value: int, arr: list, temp_B: list):
  if not temp_B:
    print(" ".join(str(i) for i in arr))
    return
  
  if len(arr) == 1:
    temp_B.remove(value)
  # print(f"arr : {arr}")
  left = value // 3
  right = value * 2
  
  # print(f"left:{left} / right:{right} / B:{temp_B}")
  if value % 3 == 0 and left in temp_B:
    temp_B.remove(left)
    arr.append(left)
    binary_tree(left, arr, temp_B[:])
    temp_B.append(left)

  
  if right in temp_B:
    temp_B.remove(right)
    arr.append(right)
    binary_tree(right, arr, temp_B[:])
    
  # print(f"B : {temp_B}")
  # print()
      
for i in B:
  binary_tree(i, [i], B[:])
