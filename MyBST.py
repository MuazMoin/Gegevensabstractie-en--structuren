class TreeNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        """
        Initialiseert een lege BST.
        """
        self.root = None

    def isEmpty(self):
        """
        Controleert of de BST leeg is.
        """
        return self.root is None

    def searchTreeInsert(self, key, data):
        """
        Voegt een nieuwe node toe aan de BST.
        """
        if self.root is None:
            self.root = TreeNode(key, data)
        else:
            self._insert(key, data, self.root)

    def _insert(self, key, data, node):
        """
        Hulpfunctie voor insert.
        """
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key, data)
            else:
                self._insert(key, data, node.left)
        else:
            if node.right is None:
                node.right = TreeNode(key, data)
            else:
                self._insert(key, data, node.right)

    def searchTreeRetrieve(self, key):
        """
        Zoekt een node met de opgegeven sleutel in de BST.
        """
        if self.root is None:
            return False
        else:
            return self._retrieve(key, self.root)

    def _retrieve(self, key, node):
        """
        Hulpfunctie voor search.
        """
        if key == node.key:
            return True, node.data
        elif key < node.key and node.left is not None:
            return self._retrieve(key, node.left)
        elif key > node.key and node.right is not None:
            return self._retrieve(key, node.right)
        else:
            return False, None

    def searchTreeDelete(self, key):
        """
        Verwijdert een node met de opgegeven sleutel uit de BST.
        """
        if self.root is None:
            return False
        else:
            self.root = self._delete(key, self.root)
            return True  # Return True omdat de verwijdering is geslaagd

    def _delete(self, key, node):
        """
        Hulpfunctie voor delete.
        """
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(key, node.left)
        elif key > node.key:
            node.right = self._delete(key, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Node heeft twee kinderen
            node.key, node.data = self._find_min(node.right)
            node.right = self._delete(node.key, node.right)

        return node

    def _find_min(self, node):
        """
        Hulpfunctie om het minimum in een BST te vinden.
        """
        while node.left is not None:
            node = node.left
        return node.key, node.data

    def inorder(self):
        """
        Geeft een generator terug die de waarden van de BST in inorder volgorde geeft.
        """
        return self._inorder(self.root)

    def _inorder(self, node):
        if node is not None:
            yield from self._inorder(node.left)
            yield node.key, node.data
            yield from self._inorder(node.right)

    def save(self):
        """
        Geeft een dictionary terug met de waarden van de BST.
        """
        return self._serialize(self.root)

    def _serialize(self, root):
        if root is not None:
            return {'key': root.key, 'data': root.data, 'left': self._serialize(root.left), 'right': self._serialize(root.right)}
        else:
            return None

    def load(self, data):
        """
        Laadt de waarden van de BST uit een dictionary.
        """
        self.root = self._deserialize(data)

    def _deserialize(self, data):
        if data is not None:
            node = TreeNode(data['key'], data['data'])
            node.left = self._deserialize(data['left'])
            node.right = self._deserialize(data['right'])
            return node
        else:
            return None

def createTreeItem(key, data):
    return {'key': key, 'data': data, 'left': None, 'right': None}


    t = BST()
    print(t.isEmpty())
    print(t.searchTreeInsert(8, 8))
    print(t.searchTreeInsert(5, 5))
    print(t.isEmpty())
    print(t.searchTreeRetrieve(5))
    t.inorderTraverse(print)
    print(t.save())
    t.load({'key': 10, 'data': None, 'left': {'key': 5, 'data': None, 'left': None, 'right': None}, 'right': None})
    t.searchTreeInsert(15, 15)
    print(t.searchTreeDelete(0))
    print(t.save())
    print(t.searchTreeDelete(10))
    print(t.save())
