from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    # 1. 트럭의 무게와 다리가 견딜 수 있는 무게를 비교한다.
    # 2. 트럭을 한 대 출발 시킨다.
    # 3. 시간이 경과한다.
    
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    t = 0
    weight_sum = 0
    
    while bridge:
        t+=1
        # 시간이 경과했으므로 bridge에서 shift한다
        w = bridge.popleft()
        weight_sum -= w
        
        # 출발할 트럭이 남아있는지 확인한다
        if len(truck_weights) == 0:
            continue
        
        # 무게가 초과하는지 확인한다
        if weight < weight_sum + truck_weights[0]:
            bridge.append(0)
            continue
        # 무게가 초과하지 않는 경우, 트럭을 출발시킨다.
        w = truck_weights.popleft()
        bridge.append(w)
        weight_sum += w
    
    return t
    
    
#     while True:
#         t+=1
#         # bridge에 트럭이 있다면,
#         if len(bridge) > 0:
#             bridge
            
#         # 무게 초과시 다음 시간으로 넘김
#         if weight < sum(bridge) + truck_weights[0] :
#             continue
#         # 트럭이 남아있는지 확인
#         if len(truck_weights) == 0:
#             break
            
#         # 트럭이 남아있다면, 무게 초과가 아닐 경우 트럭 한 대 출발
#         bridge.append(truck_weights.popleft())
        
    