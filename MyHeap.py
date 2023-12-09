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
        self.size = 0

    def heapIsEmpty(self):
        return self.root is None

    def heapInsert(self, key):
        if self.heapIsEmpty():
            self.root = createHeapNode(key)
            self.size += 1
            return True
        else:
            self.size += 1
            return self.__insert(self.root, key)

    def __insert(self, node, key):
        if node.leftchild is None:
            node.leftchild = createHeapNode(key)
            node.leftchild.parent = node
            self.__heapify_up(node.leftchild)
            return True
        elif node.rightchild is None:
            node.rightchild = createHeapNode(key)
            node.rightchild.parent = node
            self.__heapify_up(node.rightchild)
            return True
        else:
            if self.__insert(node.leftchild, key):
                self.__heapify_up(node.leftchild)
                return True
            elif self.__insert(node.rightchild, key):
                self.__heapify_up(node.rightchild)
                return True
            else:
                return False

    def __heapify_up(self, node):
        while node.parent is not None and node.parent.key < node.key:
            node.parent.key, node.key = node.key, node.parent.key
            node = node.parent

    def heapDelete(self):
        if self.heapIsEmpty():
            return None, False
        else:
            self.size -= 1
            return self.__delete(self.root)

    def __delete(self, node):
        if node.leftchild is None and node.rightchild is None:
            if node.parent is None:
                self.root = None
            elif node.parent.leftchild == node:
                node.parent.leftchild = None
            else:
                node.parent.rightchild = None
            return node.key, True
        elif node.leftchild is None:
            return self.__delete_single_child(node, node.rightchild)
        elif node.rightchild is None:
            return self.__delete_single_child(node, node.leftchild)
        else:
            return self.__delete_two_children(node)

    def __delete_single_child(self, node, child):
        if node.parent is None:
            self.root = child
            child.parent = None
        elif node.parent.leftchild == node:
            node.parent.leftchild = child
            child.parent = node.parent
        else:
            node.parent.rightchild = child
            child.parent = node.parent
        return node.key, True

    def __delete_two_children(self, node):
        min_node = self.__find_min(node.rightchild)
        node.key, min_node.key = min_node.key, node.key
        return self.__delete(min_node)

    def __find_min(self, node):
        while node.leftchild is not None:
            node = node.leftchild
        return node

    def check(self):
        if self.heapIsEmpty():
            return True
        else:
            return self.__check(self.root)

    def __check(self, node):
        if node.leftchild is None and node.rightchild is None:
            return True
        elif node.leftchild is None:
            return node.key >= node.rightchild.key and self.__check(node.rightchild)
        elif node.rightchild is None:
            return node.key >= node.leftchild.key and self.__check(node.leftchild)
        else:
            return node.key >= node.leftchild.key and node.key >= node.rightchild.key and self.__check(node.leftchild) and self.__check(node.rightchild)

    def heapRetrieve(self):
        if self.heapIsEmpty():
            return None, False
        else:
            return self.root.key, True

    def inorderTraverse(self, function):
        if not self.heapIsEmpty():
            self.__inorderTraverse(self.root, function)

    def __inorderTraverse(self, node, function):
        if node.leftchild is not None:
            self.__inorderTraverse(node.leftchild, function)
        function(node.key)
        if node.rightchild is not None:
            self.__inorderTraverse(node.rightchild, function)

    def save(self):
        if self.heapIsEmpty():
            return None
        else:
            return self.__save(self.root)

    def __save(self, node):
        if node.leftchild is None and node.rightchild is None:
            return {'root': node.key}
        elif node.leftchild is None:
            return {'root': node.key, 'children': [self.__save(node.rightchild), None]}
        elif node.rightchild is None:
            return {'root': node.key, 'children': [self.__save(node.leftchild), None]}
        else:
            return {'root': node.key, 'children': [self.__save(node.leftchild), self.__save(node.rightchild)]}

    def load(self, data):
        if data is None:
            self.root = None
        else:
            self.root = createHeapNode(data['root'])
            self.__load(self.root, data['children'])

    def __load(self, node, data):
        if not data:
            return

        if data[0] is not None:
            node.leftchild = createHeapNode(data[0]['root'])
            node.leftchild.parent = node
            self.__load(node.leftchild, data[0].get('children', []))

        if len(data) > 1 and data[1] is not None:
            node.rightchild = createHeapNode(data[1]['root'])
            node.rightchild.parent = node
            self.__load(node.rightchild, data[1].get('children', []))



t = Heap()
print(t.heapIsEmpty())
print(t.heapDelete()[1])
print(t.heapInsert(5))
print(t.heapInsert(8))
print(t.heapIsEmpty())
print(t.save())
t.load({'root': 10,'children':[{'root':5},None]})
t.heapInsert(15)
print(t.save())
result = t.heapDelete()
print(result[0])
print(result[1])
print(t.save())
