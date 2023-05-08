def solution(numbers):
    ns = list(map(lambda x: str(x), numbers))
    
    ns = sorted(ns, key=lambda x: x*3, reverse=True)
        
    if ns[0] == "0":
        return "0"
        
    return "".join(ns)