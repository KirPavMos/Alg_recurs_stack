# Напишите класс Stack, который реализует основные
# операции стека

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return f"Stack({self.items})"

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack)
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.size())
print(stack.is_empty())
stack.pop()
print(stack.is_empty())