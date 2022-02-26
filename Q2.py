def remvoves(list):
    newlist=[]
    for item in list:
        if item not in newlist:
            newlist.append(item)
    return newlist

print(remvoves([1,3,4,4,4,5,5,6]))
