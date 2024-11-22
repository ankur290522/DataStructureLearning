import unittest
from depth_first_search import DepthFirstSearch, DFSMaizeEmptyError
from Stack import Stack
from StackErrorHandling import StackIsEmpty


class TestDepthFirstSearch(unittest.TestCase):
    def setUp(self):
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
    
    def test_reverse_string_empty(self):
        with self.assertRaises(StackIsEmpty) as context:
            self.stack.reverse_string()

    def create_maize(self):
        maize = [[0]*3 for row in range(3)]
        return maize

    def test_depth_first_search_single_node(self):
        maize = [[0]]
        dfs = DepthFirstSearch(maize)
        self.assertEqual(dfs.get_result(), [0])

    def test_depth_first_search_disconnected_graph(self):
        maize = self.create_maize()
        maize[0][1] = 1
        maize[1][0] = 1
        maize[2][2] = 1
        dfs = DepthFirstSearch(maize)
        self.assertEqual(dfs.get_result(), [0, 1])

    def test_depth_first_search_empty_graph(self):
        maize = []

        with self.assertRaises(DFSMaizeEmptyError) as context:
            DepthFirstSearch(maize)

    def test_predecessor(self):
        maize = self.create_maize()
        maize[0][1] = 1
        maize[1][0] = 1
        maize[1][2] = 1
        maize[2][1] = 1
        dfs = DepthFirstSearch(maize)
        self.assertEqual(dfs.get_result(), [0, 1, 2])
        
if __name__ == "__main__":
    unittest.main()
