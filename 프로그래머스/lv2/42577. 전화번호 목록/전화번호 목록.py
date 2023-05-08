# def solution(phone_book):
#     new_book = sorted(phone_book, key=lambda x: len(x))
    
#     for i, e in enumerate(new_book):
#         for v in new_book[i+1:]:
#             if v.startswith(e):
#                 return False
    
#     return True

    
def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1][:len(phone_book[i])].startswith(phone_book[i]):
            return False
            
    return True