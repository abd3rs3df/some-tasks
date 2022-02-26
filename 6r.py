def ch2(lis, f):

    x=0
    lis1=lis.copy()

    lis1.pop(f)
    print(lis1)
    che=True
    for i in range(len(lis1) -1):
        if lis1[i] > lis1[i + 1]:
            che=False

    print(che)
    return che


def almostIncreasingSequence(sequence):
    x = 0
    for i in range(len(sequence)):
        if ch2(sequence, i):
            x += 1

    if  x >=1:
        return True
    else:
        return False


"""f=[1,3,4,1]
f.pop(2)
print(f)
f.pop(1)
print(f)"""
print(almostIncreasingSequence([1,3,2]))