import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value: # new value less than current value
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                temp = self.left
                temp.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                temp = self.right
                temp.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        else:
            if target < self.value: # target less than current value
                try:
                    temp = self.left
                    return temp.contains(target)
                except AttributeError:
                    return False
            else:
                try:
                    temp = self.right
                    return temp.contains(target)
                except AttributeError:
                    return False


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        try:
            self.in_order_print(node.left)
            print(str(node.value)+"\n", end='')
            self.in_order_print(node.right)
        except AttributeError:
            return

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        theQueue = Queue()
        theQueue.enqueue(node)
        while theQueue.len() != 0:
            node = theQueue.dequeue()
            print(str(node.value)+"\n", end='')
            if node.left is not None:
                theQueue.enqueue(node.left)
            if node.right is not None:
                theQueue.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        theStack = Stack()
        theStack.push(node)
        while theStack.len() != 0:
            node = theStack.pop()
            print(str(node.value)+"\n", end='')
            if node.left is not None:
                theStack.push(node.left)
            if node.right is not None:
                theStack.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
