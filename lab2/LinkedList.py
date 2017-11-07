class LinkedList:
    """Defines a Singly Linked List.

    attributes: head
    """

    def __init__(self):
        """Create a new list with a Sentinel Node"""
        self.head = ListNode()

    def insert(self, val, pos):
        """Insert element val in the position after pos"""
        tmp = ListNode(val, pos.next)
        pos.next = tmp

    def delete(self, pos):
        """Delete the node following node pos in the linked list."""
        pos.next = pos.next.next

    def __str__(self):
        """ Print all the elements of a list in a row."""
        tmp = self.head
        string = ""
        while tmp.next:
            string += str(tmp.next.val) + ", "
            tmp = tmp.next
        return string[:-2]

    def insertAtIndex(self, val, i):
        """Insert value val at list position i. (The position of the first element is taken to be 0.)"""
        tmp = self.head
        index = 0
        while tmp:
            if index == i:
                self.insert(val, tmp)
                break
            else:
                index += 1
                tmp = tmp.next
        else:
            print("Index out of range")

    def search(self, val):
        """Search for value val in the list. Return a reference to the first node with value val; return None if no such node is found."""
        tmp = self.head
        while tmp.next:
            if tmp.next.val == val:
                return tmp.next
            else:
                tmp = tmp.next
        return None

    def len(self):
        """Return the length (the number of elements) in the Linked List."""
        tmp = self.head
        count = 0
        while tmp.next:
            count += 1
            tmp = tmp.next
        return count

    def isEmpty(self):
        """Return True if the Linked List has no elements, False otherwise."""
        if self.head.next:
            return False
        else:
            return True


class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: value, next. 
    """

    def __init__(self, val=None, nxt=None):
        self.val = val
        self.next = nxt


def main():
    L = LinkedList()
    L.insert(10, L.head)
    print('List is:', L)
    L.insert(12, L.head.next)
    print('List is:', L)
    L.insert(3, L.head)
    print('List is:', L)
    print('Size of L is', L.len())
    L.delete(L.head)
    print('List is:', L)
    L.delete(L.head.next)
    print('List is:', L)
    print('List is empty?', L.isEmpty())
    print('Size of L is', L.len())
    L.delete(L.head)
    print('List is empty?', L.isEmpty())
    print('Size of L is', L.len())
    L.insertAtIndex(2, 0)
    L.insertAtIndex(1, 0)
    print('List is:', L)


if __name__ == '__main__':
    main()
