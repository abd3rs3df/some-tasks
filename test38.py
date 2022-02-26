def solution(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1+value2
    elif weight2 <= maxW and weight1 <= maxW:
        return max(value1,value2)
    elif  weight1> maxW and weight2<= maxW:
        return value2
    elif weight2 > maxW and weight1<= maxW:
        return value2
    else :
        return 0

x ='1'
x.isnumeric()
"""    while n!=9:
        x =upSpeed + summ
        if n == 0:
            print(n+1,upSpeed+summ,upSpeed-downSpeed)
        else:
            print(x,x-downSpeed)
            x += summ
        n+=1
        summ =upSpeed-downSpeed"""

print(solution(5,3,7))