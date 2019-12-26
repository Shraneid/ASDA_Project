import numpy as np

class BTreeNode(object):
    def __init__(self, t, isLeaf):
        self.keys = []
        self.t = t
        self.children = []
        self.maxKeys = self.t * 2 - 1
        self.maxChildren = self.t * 2
        self.nbOfKeys = 0
        self.isLeaf = isLeaf

    def insertNonFull(self, k):
        self.nbOfKeys = len(self.keys)
        i = self.nbOfKeys - 1

        if (self.isLeaf):
            while (i >= 0 and self.keys[i] > k):
                try:
                    self.keys[i + 1] = self.keys[i]
                except:
                    self.keys.append(self.keys[i])
                i -= 1
            try:
                self.keys[i + 1] = k
            except:
                self.keys.append(k)
            self.nbOfKeys += 1
        else:
            while (i >= 0 and self.keys[i] > k):
                i -= 1

            if self.children[i + 1].nbOfKeys == 2*self.t - 1:
                self.splitChild(i + 1, self.children[i + 1])
                if (self.keys[i + 1] < k):
                    i += 1

            self.children[i + 1].insertNonFull(k)

    def splitChild(self, i, y):
        z = BTreeNode(y.t, y.isLeaf)
        z.n = self.t - 1

        for j in range(self.t - 1):
            z.keys.insert(j, y.keys[j + self.t])

        if not y.isLeaf:
            for j in range(self.t):
                z.children[j] = y.children[j + self.t]

        y.nbOfKeys = self.t - 1

        for j in range(self.nbOfKeys, i + 2, -1):
            self.children[j + 1] = self.children[j]

        self.children.insert(i + 1, z)

        for j in range(self.nbOfKeys, i + 1, -1):
            self.keys[j + 1] = self.keys[j]

        self.keys.insert(i, y.keys[self.t - 1])

        while len(y.keys) > y.nbOfKeys:
            y.keys.pop(len(y.keys)-1)

        self.nbOfKeys += 1

    def traverse(self):
        for i in range(self.nbOfKeys):
            if not self.isLeaf:
                self.children[i].traverse()
            print(" " + str(self.keys[i]))

    def search(self, k):
        i = 0
        while (i < self.nbOfKeys and k > self.keys[i]):
            i += 1

        if self.keys[i] == k:
            return self

        if self.isLeaf:
            return None

        return self.children[i].search(k)


class BTree(object):
    def __init__(self, t):
        self.root = None
        self.t = t

    def traverse(self):
        if self.root:
            self.root.traverse()

    def search(self, k):
        if self.root:
            self.root.search(k)
        else:
            return None

    def insert(self, k):
        if not self.root:
            self.root = BTreeNode(self.t, True)
            self.root.keys.append(k)
            self.root.nbOfKeys = 1

        else:
            if self.root.nbOfKeys == 2 * self.t - 1:
                s = BTreeNode(self.t, False)
                s.children.append(self.root)
                s.splitChild(0, s.children[0])

                i = 0
                if (s.keys[0] < k):
                    i += 1
                s.children[i].insertNonFull(k)
                self.root = s
            else:
                self.root.insertNonFull(k)


tree = BTree(3)
#testing tree
'''tree.insert(10)
tree.insert(20)
tree.insert(5)
tree.insert(6)
tree.insert(12)
tree.insert(30)
tree.insert(7)
tree.insert(17)
tree.insert(15)
tree.insert(16)'''

arr = np.arange(100)
np.random.shuffle(arr)
arr = list(arr)
print(arr)

for number in arr:
    tree.insert(number)


print(tree.root.keys)
for leaf in tree.root.children:
    print(leaf.keys)

