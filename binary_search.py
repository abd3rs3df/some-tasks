def binary_search(lis, target):
    first =0
    last = len(lis)-1
    n=0
    while True:
        point = (first +last)//2
        if target == lis[point]:
            return point
        elif  lis[point] <target :
            first=point+1
        else :
            last=point-1
        n+=1


print(binary_search([1,2,3,4,5,6],3))


"""
10
3 akuof byyii dlust
1 xdozp
3 dlust luncl qzfyo
1 xdozp
3 akuof luncl vxglq
1 qzfyo
3 dlust vxglq luncl
0
3 dlust xveqd tfeej
0
3 qzfyo vxglq luncl
1 byyii
3 luncl xdozp xveqd
1 sunhp
3 byyii xdozp tfeej
1 qzfyo
3 dlust akuof tfeej
1 xveqd
3 vxglq dlust byyii
1 akuof"""