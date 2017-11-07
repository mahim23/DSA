class BSTNode:

    def __init__(self, parent=None, key=None, left=None, right=None):
        self.parent = parent
        self.key = key
        self.left = left
        self.right = right

    def isLeftChild(self):
        if self.parent is None:
            return False
        if self.parent.left == self:
            return True
        return False

    def isRightChild(self):
        if self.parent is None:
            return False
        if self.parent.right == self:
            return True
        return False

    def hasLeftChild(self):
        if self.left is not None:
            return True
        return False

    def hasRightChild(self):
        if self.right is not None:
            return True
        return False

    def search(self, k):
        if self.key == k:
            return self
        elif self.key > k:
            if self.left is not None:
                return self.left.search(k)
            else:
                return None
        else:
            if self.right is not None:
                return self.right.search(k)
            else:
                return None

    def minimum(self):
        if self.left is None:
            return self
        return self.left.minimum()

    def maximum(self):
        if self.right is None:
            return self
        return self.right.maximum()

    def successor(self):
        if self.right is not None:
            return self.right.minimum()
        if self.parent is None:
            return None
        x = self
        y = x.parent
        while y is not None and x != y.left:
            x = y
            y = y.parent
        return y

    def predecessor(self):
        if self.left is not None:
            return self.left.maximum()
        if self.parent is None:
            return None
        x = self
        y = x.parent
        while y is not None and x != y.right:
            x = y
            y = y.parent
        return y

    def insert(self, k):
        if k <= self.key:
            if self.left is None:
                self.left = BSTNode(self, k)
                return
            else:
                return self.left.insert(k)
        else:
            if self.right is None:
                self.right = BSTNode(self, k)
                return
            else:
                return self.right.insert(k)

    def preOrder(self):
        print(self.key, end=" ")
        if self.left is not None:
            self.left.preOrder()
        if self.right is not None:
            self.right.preOrder()


class BST:

    def __init__(self):
        self.root = None

    def insert(self, k):
        if self.root is None:
            self.root = BSTNode(None, k)
            return
        self.root.insert(k)

    def delete(self, k):
        node = self.root.search(k)
        if node.left is None and node.right is None:
            if node.isLeftChild():
                node.parent.left = None
            elif node.isRightChild():
                node.parent.right = None
            else:
                self.root = None
        elif node.left is None and node.right is not None:
            if node.isLeftChild():
                node.parent.left = node.right
            elif node.isRightChild():
                node.parent.right = node.right
            else:
                self.root = node.right
        elif node.right is None and node.left is not None:
            if node.isLeftChild():
                node.parent.left = node.left
            elif node.isRightChild():
                node.parent.right = node.left
            else:
                self.root = node.left
        else:
            prd = node.predecessor()
            node.key = prd.key
            self.delete(prd.key)
            return

    def search(self, k):
        return self.root.search(k)

    def minimum(self):
        return self.root.minimum()

    def maximum(self):
        return self.root.maximum()

    def preOrder(self):
        self.root.preOrder()
        print()


def main():
    T = BST()
    T.insert(10)
    # T.preOrder()
    # T.insert(5)
    # T.preOrder()
    # T.insert(12)
    # T.preOrder()
    # print(T.minimum().key)
    # T.insert(15)
    # T.preOrder()
    # print(T.maximum().key)
    # print(T.search(17))
    # print(T.root.predecessor().key)
    # T.delete(12)
    # T.preOrder()
    # print(T.root.successor().key)
    T.insert(5)
    T.insert(12)
    T.insert(11)
    T.insert(13)
    T.insert(15)
    T.insert(14)
    T.preOrder()
    print(T.search(11).key)
    T.insert(14)
    T.preOrder()
    print(T.search(11).predecessor().key)
    print(T.maximum().key)



if __name__ == '__main__':
    main()