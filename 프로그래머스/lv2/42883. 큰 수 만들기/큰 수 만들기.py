from collections import deque

def solution(number, k):
    number = list(number)
    stack = []
    
    for n in number:
        while stack and k > 0:
            if stack[-1] < n:
                k-=1
                stack.pop()
            else:
                break
        # 주의. k가 0아래로 내려갔는데도 append 될 수 있다.
        stack.append(n)
                
    # k개가 뒤에 남았다는 것은 동일한 숫자가 마지막에 남았다는 뜻이므로 마지막 동일한 숫자를 제거한다.
    return "".join(stack[:len(stack)-k])
            
