def solution(inputString):
    l =[]
    l[0:]=inputString
    for i in range(len(l)):
        if l == l[::-1]:
            return ''.join(l)
        else:
            l.insert(len(l)-i,l[i])
    return inputString[inputString.index(-1)]


print(solution('moomm'))
