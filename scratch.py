def sum (x,y):
    return x+y
def min (n1,n2,n3):
    if n1 < n2 and n1 < n3 :
        return n1
    elif n2 < n1 and n2< n3 :
        return n2
    else:
        return n3

n1=float (input("enter the number : "))
n2=float (input("enter the number : "))
n3=float (input("enter the number : "))

print(min(n1,n2,n3))









