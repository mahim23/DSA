class BinaryTreeNode:

    def __init__(self, parent=None, key=None, left=None, right=None):
        self.parent = parent
        self.key = key
        self.left = left
        self.right = right

    def preOrder(self):
        s = str(self.key) + " "
        if self.left is not None:
            s += self.left.preOrder()
        if self.right is not None:
            s += self.right.preOrder()
        return s

    def postOrder(self):
        s = ""
        if self.left is not None:
            s += self.left.postOrder()
        if self.right is not None:
            s += self.right.postOrder()
        s += str(self.key) + " "
        return s


def isOperand(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def parseTree(exp):
    exp = exp.split()
    ptr = BinaryTreeNode()
    root = ptr
    for i in exp:
        if i == "(":
            ptr.left = BinaryTreeNode(ptr)
            ptr = ptr.left
        elif i in ['+', '-', '*', '/', '%', '**']:
            ptr.key = i
            ptr.right = BinaryTreeNode(ptr)
            ptr = ptr.right
        elif isOperand(i):
            ptr.key = i
            ptr = ptr.parent
        elif i == ")":
            ptr = ptr.parent
    return root


def evaluate(op1, op2, op):
    if op == "+":
        return op1 + op2
    if op == "-":
        return op1 - op2
    if op == "*":
        return op1 * op2
    if op == "/":
        return op1 / op2
    if op == "%":
        return op1 % op2
    if op == "**":
        return op1 ** op2


def evalParseTree(node):
    if not isOperand(node.key):
        op1 = evalParseTree(node.left)
        op2 = evalParseTree(node.right)
        return evaluate(op1, op2, node.key)
    else:
        return int(node.key)


exp = "( ( ( 3 + 5 ) * 4 ) * 6 )"

root = parseTree(exp)
prefix = root.preOrder()
postfix = root.postOrder()
print("\nPrefix = ", prefix)
print("\nPostfix = ", postfix)
print("\nResult = ", evalParseTree(root))
