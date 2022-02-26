

f=       [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]

l=[]
for j in range(len(f[0])-1):
    for i in range(len(f)-1):
        x=f[i][j:j+2]
        y=f[i+1][j:j+2]
        if [x,y] not in l :
            l.append([x,y])


print(len(l))
s = set()
print(s.add(12))
print(s)