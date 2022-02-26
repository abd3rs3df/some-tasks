def solution(bishop, pawn):
    l =[]
    x = int(bishop[1])
    for i in range(ord(bishop[0]),ord('h')+1):
        print(chr(i)+str(x))

        l.append(i+x)
        x+=1
    x = int(bishop[1])
    for i in range(ord(bishop[0]),ord('a')-1,-1):
        print(chr(i)+str(x))
        l.append(i+x)
        x-=1
    x=int(bishop[1])
    for i in range(ord(bishop[0]),ord('g')+1):
        print(chr(i)+str(x))
        l.append(i+x)
        x-=1
    x= int(bishop[1])
    for i in range(ord(bishop[0]),ord('a')-1,-1):
        print(chr(i)+str(x))

        l.append(i+x)
        x+=1
    return ord(pawn[0])+int(pawn[1]) in l

print(solution("b1",'d3'))

