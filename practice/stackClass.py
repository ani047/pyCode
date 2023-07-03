class Stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")
        
    def is_empty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")
        

stack=Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
print(stack.size())
print(stack.peek())
item = stack.pop()


print(stack.size())
print(stack.is_empty())
