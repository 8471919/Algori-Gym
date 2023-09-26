from itertools import product

def solution(users, emoticons):    
    answer = [0, 0]
    discount_arr = list(product([10,20,30,40], repeat=len(emoticons)))
    
    
    for discount in discount_arr:
        first_count = 0
        second_price = 0
        
        for user in users:
            price = 0
            for i, e in enumerate(emoticons):
                if discount[i] >= user[0]:
                    price += e * (100-discount[i])/100
            
            if price >= user[1]:
                first_count+=1
            else:
                second_price+=price

        if first_count == answer[0]:
            if second_price > answer[1]:
                answer[1] = second_price

        if first_count > answer[0]:
            answer[0] = first_count
            answer[1] = second_price                
        
    return answer
    
    