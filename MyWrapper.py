class BSTTable:

    def __init__(self):
        """
            Initialiseert een lege BSTTable met een interne BST.

            Precondities:
            - Geen.

            Postcondities:
            - Een lege BSTTable is geïnstantieerd met een interne BST.
        """
        self.bst = BST()

    def tableIsEmpty(self):
        """
            Controleert of de BSTTable leeg is.

            Output:
            - True als de BSTTable leeg is, False anders. (bool)

            Precondities:
            - Geen.

            Postcondities:
            - De toestand van de BSTTable blijft ongewijzigd.
        """
        return self.bst.isEmpty()

    def tableInsert(self, item):
        """
            Voegt een item toe aan de BSTTable.

            Input:
            - item: Het item dat aan de BSTTable moet worden toegevoegd. (TreeNode)

            Output:
            - True als de invoeging succesvol is, False als het item al bestaat. (bool)

            Precondities:
            - Het input-item 'item' moet een geldige TreeNode zijn.

            Postcondities:
            - De BSTTable kan één element meer bevatten als de invoeging succesvol is.
        """
        return self.bst.searchTreeInsert(item)

    def tableRetrieve(self, searchKey):
        """
            Zoekt een item met de opgegeven sleutel in de BSTTable.

            Input:
            - searchKey: De sleutel waarnaar wordt gezocht in de BSTTable. (Comparable)

            Output:
            - Een tuple bestaande uit de gevonden data en True als de sleutel gevonden is, of (None, False) als de sleutel niet bestaat. (tuple)

            Precondities:
            - De sleutel 'searchKey' moet van hetzelfde type zijn als de sleutels in de BSTTable.

            Postcondities:
            - De toestand van de BSTTable blijft ongewijzigd.
        """
        return self.bst.searchTreeRetrieve(searchKey)

    def tableDelete(self, searchKey):
        """
            Verwijdert een item met de opgegeven sleutel uit de BSTTable.

            Input:
            - searchKey: De sleutel van het item dat uit de BSTTable moet worden verwijderd. (Comparable)

            Output:
            - True als de verwijdering succesvol is, False als de sleutel niet bestaat. (bool)

            Precondities:
            - De sleutel 'searchKey' moet van hetzelfde type zijn als de sleutels in de BSTTable.

            Postcondities:
            - De BSTTable kan één element minder bevatten als de verwijdering succesvol is.
        """
        return self.bst.searchTreeDelete(searchKey)

    def traverseTable(self, functie):
        """
            Voert een functie uit op alle waarden in de BSTTable in inorder volgorde.

            Input:
            - functie: Een functie die wordt toegepast op elke waarde in de BSTTable. (Callable)

            Precondities:
            - De input 'functie' moet een geldige callable zijn.

            Postcondities:
            - De toestand van de BSTTable blijft ongewijzigd.
        """
        self.bst.inorderTraverse(functie)

    def save(self):
        """
            Slaat de huidige BSTTable op in een dictionary.

            Output:
            - Een dictionary die de geneste structuur van de BSTTable weergeeft.

            Precondities:
            - De BSTTable moet minstens één knoop bevatten.

            Postcondities:
            - De toestand van de BSTTable blijft ongewijzigd.
        """
        return self.bst.save()

    def load(self, data):
        """
            Laadt de waarden van de BSTTable uit een dictionary.

            Input:
            - data: Een dictionary die de geneste structuur van de BSTTable vertegenwoordigt.

            Precondities:
            - De input 'data' moet een geldige dictionary zijn die de geneste structuur van een BSTTable vertegenwoordigt.

            Postcondities:
            - De BSTTable is geladen met de waarden uit de gegeven dictionary.
        """
        self.bst.load(data)

""" 

testcode:

t = BSTTable()
print(t.tableIsEmpty())
print(t.tableInsert(createTreeItem(8,8)))
print(t.tableInsert(createTreeItem(5,5)))
print(t.tableIsEmpty())
print(t.tableRetrieve(5)[0])
print(t.tableRetrieve(5)[1])
t.traverseTable(print)
print(t.save())
t.load({'root': 10,'children':[{'root':5},None]})
t.tableInsert(createTreeItem(15,15))
print(t.tableDelete(0))
print(t.save())
print(t.tableDelete(10))
print(t.save())

"""
