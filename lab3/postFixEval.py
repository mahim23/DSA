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


def isOperand(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


exp = input("Enter postfix: ")
exp = exp.split()

stack = []

for i in exp:
    if isOperand(i):
        stack.append(float(i))
    else:
        o2 = stack.pop()
        o1 = stack.pop()
        stack.append(evaluate(o1, o2, i))

print('Result is = ', stack.pop())
