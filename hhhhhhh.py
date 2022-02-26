def solution(min1, min2_10, min11, s):

    if s-min1==0:
         return 1
    else:
        s-=min1
        minee=1
    while True:
        if 0<minee<10:
            if s - min2_10<0:
                return minee
            elif s - min2_10==0 :
                return minee+1
            s-=min2_10
        else:
            if s - min11<0:
                return minee
            elif s - min11 == 0:
                return minee+1
            s-=min11

        minee+=1
min1= 1
min2_10= 2
min11=1
s= 6
print(solution(min1,min2_10,min11,s))
print(4^3)