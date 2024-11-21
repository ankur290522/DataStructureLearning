import unittest
from depth_first_search import DepthFirstSearch, DFSMaizeEmptyError


class TestDepthFirstSearch(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()
