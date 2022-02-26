import string
def solution(text):
    ma= 0
    min =0
    l=[0,0]
    text = text+' ' if text[-1].isupper() or text[-1].islower() else text
    for i in range(len(text)):
        if text[i].isupper() or text[i].islower() :
            ma+=1
        elif abs(ma-min) > abs(l[0]-l[1]):
            l[0]=min
            l[1]=ma
            min = i + 1
            ma = min

        else:
            min = i+1
            ma=min


    return text[l[0]:l[1]]

print(solution('aa  vff  ggggggh'))

print(max('aa  vfvvvvvvf  gggggvvvvvvvvvvvvgh'.split(),key=len))

def solution(time):
    return 1<=int(time[0:2]) <=12 and 0<=int(time[2:]) <=60

