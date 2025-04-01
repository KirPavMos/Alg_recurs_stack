# Класс Stack, который реализует основные операции стека

class Stack:
    def __init__(self):
        self.items = []  # Инициализация стека как пустого списка

    def push(self, item):
        """Добавляет элемент на вершину стека."""
        self.items.append(item)

    def pop(self):
        """Удаляет и возвращает элемент с вершины стека.
        Вызывает исключение, если стек пуст."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Возвращает элемент с вершины стека без удаления.
        Вызывает исключение, если стек пуст."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """Проверяет, пуст ли стек."""
        return len(self.items) == 0

    def size(self):
        """Возвращает количество элементов в стеке."""
        return len(self.items)

    def __str__(self):
        """Строковое представление стека (для удобства отладки)."""
        return f"Stack({self.items})"

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack)        # Stack([10, 20, 30])
print(stack.peek()) # 30
print(stack.pop())  # 30
print(stack.pop())  # 20
print(stack.size()) # 1
print(stack.is_empty()) # False
stack.pop()
print(stack.is_empty()) # True