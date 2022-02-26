class Node(object):
    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left


class Tree:
    def __init__(self):
        self.root = None
        self.check_serch=0

    def isEpmty(self):
        if self.root is None:
            return True

        else:
            return False

    def printTree(self):

        if self.isEpmty():
            print('it is epmty')

        else:
            self._loopPrint(self.root)


    def _loopPrint(self,temp):
        if temp is not None:
            print(temp.data)
            self._loopPrint(temp.left)
            self._loopPrint(temp.right)

    def insert(self, data):
        newNode = Node(data=data)
        current = self.root
        parent = None
        if self.isEpmty():
            self.root = newNode

        else :
            self._insert(newNode,self.root)


    def _insert(self,node,par):

        if node.data >=par.data :
            if par.right is None :
                par.right = node
                return
            else:
                par = par.right
                self._insert(node,par)


        elif node.data < par.data:
            if par.left is None:
                par.left = node
                return
            else:
                par = par.left
                self._insert(node, par)


    def serch(self,key):

        if self.root :
            self._serch(key,self.root)
            if self.check_serch == 1 :
                print('yes ... here you are')
            else:
                print('not found ...')

        else:
            print('is epmty')

    def _serch(self, key , par):

        if par :
            self._serch(key,par.left)
            if par.data ==key :
                self.check_serch=1
            self._serch(key,par.right)






tree = Tree()

tree.printTree()

tree.insert(12)
tree.insert(16)
tree.insert(14)
tree.insert(17)
tree.insert(4)
tree.insert(5)
tree.insert(3)

tree.insert(12)

tree.printTree()
tree.serch(12)
tree.serch(3)


