from StackErrorHandling import StackIsEmpty

class Stack:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        return str(self.items)
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return not self.items
    
    def push(self, value):
        self.items.append(value)
    
    def peek(self):
        return self.items[-1]
    
    def pop(self):
        return self.items.pop()
    
    def reverse_string(self):
        if self.is_empty():
            raise StackIsEmpty
        return ''.join(self.items[::-1])
    
    def read_elements_as_list(self):
        return self.items
    