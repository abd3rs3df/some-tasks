def solution(code):
    x=''
    for i in range(0,len(code),8):
        x+=chr(int(code[i:i+8],2))
    return