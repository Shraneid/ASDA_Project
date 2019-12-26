import numpy as np

class BtreeNode:
    def __init__(self,leaf = False): 
        self.keys = []
        self.children = []
        #current number of keys
        self.leaf = leaf
class Btree:
    def __init__(self,t):
        self.t = t
        self.root = BtreeNode(leaf = True)


class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node)

def find(root, value):
    if root.val == value:
        return root
    elif root.val > value:
        return find(root.left, value)
    elif root.val < value:
        return find(root.right, value)

class AVL_Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree:
    def insert(self, root, key): 
      
        # Step 1 - Perform normal BST 
        if not root: 
            return AVL_Node(key) 
        elif key < root.val: 
            root.left = self.insert(root.left, key) 
        else: 
            root.right = self.insert(root.right, key) 
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                           self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and key < root.left.val: 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and key > root.right.val: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and key > root.left.val: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and key < root.right.val: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 

    def rightRotate(self, nToRot):
        left = nToRot.left
        backUp = left.right

        left.right = nToRot
        nToRot.left = backUp

        nToRot.height = 1 + max(self.getHeight(nToRot.left), self.getHeight(nToRot.right))
        left.height = 1 + max(self.getHeight(left.left), self.getHeight(left.right))

        return left

    def leftRotate(self, nToRot):
        right = nToRot.right
        backUp = right.left

        right.left = nToRot
        nToRot.right = backUp

        nToRot.height = 1 + max(self.getHeight(nToRot.right), self.getHeight(nToRot.left))
        right.height = 1 + max(self.getHeight(nToRot.right), self.getHeight(nToRot.left))

        return right

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def preorder(self, root):
        if not root:
            return

        print("{0} ".format(root.val), end="")
        self.preorder(root.left)
        self.preorder(root.right)

arr = np.arange(100)
np.random.shuffle(arr)
arr = list(arr)
print(arr)

root = Node(arr[0])
for val in arr[1:]:
    insert(root, Node(val))

print(find(root, 16).val)

avl = AVL_Tree()
root = None

for val in arr:
    root = avl.insert(root, val)

avl.preorder(root)

    
