def solution(k, tangerine):
    dict = {}
    answer = 0
    for e in tangerine:
        if e not in dict:
            dict[e] = 1
        else:
            dict[e] += 1
    temp = sorted(dict.items(), key=lambda x: x[1])
    while k > 0 and len(temp) != 0:
        a = temp.pop()
        k -= a[1]
        answer+=1
    return answer