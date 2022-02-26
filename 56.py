def solution(p):
    if p == 0:
        return 10
    elif p == 1:
        return 1

    n = []

    while 1 < p:
        for d in range(9, 1, -1):
            if p % d == 0:
                p /= d
                n.append(d)
                break
        else:
            return -1
    print(map(str,sorted(n)))
    return int(''.join(map(str, sorted(n))))

print(solution(450))

"""    while True:
        x = [int(i) for i in str(n*10-1)]
        y = functools.reduce(operator.mul,x)
        if y < product :
            n*=10
        else:
            break
    while True:
        x = [int(i) for i in str(n)]
        y = functools.reduce(operator.mul,x)
        if y ==product:
            l.append(n)
        print(x)
        if l!=[]:
            if len(str(l[0])) <len(str(l[-1]) ) :
                return min(l)
        n+=1
import functools
import operator
def solution(product):
    n=1
    l=[]
    while True:
        if product /n ==1:
            if n >9:
                return -1
            else :
                break
        if product%n==0 and  product//n < product :
            if solution(product//n)==-1 and product//n!=1:
                pass
            else:
                product //= n
                l.append(n)
                n = 0
        n+=1
    if l!=[]:
        if functools.reduce(operator.mul, l) == product:
            return l
        else:return -1
    else:
        return -1"""

l=[3, 3, 3, 3, 3]
ll=[]
ll.append(l[-1])
for i in range(len(l)-2,-1,-1):
    if l[i] * ll[0] <= 9:
        ll[0] = l[i] * ll[0]
    else:
        ll.insert(0, l[i])




