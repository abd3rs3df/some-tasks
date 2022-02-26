def solution(n):
    n = n.split('-')
    b = False
    for i in n :
        if len(i)==2:
            if len(n)==6 and i[0].isnumeric() or 65<=ord(i[0])<=70 and i[1].isnumeric() or 65<=ord(i[1])<=70  :
                     b= True
            else: return False
        else:
            return False
    return b

print(solution('12-34-56-78-9A-B'))


print(ord('F'))

