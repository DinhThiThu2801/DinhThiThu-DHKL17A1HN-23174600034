class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def push(self, element):
        if not self.isFull():
            self.top += 1
            self.stack[self.top] = element
            print(f"Pushed {element} into the stack.")
        else:
            print("Stack is full. Cannot push element.")

    def pop(self):
        if not self.isEmpty():
            popped_element = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return popped_element
        else:
            print("Stack is empty. Cannot pop element.")
    
    def isEmpty(self):
        return True if (self.top == -1) else False
    
    def isFull(self):
        return True if (self.top == (self.capacity - 1)) else False


stack_capacity = 5 
my_stack = Stack(stack_capacity)

my_stack.push(3.14)
my_stack.push(2.71)
my_stack.push(1.618)
print(my_stack.pop()) 

print(my_stack.isEmpty())

print(my_stack.pop())

print(my_stack.isFull())