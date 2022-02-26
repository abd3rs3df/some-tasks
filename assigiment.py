import math
from itertools import permutations

def solution(ce):
    def ch(li, li2):
        n = 0
        for i in range(len(li)):
            if li[i] != li2[i]:
                n += 1
        return n
    c = permutations(ce,len(ce))
    b = False
    n = 0
    g = 0
    for i in c:
        n =0
        x = list(i)
        for j in range(len(x)-1):

            list1 = []
            list2=[]
            list1[:0] = x[j]
            list2[:0] = x[j+1]
            print(list1,list2)
            if ch(list2,list1)== 1:

                n+=1

        if n == len(x)-1:

            return True

    return False
xx='a'
""""["aba", "bbb", "bab"]
["aba", "bab", "bbb"]
["bbb", "aba", "bab"]
["bbb", "bab", "aba"]
["bab", "bbb", "aba"]
["bab", "aba", "bbb"]"""
print(solution(["abc",
 "abx",
 "axx",
 "abc"]))

x =permutations(["abc",
 "abx",
 "axx",
 "abc"],4)
for i in x:
    print(type(i))

["abc",
 "abx",
 "axx",
 "abc"]
"""bon = False
k = 10
summ = 0
if inputString[0] == '.' or not inputString[0].isnumeric():
    return False
for i in range(len(inputString)):
    if inputString[i] == '.':
        bon = True


    else:
        bon = False

    if not bon:

        if inputString[i].isnumeric():
            if inputString[i] >= '0' and inputString[i] <= '9':
                summ = summ * k + int(inputString[i])

                print(summ)
        else:
            print('aa')
            return False

    elif summ > 255:
        print('gg')
        return False

    elif summ < 255:
        summ = 0"""
''''
str ='1(32)4(65(78)) '
while True :
    for i in range(len(str)):
        if str[i]=='(':
            x = i

    for i in range(len(str)):
        if str[i]==')':
            y = i
            


    print(str)
    """"str = str.replace(')', '')
    str = str.replace('(', '')"""
    str = str[:x]+str[y-1:x:-1]+str[y+1:]
    #str = str[:x]+ str[y:x:-1]+str[y:]

    if '(' not in str  :
        break
print(str)'''
"""
def solution(a):

    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[i]!=-1 :
                if a[i]<a[j]:
                    temp =a[i]
                    a[i]=a[j]
                    a[j]=temp
    return a"""

""""
    if ')' in inputString and '(' in inputString:


        for i in range(len(inputString)):
            if inputString[i]== ')':
                y = i

        for i in range(len(inputString)):
            if inputString[i]== '(':
                x = i
                break
        #x = inputString.index('(')
        y=inputString.index(')')
        print(x,y)
        c = inputString[x+1 :y ]
        inputString= inputString.replace(')','')
        inputString = inputString.replace('(', '')
        inputString=inputString[:x]+c+inputString[y-1:]

        print("c in one |||||",c)
        return  inputString[:x]+solution(c)+inputString[y-1:]
    else :
        x = inputString.index('(')
        y = inputString.index(')')
        c = inputString[y - 1:x:-1]
        inputString = inputString.replace('(', '')
        print(inputString)
        inputString = inputString.replace(')', '')
        print(inputString)
        inputString = inputString[:x] + c + inputString[y - 1:]
        print('in two |||||',inputString[::-1])
        return inputString[::-1]"""