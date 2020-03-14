# The common parent node code in binary tree

class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# If target is present in tree, then prints the ancestors and returns true, otherwise returns false
a = []
b = []


def printAncestors(root1, target1):
    if root1 == None:
        return False

    if root1.data == target1:
        return True

# If target is present in either left or right subtree of this node, then print this node
   
    if (printAncestors(root1.left, target1) or
            printAncestors(root1.right, target1)):
        a.append(root1.data)
        # print(a)
        return a

    # Else return False
    return False


def printAncestors1(root2, target2):
   
    if root2 == None:
        return False

    if root2.data == target2:
        return True

# If target is present in either left or right subtree of this node, then print this node
    if (printAncestors1(root2.left, target2) or
            printAncestors1(root2.right, target2)):
        b.append(root2.data)
        # print(b)
        return b

    # Else return False
    return False



# Binary tree
root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
root.right.right.left = Node(6)

printAncestors(root, 1)
printAncestors1(root, 3)
# finding the common parent of two targets
c = set(a) & set(b)
if c==set():
    print("no common node")
else:
    print(f'common parent nodes {c}')
