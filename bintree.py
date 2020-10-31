class BinTreeNode:
    def __init__(self, key, parent = None, left = None, right = None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
    
    # min, max access
    def maximum(self):
        x = self
        # take rightmost node
        while x.right is not None:
            x = x.right
        return x

    def minimum(self):
        x = self
        # take leftmost node
        while x.left is not None:
            x = x.left
        return x
    
    # successor
    def successor(self):
        if self.right is not None:
            return self.right.minimum()

        y = self.parent
        while y is not None and self == y.right:
            x = y
            y = y.parent

    # search into the subtree
    def search(self, key):
        if key == self.key:
            return self

        if key < x.key:
            # perform this control in advance
            if x.left is None:
                return None
            return x.left.search(key)
        else:
            # perform this control in advance
            if x.right is None:
                return None
            return x.right.search(key)
    
    # element-wise action walk
    # action is a lambda expression taking the current node

    def inorder_action(self, action):
        # recurse left
        if self.left is not None:
            self.left.inorder_action(action)

        # act
        action(self)

        # recurse right
        if self.right is not None:
            self.right.inorder_action(action)

    def preorder_action(self, action):
        # act
        action(self)

        # recurse left
        if self.left is not None:
            self.left.preorder_action(action)

        # recurse right
        if self.right is not None:
            self.right.preorder_action(action)

    def postorder_action(self, action):
        # recurse left
        if self.left is not None:
            self.left.postorder_action(action)

        # recurse right
        if self.right is not None:
            self.right.postorder_action(action)

        # act
        action(self)



class BinTree:
    def __init__(self, root = None):
        self.root = root

    def search(self, key):
        if self.root is None:
            return None
        return self.root.search(key)
    
    # min, max access

    def minimum(self):
        if self.root is None:
            return None
        return self.root.minimum()

    def maximum(self):
        if self.root is None:
            return None
        return self.root.maximum()

    # element-wise walk
    def inorder_action(self, action):
        if self.root is not None:
            self.root.inorder_action(action)

    def preorder_action(self, action):
        if self.root is not None:
            self.root.preorder_action(action)

    def postorder_action(self, action):
        if self.root is not None:
            self.root.postorder_action(action)

    # insertion
    def insert(self, key):
        z = BinTreeNode(key) # initialize an empty node
        y = None
        x = self.root
        
        # find optimal parent for z
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y

        if y is None: # in case the tree is empty, assign z as root
            self.root = z
        elif z.key < y.key: # emplace z on left side
            y.left = z
        else:               # emplace z on right side
            y.right = z



