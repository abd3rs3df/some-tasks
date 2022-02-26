import re
def solution(inputString):
    print(re.findall('^\d*',inputString))
    return re.findall('^\d*',inputString)[0]


x ='1243b'
print(solution('1243b'))
print(re.findall('^\d*',x))