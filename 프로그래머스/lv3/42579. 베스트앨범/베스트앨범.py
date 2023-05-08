def solution(genres, plays):
    answer = []
    
    for_genre = {}
    
    hash_table = {}
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in hash_table:
            hash_table[g] = []
        hash_table[g].append((i, p))

    for g, p in zip(genres, plays):
        if g not in for_genre:
            for_genre[g] = 0
        for_genre[g] += p
        
    for k, v in sorted(for_genre.items(), key=lambda x: x[1], reverse=True):
        for i, p in sorted(hash_table[k], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(i)
            

    return answer
    