import unittest
import height_tree

class HeightTreeTest(unittest.TestCase):
    def test_check_height_tree(self):
        self.assertEqual(height_tree.height_tree("4 -1 4 1 1"), 3)
        self.assertEqual(height_tree.height_tree("-1 0 4 0 3"), 4)
        self.assertEqual(height_tree.height_tree("-1 0 1 0 3"), 3)

if __name__ == '__main__':
    unittest.main()
