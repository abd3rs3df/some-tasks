class Stack:
    def __init__(self,size):
        self.stack=[]
        self.size=size

    def push(self, item):
        if len(self.stack) == self.size:
            print("Stack is full!!")
        else:
            self.stack.append(item)

    def pop(self):
        if self.stack == []:
            print("Stack is empty!")
            result = 0
        else:
            result = self.stack.pop()
        return result
    def disp(self):
        return self.stack[-1]

stack1=Stack(8)
stack2=Stack(4)
stack3=Stack(8)
exit = False
for i in range(4):
    stack1.push(int(input("stack 1:")))

for i in range(4):
    stack2.push(int(input("stack 2:")))

stack1.push(stack2.pop())
stack1.push(stack2.pop())
stack1.push(stack2.pop())
stack1.push(stack2.pop())
for i in  range(4):
    if stack1.disp()>stack2.disp()  :
        x =stack1.pop()
        stack1.push(stack2.pop())
        stack1.push(x)
    else:
        stack1.push(stack2.pop())

print(stack1.stack)