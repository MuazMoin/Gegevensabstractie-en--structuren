class Node:
    def __init__(self, key):
        self.key = key
        self.leftchild = None
        self.rightchild = None
        self.parent = None

def createHeapNode(key):
    return Node(key)

class Heap:
    def __init__(self):
        self.root = None

    def heapIsEmpty(self):
        if self.root is None:
            return True
        return False

    def heapUp(self):
        self._heapUp(self.root)
        return True

    def _heapUp(self, node):
        if node.leftchild is not None:
            if node.leftchild.key > node.key:
                temp = node.key
                node.key = node.leftchild.key
                node.leftchild.key = temp
        if node.rightchild is not None:
            if node.rightchild.key > node.key:
                temp = node.key
                node.key = node.rightchild.key
                node.rightchild.key = temp
        if node.leftchild is not None:
            self._heapUp(node.leftchild)
        if node.rightchild is not None:
            self._heapUp(node.rightchild)
        return True

    def trickleDown(self):
        self._trickledown(self.root)
        return True
    def _trickledown(self, node):
        if node.leftchild is None and node.rightchild is None:
            return
        if node.leftchild is not None and node.rightchild is None:
            if node.leftchild.key > node.key:
                temp = node.key
                node.key = node.leftchild.key
                node.leftchild.key = temp
        if node.rightchild is not None and node.leftchild is None:
            if node.rightchild.key > node.key:
                temp = node.key
                node.key = node.rightchild.key
                node.rightchild.key = temp
        if node.leftchild is not None:
            self._trickledown(node.leftchild)
        if node.rightchild is not None:
            self._trickledown(node.rightchild)
        return True

    def heapInsert(self, key):
        if self.heapIsEmpty():
            self.root = createHeapNode(key)
            return True
        node = createHeapNode(key)
        current = self.root

        while current.leftchild is not None and current.rightchild is not None:
            current = current.leftchild
        if current.leftchild is None:
            current.leftchild = node
            node.parent = current
        elif current.rightchild is None:
            current.rightchild = node
            node.parent = current
        while not self.checkHeap():
            self.heapUp()
        return True

    def checkHeap(self):
        result = self._checkheap(self.root)
        return result

    def _checkheap(self, node):
        if node.leftchild is None and node.rightchild is None:
            return True
        if node.leftchild is None and node.rightchild is not None:
            node.leftchild = node.rightchild
            node.rightchild = None
        if node.leftchild is not None:
            if node.leftchild.key > node.key:
                return False
        if node.rightchild is not None:
            if node.rightchild.key > node.key:
                return False
        if node.leftchild is not None:
            answer = self._checkheap(node.leftchild)
            if answer is False:
                return False
        if node.rightchild is not None:
            answer = self._checkheap(node.rightchild)
            if answer is False:
                return False
        return True

    def _inorder(self, node):
        if node is None:
            return
        self._inorder(node.leftchild)
        print(node.key)
        self._inorder(node.rightchild)


    def inorder(self, func):
        self._inorder(self.root)

    def inorderTraverse(self, func):
        self._inorderTraverse(self.root, func)

    def save(self):
        return self.toDict(self.root)

    def toDict(self, node):
        if node is None:
            return None
        root = {"root": node.key}
        leftTree = self.toDict(node.leftchild)
        rightTree = self.toDict(node.rightchild)
        if leftTree is not None or rightTree is not None:
            root["children"] = [leftTree, rightTree]
        return root

    def load(self, data):
        if data is None:
            self.root = None
        else:
            self.root = createHeapNode(data['root'])
            self._load(self.root, data.get('children'))

    def _load(self, node, data):
        if not data:
            return

        if data[0] is not None:
            node.leftchild = createHeapNode(data[0]['root'])
            node.leftchild.parent = node
            self._load(node.leftchild, data[0].get('children', []))

        if len(data) > 1 and data[1] is not None:
            node.rightchild = createHeapNode(data[1]['root'])
            node.rightchild.parent = node
            self._load(node.rightchild, data[1].get('children', []))

    def heapDelete(self):
        if self.root is None:
            return False, False

        current = self.root
        lefttree = self.root.leftchild
        righttree = self.root.rightchild
        delete = self.root.key

        if lefttree is not None and righttree is None:
            self.root = lefttree
            return delete, True
        elif righttree is not None and lefttree is None:
            self.root = righttree
            return delete, True

        if current.rightchild.leftchild is None and current.rightchild.rightchild is None:
            current = current.leftchild
        while current.rightchild is not None:
            current = current.rightchild
        while current.leftchild is not None:
            current = current.leftchild
        if current.parent.leftchild.key == current.key:
            current.parent.leftchild = None
        else:
            current.parent.rightchild = None
        swap = current.key
        self.root.key = swap

        self.trickleDown()
        while self.checkHeap() is False:
            self.heapUp()
        if self.root.leftchild is not None and self.root.rightchild is not None:
            if self.root.leftchild.key < self.root.rightchild.key:
                temp = self.root.leftchild.key
                self.root.leftchild.key = self.root.rightchild.key
                self.root.rightchild.key = temp

        return delete, True

    def heapSort(self):
        self._heapSort(self.root)
        return True

    def _heapSort(self, node):
        if node is None:
            return

        left_child = node.leftchild
        right_child = node.rightchild

        if left_child and left_child.key > node.key:
            node.key, left_child.key = left_child.key, node.key

        if right_child and right_child.key > node.key:
            node.key, right_child.key = right_child.key, node.key

        self._heapSort(left_child)
        self._heapSort(right_child)
        return True

"""

testcode:

t = Heap()
t.load({'root': 3, 'children': [{'root': 2}, {'root': 1}]})
t.heapInsert(5)
t.heapInsert(4)
result = t.heapDelete()
print(t.save())

"""
