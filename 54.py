def solution(inputString):

    m = 0
    g = ''.join([i if i.isdigit() else ' ' for i in inputString ]).split()
    for i in g:
       m+=int(i)
    return m
print(m)