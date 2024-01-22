import sys

input = sys.stdin.readline

V = int(input())

adj_list = [[] for _ in range(0, V)]

for i in range(0, V):
  arr = list(map(lambda x: int(x)-1, input().split()))
  for j in range(1, len(arr)-1, 2):
    # 인접 리스트에 [정점, 거리]로 저장
    adj_list[arr[0]].append([arr[j], arr[j+1]+1])

# 간선에 가중치가 존재 -> 다익스트라?
# def dijkstra():

visited = [0 for _ in range(0, V)]

# def dfs(node):
#   visited[node] = 1
#   arr = []
#   for next in adj_list[node]:
    # print(next)
#     if not visited[next[0]]:
#       arr.append(dfs(next[0]) + next[1])
  
#   if len(arr) > 0:
#     return max(arr)
#   return 0
      
# answer = 0
# for i in range(0, V):
#   visited = [0 for _ in range(0, V)]
  # print(i)
#   answer = max(dfs(i), answer)
  

# 트리는 순환하지 않으니, 어느 정점도 루트 노드가 될 수 있다.
# 트리니까 중간에 끊겨있는 정점이 없을 것

# def dfs(i, dist):
#   visited[i] = 1
  
#   arr = [dist]  
#   for next in adj_list[i]:
#     # 파생 노드가 2개 이상이라면
#     if not visited[next[0]] and len(adj_list[i]) > 2:
#       arr.append(dfs(next[0], dist+next[1]))

#   # 연결된 정점의 개수가 3개 이상일 때, 
#   # 만약 현재 노드까지의 거리가 제일 작다면

#   return max(arr)
  

# answer = dfs(0)

# 다익스트라를 사용하여 간선이 하나밖에 없는 노드가 무조건 있을 것
# 간선이 하나밖에 없는 정점을 시작으로 다 최단거리를 구한 후... 어떻게 하면 되지 않을까?

answer = 0

# 모든 정점에서 모든 거리를 구하면 안된다.
def dfs(i, dist):
  global answer
  visited[i] = 1
  
  arr = []
  for next in adj_list[i]:
    # 파생 노드가 2개 이상일 때, 자식노드의 리턴 값 중 1, 2위
    # 로 큰 값을 더하자.
    if not visited[next[0]]:
      arr.append(dfs(next[0], next[1]))

  if len(arr) >= 2:
    # 오름차순 정렬
    arr.sort()
    a = arr.pop()
    b = arr.pop()
    answer = max(answer, a+b)
    # print(f"answer: {answer}")
    return max(a, b) + dist
  
  if len(arr) == 0:
    return dist
  
  temp = max(arr) + dist
  answer = max(temp, answer)
  return temp

dfs(0, 0)

print(answer)