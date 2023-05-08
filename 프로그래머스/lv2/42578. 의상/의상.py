from itertools import combinations

def solution(clothes):

    hash_table = {}
    
    temp = []
    
    for v in clothes:
        if v[1] not in hash_table:
            hash_table[v[1]] = []
        hash_table[v[1]].append(v[0])
    
    print(hash_table)
    
    for k, v in hash_table.items():
        temp.append(len(v) + 1)
        print(v)

    sum = 1
    for e in temp:
        sum *= e
    
    print(temp)
    
    return sum-1