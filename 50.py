def solution(cell):
    k= 0
    if  9> int(cell[1])-1 >0 and 97 <=ord(cell[0])+2<=104  :
         k+=1
    if 9> int(cell[1])-2 >0 and 97 <=ord(cell[0])+1<=104 :
        k+=1

    if 9> int(cell[1])+1 >0 and 97 <=ord(cell[0])+2<=104  :
         k+=1
    if 9>int(cell[1])+2 >0 and 97 <=ord(cell[0])+1<=104 :
        k+=1


    if 9>int(cell[1])-1 >0 and 97 <=ord(cell[0])-2<=104  :
         k+=1
    if 9>int(cell[1])-2 >0 and 97 <=ord(cell[0])-1<=104 :
        k+=1

    if 9>int(cell[1])+1 >0 and 97 <=ord(cell[0])-2<=104  :
         k+=1
    if 9>int(cell[1])+2 >0 and 97 <=ord(cell[0])-1<=104 :
        k+=1

    return k

print(solution('1a'))