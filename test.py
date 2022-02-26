class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head=None

    def print(self):
        current = self.head
        while current:
            print(current.data , end=" ")
            current=current.next

# insert to the start of the linked list
    def insertAtStart(self,data):
        if self.head==None:
            newnode=Node(data)
            self.head=newnode

        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode

#inserting at the middle of two nodes:
    def insertbetween(self,previosnode,data):
        if previosnode.next == None:
            print(' you dummass -_- , '
                  'you cant use this method with empty list or list with one node  ')
            return
        else:
            newnode=Node(data)
            newnode.next=previosnode.next
            previosnode.next=newnode

# inserting at the end of the linked list:
    def insertatend(self,data):
        newnode=Node(data)
        prevnode=self.head
        if self.head==None:
            self.head=newnode

        else:
            while prevnode.next != None:
                prevnode=prevnode.next
            prevnode.next=newnode


#delete node based on key :
    def deletenode(self,key):
        temp=self.head
        if temp.next is not None:
            if temp.data == key:
                self.head=temp.next
                temp=None
            else:
                while temp.next != None:
                    if temp.data == key:
                        break
                    prev=temp
                    temp=temp.next

                if temp==None:
                    print('the key you intered in not in the linked list ')
                    return

                prev.next=temp.next
                temp=None
                return

#to delete the first node in th linked list
    def delfirst(self):
        temp=self.head
        self.head=temp.next

#delete the first node in a linked list (simplified)
    def delsimp(self):
        self.head=self.head.next

    #recursive searching
    def recsearch(self,node,key):
        if node == None:
            return False
        if node.data == key:
            return True
        return self.recsearch(node.next,key)

    def delsimpeere(self):
         self.head=self.head.next

    def delfirstprov(self):
        temp=self.head
        self.head=temp.next
        print( temp.data)
        temp=None

#testing our code
list = LinkedList()
list.insertAtStart(5)
list.insertAtStart(7)
list.insertbetween(list.head,55)
list.insertatend(65)
list.delfirstprov()
list.print()