import unittest
from Others.AVL import AVLTree


class TestAVLTree(unittest.TestCase):

    def test_BST(self):
        nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]

        def isValidBST(node, lower=float('-inf'), upper=float('inf')):  # test BST

            if not node:
                return True

            key = node.key
            if key <= lower or key >= upper:
                return False

            if not isValidBST(node.right, key, upper):
                return False
            if not isValidBST(node.left, lower, key):
                return False

            return True

        root = None
        AT = AVLTree.AVLTree()
        for num in nums:
            root = AT.Insert(root, num)
        self.assertTrue(isValidBST(root))

    def test_AVL(self):
        nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
        root = None
        AT = AVLTree.AVLTree()
        for num in nums:
            root = AT.Insert(root, num)

        def Calculate(root):
            if root is None:
                return True
            if abs((AT.Height(root.left) - AT.Height(root.right))) > 1:
                return False

            return Calculate(root.left) and Calculate(root.right)

        self.assertTrue(Calculate(root))
