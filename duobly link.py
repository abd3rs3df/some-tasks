class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkList():
    def __init__(self):
        self.head = None
        self.tail =None
        self.count = 0

    def printList(self):
        current = self.head
        while current :
            print(current.data , end=' ')
            current=current.next
    def printListBack(self):
        current = self.tail
        while current :
            print("\033[93m {}\033[00m".format(current.data)  , end=' ')
            current=current.prev

    def append(self, data):
        """ Append an item to the list. """
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete(self,data):
        current =self.head

        if current is None :
            return

        elif current.data is  data:
            self.head = current.next
            self.head.prev =None

        elif self.tail.data is data :
            self.tail = self.tail.prev
            self.tail.next = None

        else :
            while current :
                if current.data is data :
                    current.next.prev=current.prev
                    current.prev.next = current.next
                    break
                current=current.next

            else:
                print('not found')


    def insertAtStart(self,data):
        current = self.head
        newNode =Node(data)
        if self.head is None:
            self.head=newNode
            self.tail =newNode

        else:
            newNode.next = self.head
            self.head = newNode
            current.prev = newNode

    def insertAtEnd(self, data):
        current = self.tail
        newNode = Node(data)
        if self.head is None:
            self.head=newNode
            self.tail =newNode

        elif  self.tail.next is None:
            newNode.prev = self.tail
            self.tail = newNode
            current.next= newNode


    def insertAtbetween(self,data):
        current = self.head
        newNode =Node(data)

        if self.head.next is None:
            self.head=newNode
            self.tail =newNode

        else:
            newNode.next=current.next
            current.next.prev=newNode
            current.next = newNode
            newNode.prev = current

    def get_evrey_element(self):
        current = self.head

        if current is None:
            return
        else:
            data1 = self.head.data

            if self.head != None:

                self.head = current.next
                if self.head :
                    self.head.prev = None
                return data1
            else:
               return  None


    def get_evrey_element2(self):
        current = self.tail

        if current is None:
            return
        else:
            data1 = self.tail.data

            if self.tail != None:

                self.tail = current.prev
                if  self.tail !=None:
                    self.tail.next = None
                return data1
            else:
               return  None

    def printQ(self):
        current = self.head

        i = 0
        while current and i<10 :
            print(current.data, end=' ')
            if current.data % 2 == 0:
                if current.prev != None:
                    current = current.prev

            else:
                if current.next !=None :
                    if current.next.next  != None  :
                        current = current.next.next
            i+=1


    def sort(slef):
        current = slef.tail

        i =1
        while current != None:
            current2 = slef.head
            while current2 != None:
                temp = current2.data
                if current2.next !=None:
                    if current2.data > current2.next.data:
                        current2.data =current2.next.data
                        current2.next.data =temp

                if current2.next != None:
                    i+=1
                current2=current2.next
            if current.prev  != None:
                i+=1

            current=current.prev
    def sort_test(self):
        temp= self.head.data
        self.head.data = self.head.next.data
        self.head.next.data = temp



Link = DoublyLinkList()
Link.append(9)
Link.append(6)
Link.append(1)
Link.append(3)
Link.append(4)
Link.append(5)

LinkO= DoublyLinkList()
LinkE =DoublyLinkList()



while Link.head :
    x = Link.get_evrey_element()
    if x %2 == 0:
        LinkE.append(x)
    else:
        LinkO.append(x)



LinkE.printList()
print()
LinkE.sort()
print()
LinkE.printList()
print()
LinkO.printList()
print()
LinkO.sort()
print()
LinkO.printList()




