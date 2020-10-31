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
    
    # transplant node u and replace with v
    def transplant(self, u, v):
        p = u.parent

        if p is None:
            self.root = v    # replace root if u is root

        # identify if u belongs to left or right, then replace with the correct one
        elif u == p.left:
            p.left = v 
        else:
            p.right = v

        if v is not None:
            v.parent = p     # assign same parent as u

    # delete a node z
    def delete(self, z):
        if z.left is None:  # no left child
            self.transplant(z, z.right) # just replace with right one

        elif z.right is None: # only left child
            self.transplant(z, z.left) # just replace with left one

        else:  # two children
            self.delete_with_two_children(z)

    def delete_with_two_children(self, z):
        y = z.right.minimum() # find minimum over right child

        if y.parent != z: # if y is not a direct child of z
            self.transplant(y, y.right) # make y the z.right subtree root
            y.right = z.right
            y.right.parent = y

        self.transplant(z, y) # replace z with y
        y.left = z.left  # fix dependencies
        y.left.parent = y
