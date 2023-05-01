def solution(n, words):
    answer = [0, 0]
    
    for i, word in enumerate(words):
        if i == 0:
            continue
        if word in words[:i]:
            answer[0] = i%n + 1
            answer[1] = i//n + 1
            return answer
        if list(word)[0] != list(words[i-1])[-1]:
            answer[0] = i%n + 1
            answer[1] = i//n + 1
            return answer
    
    return answer