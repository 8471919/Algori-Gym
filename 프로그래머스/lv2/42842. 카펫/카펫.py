def solution(brown, yellow):
    
    s = []
    
    for width in range(3, brown+yellow):
        height = (brown+yellow)/width
        if height % 1 == 0 and width >= height:
            s.append([width, int(height)])

    print(s)
    for el in s:
        if sum(el)*2 -4 == brown:
            return el
        
        
        