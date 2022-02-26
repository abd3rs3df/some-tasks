def solution(a,b):
    m=0
    while a<=b:
        print(a,len(bin(a)[2:]))
        m+=bin(a)[2:].count('1')
        a+=1

    return m

print(solution(2,7))



x='12'
x='333'+x[:]
print(x)