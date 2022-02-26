class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
class ListLink():
    def __init__(self):
        self.head=None

    def printlist(self):
        current = self.head
        while current:
            print(current.data,end=' ')
            current=current.next
    def insertAtStart(self,data):
        newNode = Node(data)

        if self.head ==None :
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode

    def insertBetween(self,data):
        previousNode=self.head
        if previousNode.next ==None :
            print('not fuond')
            return
        else:
            newNode = Node(data)
            newNode.next=previousNode.next
            previousNode.next=newNode
    def insertAtEnd(self,data):
        newNode = Node(data)
        prevNode =self.head
        if self.head == None :
            self.head = newNode
        else:
            while prevNode.next!=None:
                 prevNode=prevNode.next
            prevNode.next=newNode
    def delete(self,key):
        temp =self.head
        if temp.next!=None:
            if temp.data==key:
               self.head=temp.next
               temp=None
               return self.head.data
            else:
                while temp !=None:
                    if temp.data==key:
                        break
                    prev=temp
                    temp=temp.next
                if temp ==None :
                    print('dffffff')
                    return
                prev.next =temp.next
                temp=None
        else:

            print('999')

    def check(self):
         temp = self.head
         if self.head != None :
             #self.head = self.head.next
             return temp
         else:
              return None








L=ListLink()
L.insertAtStart(1)
L.insertAtStart(2)
L.insertAtStart(3)
L.insertBetween(2)
L.insertAtbetween(7)
L.printlist()

'''
L2=ListLink()
L2.insertAtEnd(2)
L2.insertAtEnd(2)
L2.insertAtEnd(2)
L2.insertAtEnd(4)


L3=ListLink()
x = L2.check()
while  x !=None:
    if x % 2 == 0:
        L3.insertAtEnd(x)
    else:
        L3.insertAtEnd(x)
    x = L2.check()

x = L.check()
while  x !=None:
    while x.data !=None:
        if int(x.data) % 2 == 0:
            L3.insertAtStart(x.data)
        else:
            L3.insertAtStart(x.data)
        x.data = x.next

    x = L.check()

L3.printlist()

print()
L2.printlist()
L.printlist()


'''