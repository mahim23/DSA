from lab5.BinarySearchTree import *


class AVLTreeNode(BSTNode):

    def __init__(self, parent=None, key=None, left=None, right=None):
        super(AVLTreeNode, self).__init__(parent, key, left, right)
        self.h = 1

    def insert(self, k):
        tmp = self
        s = []
        while True:
            if k <= tmp.key:
                if tmp.left is None:
                    tmp.left = AVLTreeNode(tmp, k)
                    tmp = tmp.left
                    s.append(0)
                    break
                else:
                    tmp = tmp.left
            else:
                if tmp.right is None:
                    tmp.right = AVLTreeNode(tmp, k)
                    tmp = tmp.right
                    s.append(1)
                    break
                else:
                    tmp = tmp.right

        z = tmp.parent
        while z is not None and abs(height(z.left) - height(z.right)) <= 1:
            if z.parent is None:
                pass
            elif z.isLeftChild():
                s.append(0)
            else:
                s.append(1)
            z.h = max(height(z.left), height(z.right)) + 1
            z = z.parent

        if len(s) >= 2 and z is not None:
            c1 = s.pop()
            if c1 == 1:
                y = z.right
            else:
                y = z.left
            c2 = s.pop()
            if c2 == 1:
                x = y.right
            else:
                x = y.left

            if c1 == 0 and c2 == 0:
                AVLTreeNode.rotateRight(y, z)
                z.h -= 1
            elif c1 == 1 and c2 == 1:
                AVLTreeNode.rotateLeft(z, y)
                z.h -= 1
            elif c1 == 0 and c2 == 1:
                AVLTreeNode.rotateLeft(y, x)
                AVLTreeNode.rotateRight(x, z)
                x.h += 1
                y.h -= 1
                z.h -= 1
            else:
                AVLTreeNode.rotateRight(x, y)
                AVLTreeNode.rotateLeft(z, x)
                x.h += 1
                y.h -= 1
                z.h -= 1

        while tmp is not None:
            if tmp.parent is None:
                return tmp
            tmp = tmp.parent


    def delete(self, k):

        s = []
        tmp = self.search(k)
        z = tmp.parent
        if tmp.left is not None and tmp.right is not None:
            pre = tmp.predecessor()
            tmp.key, pre.key = pre.key, tmp.key
            tmp = pre
        elif tmp.left is not None:
            tmp.key, tmp.left.key = tmp.left.key, tmp.key
            tmp = tmp.left
        elif tmp.right is not None:
            tmp.key, tmp.right.key = tmp.right.key, tmp.key
            tmp = tmp.right

        if tmp.isLeftChild():
            tmp.parent.left = None
            s.append(0)
        else:
            tmp.parent.right = None
            s.append(1)

        flag = 1
        while flag:

            while z is not None and abs(height(z.left) - height(z.right)) <= 1:
                if z.parent is None:
                    flag = 0
                    break
                elif z.isLeftChild():
                    s.append(0)
                else:
                    s.append(1)
                z.h = max(height(z.left), height(z.right)) + 1
                z = z.parent

            if len(s) >= 1 and z is not None and flag:
                c1 = s.pop()
                if c1 == 1:
                    y = z.left
                else:
                    y = z.right
                if height(y.left) >= height(y.right):
                    x = y.left
                    c2 = 0
                else:
                    x = y.right
                    c2 = 1

                if c1 == 1 and c2 == 0:
                    AVLTreeNode.rotateRight(y, z)
                    z.h = max(height(z.left), height(z.right)) + 1
                    y.h = max(height(y.left), height(y.right)) + 1
                    z = y
                elif c1 == 0 and c2 == 1:
                    AVLTreeNode.rotateLeft(z, y)
                    z.h = max(height(z.left), height(z.right)) + 1
                    y.h = max(height(y.left), height(y.right)) + 1
                    z = y
                elif c1 == 1 and c2 == 1:
                    AVLTreeNode.rotateLeft(y, x)
                    AVLTreeNode.rotateRight(x, z)

                    z.h = max(height(z.left), height(z.right)) + 1
                    y.h = max(height(y.left), height(y.right)) + 1
                    x.h = max(height(x.left), height(x.right)) + 1
                    z = x
                else:
                    AVLTreeNode.rotateRight(x, y)
                    AVLTreeNode.rotateLeft(z, x)

                    z.h = max(height(z.left), height(z.right)) + 1
                    y.h = max(height(y.left), height(y.right)) + 1
                    x.h = max(height(x.left), height(x.right)) + 1
                    z = x

        return z


    @staticmethod
    def rotateLeft(node1, node2):
        node2.parent = node1.parent
        if node1.parent is not None:
            if node1.isLeftChild():
                node2.parent.left = node2
            else:
                node2.parent.right = node2

        node1.right = node2.left
        if node2.left is not None:
            node2.left.parent = node1
        node2.left = node1
        node1.parent = node2

    @staticmethod
    def rotateRight(node1, node2):
        node1.parent = node2.parent
        if node2.parent is not None:
            if node2.isLeftChild():
                node1.parent.left = node1
            else:
                node1.parent.right = node1

        node2.left = node1.right
        if node1.right is not None:
            node1.right.parent = node2
        node1.right = node2
        node2.parent = node1


class AVLTree:

    def __init__(self):
        self.root = None

    def insert(self, k):
        if self.root is None:
            self.root = AVLTreeNode(key=k)
            return
        self.root = self.root.insert(k)

    def preOrder(self):
        if self.root is not None:
            self.root.preOrder()
        print()

    def delete(self, k):
        if self.root is None:
            return
        self.root = self.root.delete(k)


def height(node):
    if node is None:
        return 0
    return node.h


def main():
    T = AVLTree()
    T.insert(6)
    T.insert(2)
    T.insert(7)
    T.insert(3)
    T.insert(4)
    T.insert(5)
    T.preOrder()
    T.delete(2)
    T.preOrder()
    T.delete(3)
    T.preOrder()
    T.delete(4)
    T.preOrder()



if __name__ == '__main__':
    main()