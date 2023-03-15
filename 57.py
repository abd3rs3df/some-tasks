def solution(names):
    for i in range(len(names)):
        if names[i] in names[:i]:
            j=1
            while names[i]+"("+str(j)+")" in names[:i]:
                j+=1
            names[i]+="("+str(j)+")"
    return names



print('heellldjk')

print(max("dd",
 "dd(3)",
 "dd(2)"))
names =["dd",
 "dd(1)",
 "dd(2)",
 "dd",
 "dd(1)",
 "dd(1)(2)",
 "dd(1)(1)",
 "dd",
 "dd(1)"]
res =["dd",
 "dd(1)",
 "dd(2)",
 "dd(3)",
 "dd(1)(1)",
 "dd(1)(2)",
 "dd(1)(1)(1)",
 "dd(4)",
 "dd(1)(3)"]
print(solution(names)==res)
print(solution(names))