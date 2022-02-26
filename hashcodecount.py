import numpy  as n
with open('in.txt') as inp :
    count=0
    aa = inp.readlines()
    print(type(aa))
    print(aa)
    for i in aa[1:]:
        if i[0]=='H':
            count+=1

print(count)



li =[(1,3),(4,5),(3,4),(6,5)]
print(li)
print(sorted(li))
  # for i in li:
  #       if i[0] not in