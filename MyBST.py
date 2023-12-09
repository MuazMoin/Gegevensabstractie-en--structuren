"""
Binary Search Tree (BST) voor het organiseren en beheren van gegevens.
"""

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

    def searchTreeInsert(self, node):
        """
            Voegt een nieuwe node toe aan de BST.

            Input:
            - node: Een TreeNode-object dat aan de BST moet worden toegevoegd.

            Output:
            - True als de invoeging succesvol is, False anders.

            Precondities:
            - De node heeft een geldige sleutel.

            Postcondities:
            - Als True wordt geretourneerd, bevat de BST nu de nieuwe node met de opgegeven sleutel.
        """
        if self.root is None:
            self.root = node
            return True
        else:
            return self._insert(self.root, node)


    def _insert(self, old_node, node):
        """
            Voegt een nieuwe node toe aan de BST.

            Input:
            - old_node: De ouderknoop waar de nieuwe node aan wordt toegevoegd. (TreeNode)
            - node: De nieuwe TreeNode die aan de BST wordt toegevoegd. (TreeNode)

            Output:
            - True als de invoeging succesvol is, False als de sleutel al bestaat. (bool)

            Precondities:
            - old_node moet een geldige TreeNode zijn, anders gedraagt de functie zich onvoorspelbaar.
            - old_node moet al een geldige sleutel hebben.
            - node moet een geldige TreeNode zijn.
            - node moet een geldige sleutel hebben.

            Postcondities:
            - Als True wordt geretourneerd, is de nieuwe node met de opgegeven sleutel toegevoegd aan de BST.
            - Als False wordt geretourneerd, bestaat er al een node met dezelfde sleutel in de BST.
        """

        if node.key < old_node.key:
            if old_node.left is None:
                old_node.left = node
                return True
            else:
                return self._insert(old_node.left, node)

        elif node.key > old_node.key:
            if old_node.right is None:
                old_node.right = node
                return True
            else:
                return self._insert(old_node.right, node)
        else:
            return False

    def searchTreeRetrieve(self, key):
        """
            Zoekt een node met de opgegeven sleutel in de BST.

            Input:
            - key: De sleutel waarnaar wordt gezocht in de BST. (Comparable)

            Output:
            - Een tuple bestaande uit de gevonden data en True als de sleutel gevonden is, of (None, False) als de sleutel niet bestaat. (tuple)

            Precondities:
            - De sleutel 'key' moet van hetzelfde type zijn als de sleutels in de BST.
            - Als de BST leeg is (self.root is None), wordt (None, False) direct geretourneerd.

            Postcondities:
            - Als True wordt geretourneerd, bevat het eerste element van het tuple de gevonden data.
            - Als False wordt geretourneerd, bestaat er geen node met de opgegeven sleutel in de BST, en is het tweede element van het tuple False.
        """

        if self.root is None:
            return False
        else:
            return self._retrieve(key, self.root)

    def _retrieve(self, key, node):
        """
            Hulpfunctie voor het zoeken naar een node met de opgegeven sleutel in de BST.

            Input:
            - key: De sleutel waarnaar wordt gezocht in de BST. (Comparable)
            - node: De huidige TreeNode waarin wordt gezocht. (TreeNode)

            Output:
            - Een tuple bestaande uit de gevonden data en True als de sleutel gevonden is, of (None, False) als de sleutel niet bestaat. (tuple)

            Precondities:
            - De sleutel 'key' moet van hetzelfde type zijn als de sleutels in de BST.
            - De TreeNode 'node' moet een geldige TreeNode zijn, anders gedraagt de functie zich onvoorspelbaar.

            Postcondities:
            - Als True wordt geretourneerd, bevat het eerste element van het tuple de gevonden data.
            - Als False wordt geretourneerd, bestaat er geen node met de opgegeven sleutel in de BST, en is het tweede element van het tuple False.
        """

        if key == node.key:
            return node.data, True
        elif key < node.key and node.left is not None:
            return self._retrieve(key, node.left)
        elif key > node.key and node.right is not None:
            return self._retrieve(key, node.right)
        else:
            return None, False

    def searchTreeDelete(self, key):
        """
            Verwijdert een node met de opgegeven sleutel uit de BST.

            Input:
            - key: De sleutel van de node die uit de BST moet worden verwijderd. (Comparable)

            Output:
            - True als de verwijdering succesvol is, False als de sleutel niet bestaat of de BST leeg is. (bool)

            Precondities:
            - De sleutel 'key' moet van hetzelfde type zijn als de sleutels in de BST.

            Postcondities:
            - Als True wordt geretourneerd, is de node met de opgegeven sleutel verwijderd uit de BST.
            - Als False wordt geretourneerd, bestaat er geen node met de opgegeven sleutel in de BST, of de BST is leeg.
        """

        if self.isEmpty():
            return False
        else:
            self.root, verwijderen = self._delete(self.root, key)
            return verwijderen

    def _delete(self, node, key):
        """
            Verwijdert een node met de opgegeven sleutel uit de BST.

            Input:
            - key: De sleutel van de node die uit de BST moet worden verwijderd. (Comparable)

            Output:
            - True als de verwijdering succesvol is, False als de sleutel niet bestaat of de BST leeg is. (bool)

            Precondities:
            - De sleutel 'key' moet van hetzelfde type zijn als de sleutels in de BST.

            Postcondities:
            - Als True wordt geretourneerd, is de node met de opgegeven sleutel verwijderd uit de BST.
            - Als False wordt geretourneerd, bestaat er geen node met de opgegeven sleutel in de BST, of de BST is leeg.
        """

        if node is None:
            return None, False

        if key < node.key:
            node.left, verwijderen = self._delete(node.left, key)
        elif key > node.key:
            node.right, verwijderen = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True
            else:
                successor = self._find_min(node.right)
                node.key = successor.key
                node.data = successor.data
                node.right, verwijderen = self._delete(node.right, successor.key)

        return node, verwijderen

    def _find_min(self, node):
        """
            Hulpfunctie om het minimum in een BST te vinden.

            Input:
            - node: De huidige TreeNode waarvan het minimum wordt gezocht. (TreeNode)

            Output:
            - De TreeNode met het minimumsleutelwaardepaar in de BST. (TreeNode)

            Precondities:
            - De TreeNode 'node' moet een geldige TreeNode zijn, anders gedraagt de functie zich onvoorspelbaar.

            Postcondities:
            - De teruggegeven TreeNode heeft het minimumsleutelwaardepaar in de BST.
        """
        while node.left is not None:
            node = node.left
        return node

    def _serialize(self, root):
        """
            Serialiseert de BST naar een dictionary.

            Input:
            - root: De wortelknoop van de BST. (TreeNode)

            Output:
            - Een dictionary die de geneste structuur van de BST weergeeft.

            Precondities:
            - De TreeNode 'root' moet een geldige wortelknoop van de BST zijn.

            Postcondities:
            - De geretourneerde dictionary vertegenwoordigt de geneste structuur van de BST.
        """
        if root is None:
            return None
        else:
            d = {'root': root.key}
            left = self._serialize(root.left)
            right = self._serialize(root.right)

            if left is not None or right is not None:
                d['children'] = []

                if left is not None:
                    d['children'].append(left)
                else:
                    d['children'].append(None)

                if right is not None:
                    d['children'].append(right)
                else:
                    d['children'].append(None)

            return d

    def _deserialize(self, data):
        """
            Deserialiseert een dictionary naar een BST.

            Input:
            - data: Een dictionary die de geneste structuur van de BST vertegenwoordigt.

            Output:
            - De wortelknoop van de gedeserialiseerde BST. (TreeNode)

            Precondities:
            - De input 'data' moet een geldige dictionary zijn die de geneste structuur van een BST vertegenwoordigt.

            Postcondities:
            - De geretourneerde TreeNode is de wortelknoop van de gedeserialiseerde BST.
        """

        if data is None:
            return None
        else:
            Muaz = data.get('root')
            node = createTreeItem(Muaz, Muaz)
            children = data.get('children', [])
            if children:
                node.left = self._deserialize(children[0])
                if len(children) > 1:
                    node.right = self._deserialize(children[1])

            return node


    def save(self):

        """
            Slaat de huidige BST op in een dictionary.

            Output:
            - Een dictionary die de geneste structuur van de BST weergeeft.

            Precondities:
            - De BST moet minstens één knoop bevatten.

            Postcondities:
            - De geretourneerde dictionary vertegenwoordigt de geneste structuur van de huidige BST.

            Beschrijving:
            Deze methode slaat de huidige BST op in een geneste dictionary-structuur, zodat deze later kan worden hersteld met de 'load'-methode.
        """

        return self._serialize(self.root)

    def load(self, data):
        """
            Laadt de waarden van de BST uit een dictionary.

            Input:
            - data: Een dictionary die de geneste structuur van de BST vertegenwoordigt.

            Precondities:
            - De input 'data' moet een geldige dictionary zijn die de geneste structuur van een BST vertegenwoordigt.

            Postcondities:
            - De huidige BST is geladen met de waarden uit de gegeven dictionary.
        """

        self.root = self._deserialize(data)

    def inorderTraverse(self, functie):
        """
            Voert een functie uit op alle waarden in de BST in inorder volgorde.

            Input:
            - functie: Een functie die wordt toegepast op elke waarde in de BST. (Callable)

            Precondities:
            - De BST moet minstens één knoop bevatten.
            - De input 'functie' moet een geldige callable zijn.

            Postcondities:
            - De opgegeven functie is toegepast op alle waarden in de BST in inorder volgorde.
        """
        self._inorderTraverse(self.root, functie)

    def _inorderTraverse(self, node, functie):
        """
            Hulpfunctie voor het inorder traverseren van de BST.

            Input:
            - node: De huidige TreeNode waarvan de waarde wordt verwerkt. (TreeNode)
            - functie: Een functie die wordt toegepast op elke waarde in de BST. (Callable)

            Precondities:
            - De TreeNode 'node' moet een geldige TreeNode zijn, anders gedraagt de functie zich onvoorspelbaar.
            - De input 'functie' moet een geldige callable zijn.

            Postcondities:
            - De opgegeven functie is toegepast op de waarde van elke bezochte TreeNode in inorder volgorde.
        """

        if node is not None:
            self._inorderTraverse(node.left, functie)
            functie(node.data)
            self._inorderTraverse(node.right, functie)


def createTreeItem(key, data):
        """
            Maakt een nieuwe node aan.

            Input:
            - key: De sleutel van de nieuwe TreeNode. (Comparable)
            - data: De data van de nieuwe TreeNode.

            Output:
            - Een nieuwe TreeNode met de opgegeven sleutel en data. (TreeNode)

            Beschrijving:
            Deze functie creëert en retourneert een nieuwe TreeNode met de opgegeven sleutel en data.
        """
        return TreeNode(key, data)

""" 

testcode:

t = BST()
print(t.isEmpty())
print(t.searchTreeInsert(createTreeItem(8,8)))
print(t.searchTreeInsert(createTreeItem(5,5)))
print(t.isEmpty())
print(t.searchTreeRetrieve(5)[0])
print(t.searchTreeRetrieve(5)[1])
t.inorderTraverse(print)
print(t.save())
t.load({'root': 10,'children':[{'root':5},None]})
t.searchTreeInsert(createTreeItem(15,15))
print(t.searchTreeDelete(0))
print(t.save())
print(t.searchTreeDelete(10))
print(t.save())

"""
