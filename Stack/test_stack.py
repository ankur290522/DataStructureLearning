import pytest
from Stack import Stack

class TestStack:
    @pytest.fixture(autouse=True)
    def create_stack(self):
        self.stack = Stack()

    def test_create_stack(self):
        assert self.stack.size() == 0

    def test_push(self):
        self.stack.push(1)
        assert self.stack.size() == 1
    
    def test_is_empty(self):
        assert self.stack.is_empty() == True
        self.stack.push(1)
        assert self.stack.is_empty() == False

    def test_peek(self):
        self.stack.push(1)
        assert self.stack.peek() == 1
    
    def test_pop(self):
        self.stack.push(1)
        assert self.stack.pop() == 1
        assert self.stack.size() == 0
    
    def test_print_stack(self):
        self.stack.push(1)
        self.stack.push(2)
        assert str(self.stack) == '[1, 2]'
    
    def test_reverse_string(self):
        self.stack.push('a')
        self.stack.push('b')
        self.stack.push('c')
        assert self.stack.reverse_string() == 'cba'
    
    def test_reverse_string_empty_stack(self):
        with pytest.raises(Exception) as exc_info:
            self.stack.reverse_string()
        assert str(exc_info.value) == 'CustomException: Stack is empty'
