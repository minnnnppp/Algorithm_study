def solution(phone_book):
    phone_book.sort()
    cnt = 0
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            cnt+=1
    if cnt!=0: 
        return False
    else: return True