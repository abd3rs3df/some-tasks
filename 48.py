def solution(s):
    l=[]
    l.append(s[0])
    s = s[1:]
    for i in s:
        if  i in l[len(l)-1]  :
            l[len(l)-1]= l[len(l)-1][0:] +i
        else:
            l.append(i)
    return ''.join([str(len(l[i])) + l[i][0] if len(l[i])!= 1 else   l[i][0]  for i in range(len(l))])
print(solution('aaabbbbc'))

