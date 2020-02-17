class TreeNode:
    def __init__(self, key, parent=None, left=None, right=None, height=0):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        self.height = height


class AVLTree:
    def __init__(self):
        self.root = None

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def delete(self, root, key):

        # Step 1 - Perform standard BST delete
        if not root:
            return root

        elif key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right,
                                     temp.val)

            # If the tree has only one node,
        # simply return it
        if root is None:
            return root

            # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.Height(root.left),
                              self.Height(root.right))

        # Step 3 - Get the balance factor
        balance = self.GetBalance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and self.GetBalance(root.left) >= 0:
            return self.LL_Rotate(root)

            # Case 2 - Right Right
        if balance < -1 and self.GetBalance(root.right) <= 0:
            return self.RR_Rotate(root)

            # Case 3 - Left Right
        if balance > 1 and self.GetBalance(root.left) < 0:
            root.left = self.RR_Rotate(root.left)
            return self.LL_Rotate(root)

            # Case 4 - Right Left
        if balance < -1 and self.GetBalance(root.right) > 0:
            root.right = self.LL_Rotate(root.right)
            return self.RR_Rotate(root)

        return root

    def Height(self, x):
        if not x:
            return 0
        return x.height

    def NewNode(self, key):
        node = TreeNode(key)
        return node

    def LL_Rotate(self, x):  # LL
        y = x.right
        x.right = y.left
        y.left = x

        x.height = max(self.Height(x.left), self.Height(x.right)) + 1
        y.height = max(self.Height(y.left), self.Height(y.right)) + 1

        return y

    def RR_Rotate(self, x):  # RR
        y = x.left
        x.left = y.right
        y.right = x

        x.height = max(self.Height(x.left), self.Height(x.right)) + 1
        y.height = max(self.Height(y.left), self.Height(y.right)) + 1

        return y

    def LR_Rotate(self, x):  # LR
        x.left = self.LL_Rotate(x.left)
        return self.RR_Rotate(x)

    def RL_Rotate(self, x):  # RL
        x.right = self.RR_Rotate(x.right)
        return self.LL_Rotate(x)

    def GetBalance(self, x):
        if not x:
            return 0
        return self.Height(x.left) - self.Height(x.right)

    def Insert(self, x, key):  # return new root
        if not x:
            return self.NewNode(key)
        if key < x.key:
            x.left = self.Insert(x.left, key)
        elif key > x.key:
            x.right = self.Insert(x.right, key)

        else:
            return x

        x.height = 1 + max(self.Height(x.left), self.Height(x.right))

        bf = self.GetBalance(x)  # 平衡因子

        if (bf > 1) and (key < x.left.key):  # LL型
            return self.LL_Rotate(x)

        if (bf < -1) and (key > x.right.key):
            return self.RR_Rotate(x)

        if (bf > 1) and (key > x.left.key):
            return self.LR_Rotate(x)

        if (bf < -1) and (key < x.right.key):
            return self.RL_Rotate(x)

        return x



