def createTreeItem(key, val):
    """Pre-conditie:
    - key en val moeten niet-null waarden zijn

    Post-conditie:
    - De functie retourneert een object van het type TreeItemType met de opgegeven key en val.
    - Het aangemaakte object bevat de opgegeven key en val."""
    return TreeItemType(key, val)


class TreeItemType:
    def __init__(self, key, val=None):
        """Pre-conditie:
        # - key moet niet-null zijn

        # Post-conditie:
        # - Een object van de klasse TreeItemType is aangemaakt.
        # - Het aangemaakte object heeft de opgegeven key en val-waarden toegewezen."""

        self.key = key
        self.val = val

    def __lt__(self, other):
        """Pre-conditie:
        - other moet een object van de klasse TreeItemType zijn

        Post-conditie:
        - True is geretourneerd als de key van het huidige object kleiner is dan de key van 'other'.
        - False is geretourneerd in alle andere gevallen."""

        return self.key < other.key

    def __eq__(self, other):
        """Pre-conditie:
        - other moet een object van de klasse TreeItemType zijn

        Post-conditie:
        - True is geretourneerd als de key van het huidige object gelijk is aan de key van 'other'.
        - False is geretourneerd in alle andere gevallen."""

        return self.key == other.key

    def __str__(self):
        """Pre-conditie:
        - Geen specifieke pre-condities

        Post-conditie:
        - Een leesbare string representatie van het object (de key) is geretourneerd."""

        return str(self.key)


class TwoThreeFourTreeNode:

    def __init__(self, item=None):
        """
        Preconditie:
        - item kan elk type zijn.

        Postconditie:
        - Een nieuw TreeNode-object wordt aangemaakt.
        - self.node is een lege lijst.
        - self.children is een lege lijst.
        - self.parent is None, tenzij expliciet ingesteld na instantiatie.
        """

        self.node = []
        self.children = []
        self.parent = None

    def isEmpty(self):
        """
        Bepaalt of een TwoThreeFourTree leeg is.

        preconditie: Er is geen preconditie.
        postconditie: Return True als de TwoThreeFourTree leeg is, False als het niet leeg is.

        :return: Geeft True terug als de TwoThreeFourTree leeg is, anders False
        """""
        if len(self.node) != 0:
            return False
        return True

    def isLeaf(self):
        """
        Preconditie:
        - Geen specifieke precondities.

        Postconditie:
        - Geeft True terug als het huidige knooppunt een bladknooppunt is (geen kinderen heeft).
        - Geeft False terug als het huidige knooppunt geen bladknooppunt is (minstens één kind heeft).
        """
        if len(self.children) == 0:
            return True
        return False

    def isSame(self, list1, list2):
        """
        Preconditie:
        - list1 en list2 zijn beide lijsten.

        Postconditie:
        - Geeft True terug als list1 en list2 dezelfde elementen hebben in dezelfde volgorde.
        - Geeft False terug als list1 en list2 verschillende lengtes hebben of als er minstens één paar elementen niet overeenkomt.
        """
        if len(list1) != len(list2):
            return False;
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
        return True

    def insertItem(self, insertTreeItemType):

        # deze functie heb ik gemaakt samen met iemand die nu in 2e bachelor zit, want ik kreeg mijn insert niet helemaal werkende.

        """
        Precondities:
        - insertTreeItemType is een object van een type dat een attribuut 'key' heeft.

        Postcondities:
        - Als het huidige knooppunt leeg is, wordt het knooppunt ingesteld met insertTreeItemType als enig element.
        - Als het huidige knooppunt een 4-knoop is (drie elementen), wordt het knooppunt gesplitst en wordt insertTreeItemType ingevoegd op het juiste niveau.
        - Als het huidige knooppunt een 2-knoop is (één element), kan het direct worden gesplitst en wordt insertTreeItemType ingevoegd op het juiste niveau.
        - Als het huidige knooppunt een 3-knoop is (twee elementen), wordt het knooppunt gesplitst en wordt insertTreeItemType ingevoegd op het juiste niveau.
        - In alle gevallen wordt True geretourneerd als de invoeging succesvol is.
        """
        if self.isEmpty():
            self.node = [insertTreeItemType]
            return True

        if (len(self.node)) == 3:

            parent = self.parent

            if parent is None:
                parent = TwoThreeFourTreeNode()
                parent.node = [self.node[1]]

                self.parent = parent

                left = TwoThreeFourTreeNode()
                left.node = [self.node[0]]
                left.parent = parent

                right = TwoThreeFourTreeNode()
                right.node = [self.node[2]]
                right.parent = parent

                parent.children.append(left)
                parent.children.append(right)

                if len(self.children) > 0:
                    self.children[0].parent = left
                    self.children[1].parent = left
                    self.children[2].parent = right
                    self.children[3].parent = right

                    left.children.append(self.children[0])
                    left.children.append(self.children[1])
                    right.children.append(self.children[2])
                    right.children.append(self.children[3])

                if (insertTreeItemType.val > parent.node[0].val):
                    return right.insertItem(insertTreeItemType)
                else:
                    return left.insertItem(insertTreeItemType)

            elif len(self.parent.node) == 1:

                insertIndex = 0
                if self.node[1].key < parent.node[0].key:
                    insertIndex = 0
                else:
                    insertIndex = 1

                parent.node.append(self.node[1])
                parent.node.sort()

                L3 = TwoThreeFourTreeNode()
                L3.node = [self.node[0]]
                L3.parent = parent

                R3 = TwoThreeFourTreeNode()
                R3.node = [self.node[2]]
                R3.parent = parent

                if insertIndex == 0:
                    parent.children.insert(0, L3)
                    parent.children.insert(1, R3)
                else:
                    parent.children.append(L3)
                    parent.children.append(R3)

                if len(self.children) > 0:
                    self.children[0].parent = L3
                    self.children[1].parent = L3
                    self.children[2].parent = R3
                    self.children[3].parent = R3

                    L3.children.append(self.children[0])
                    L3.children.append(self.children[1])
                    R3.children.append(self.children[2])
                    R3.children.append(self.children[3])

                self.children.clear()

                childIndex = -1

                for i in range(len(self.parent.children)):
                    if self.isSame(self.parent.children[i].node, self.node):
                        childIndex = i

                self.parent.children.pop(childIndex)

                if insertTreeItemType.val < parent.node[0].val:
                    return self.parent.children[0].insertItem(insertTreeItemType)
                elif insertTreeItemType.val < parent.node[1].val:
                    return self.parent.children[1].insertItem(insertTreeItemType)
                else:
                    return self.parent.children[2].insertItem(insertTreeItemType)


            elif len(self.parent.node) == 2:

                insertIndex = 0
                if self.node[1].key < parent.node[0].key:
                    insetIndex = 0
                elif self.node[1].key < parent.node[1].key:
                    insertIndex = 1
                else:
                    insertIndex = 2

                parent.node.append(self.node[1])
                parent.node.sort()

                L4 = TwoThreeFourTreeNode()
                L4.node = [self.node[0]]
                L4.parent = parent
                if len(self.children) > 0:
                    L4.children.append(self.children[0])
                    L4.children.append(self.children[1])

                R4 = TwoThreeFourTreeNode()
                R4.node = [self.node[2]]
                R4.parent = parent
                if len(self.children) > 0:
                    R4.children.append(self.children[2])
                    R4.children.append(self.children[3])

                if insertIndex == 0:
                    parent.children.insert(0, L4)
                    parent.children.insert(1, R4)
                elif insertIndex == 1:
                    parent.children.insert(1, L4)
                    parent.children.insert(2, R4)
                else:
                    parent.children.append(L4)
                    parent.children.append(R4)

                self.children.clear()

                childindex = -1

                for i in range(len(self.parent.children)):
                    if self.isSame(self.parent.children[i].node, self.node):
                        childindex = i

                self.parent.children.pop(childindex)

                if insertTreeItemType.val < parent.node[0].val:
                    return self.parent.children[0].insertItem(insertTreeItemType)
                elif insertTreeItemType.val < parent.node[1].val:
                    return self.parent.children[1].insertItem(insertTreeItemType)
                elif insertTreeItemType.val < parent.node[2].val:
                    return self.parent.children[2].insertItem(insertTreeItemType)
                else:
                    return self.parent.children[3].insertItem(insertTreeItemType)

        if self.isLeaf():
            self.node.append(insertTreeItemType)
            self.node.sort()
            return True
        else:
            for i in range(len(self.node)):
                if insertTreeItemType.key < self.node[i].key:
                    return self.children[i].insertItem(insertTreeItemType)

            return self.children[-1].insertItem(insertTreeItemType)

    def retrieveItem(self, searchKey):
        """
        Precondities:
        - searchKey is van hetzelfde type als de sleutels in de knooppunten.

        Postcondities:
        - Als het huidige knooppunt leeg is, wordt (None, False) geretourneerd.
        - Als het huidige knooppunt een blad is en searchKey wordt gevonden, wordt de waarde en True geretourneerd.
        - Als het huidige knooppunt een blad is en searchKey niet wordt gevonden, wordt (None, False) geretourneerd.
        - Als het huidige knooppunt geen blad is en searchKey wordt gevonden, wordt de waarde en True geretourneerd.
        - Als het huidige knooppunt geen blad is en searchKey niet wordt gevonden, wordt de retrieveItem methode op het juiste kind aangeroepen.
        """
        if self.isEmpty():
            return None, False
        elif self.isLeaf():
            for i in range(len(self.node)):
                if self.node[i].key == searchKey:
                    return self.node[i].val, True
            return None, False
        else:
            for i in range(len(self.node)):
                if searchKey == self.node[i].key:
                    return self.node[i].val, True
                elif searchKey < self.node[i].key:
                    return self.children[i].retrieveItem(searchKey)
            return self.children[len(self.node)].retrieveItem(searchKey)

    def inorderTraverse(self, functie):
        """
        Precondities:
        - functie is een functie die kan worden toegepast op de sleutels van de knooppunten.

        Postcondities:
        - Voert de gegeven functie uit op de sleutels van de knooppunten in inorder volgorde.
        """
        if self.isLeaf():
            for item in self.node:
                functie(item.key)
        else:
            for i in range(len(self.node)):
                self.children[i].inorderTraverse(functie)
                functie(self.node[i].key)
            self.children[-1].inorderTraverse(functie)

    def save(self):
        """
        Precondities:
        - Geen specifieke precondities.

        Postcondities:
        - Retourneert een dictionary die de sleutels van de knooppunten bevat en recursief de kinderen als deze bestaan.
        - De resulterende structuur kan worden gebruikt om de huidige staat van het boomknooppunt op te slaan.
        """
        if len(self.children) != 0:
            p = {
                "root": [item.key for item in self.node],
                "children": [child.save() for child in self.children]
            }

        else:
            p = {
                "root": [item.key for item in self.node],
            }

        return p

    def load(self, items):

        """
        Precondities:
        - items is een dictionary met minimaal een "root" key.
        - Elk element in "root" is van hetzelfde type als de sleutels die kunnen worden ingevoegd in het boomknooppunt.

        Postcondities:
        - Voegt de sleutels uit "root" toe aan het huidige boomknooppunt.
        - Als "children" bestaat, worden nieuwe kinderen gemaakt en de load-methode wordt recursief aangeroepen voor elk kind.
        """

        if not items:
            return

        roott = items.get("root")
        childrent = items.get("children", [])

        for nodeItems in roott:
            self.insertItem(createTreeItem(nodeItems, nodeItems))

        if len(childrent) != 0:
            for child_data in childrent:
                child = TwoThreeFourTreeNode()
                self.children.append(child)

                # Set Parent XXXXX
                child.parent = self
                # Load Recursive
                child.load(child_data)

    def deleteItem(self, searchKey):
        """
        Postcondities:

        Het opgegeven element is verwijderd uit de 2-3-4 boom.
        Indien nodig zijn knopen samengevoegd, gesplitst of herschikt om te voldoen aan de eigenschappen van een 2-3-4 boom.
        De structuur van de 2-3-4 boom is correct hersteld.
        Als een knoop nu minder dan 2 elementen heeft, is deze samengevoegd met een naburige knoop om de eigenschappen van de 2-3-4 boom te behouden.
        Als de wortel van de boom nu leeg is, is de hoogte van de boom met één verminderd.

        """
        # deze functie heb ik gemaakt met iemand die nu in 2e bachelor zit. Ik heb hierbij ook gebruik gemaakt van stackoverflow en chatgpt om foute te vinden in mijn code en het eventueel op te lossen.
        if self.isEmpty():
            return False

        for i, item in enumerate(self.node):
            if item.key == searchKey:

                if (self.parent is not None) and (self.parent.parent is not None) and (len(self.parent.node)) == 1:

                    total = len(self.parent.node)
                    for k, citem in enumerate(self.parent.children):
                        total += len(citem.node)

                    if total > 5:

                        if self.node[0].key > self.parent.node[0].key:

                            if len(self.node) > 2:

                                    self.parent.node.append(self.node[1])
                                    self.parent.node.sort()

                                    L3 = TwoThreeFourTreeNode()
                                    L3.node = [self.node[0]]
                                    L3.parent = self.parent

                                    R3 = TwoThreeFourTreeNode()
                                    R3.node = [self.node[2]]
                                    R3.parent = self.parent

                                    self.parent.children.pop(0)
                                    self.parent.children.insert(0, R3)
                                    self.parent.children.insert(0, L3)
                                    del self.node[1]

                            else:

                                self.parent.node.append(self.parent.children[0].node[1])
                                self.parent.node.sort()

                                L3 = TwoThreeFourTreeNode()
                                L3.node = [self.parent.children[0].node[0]]
                                L3.parent = self.parent

                                R3 = TwoThreeFourTreeNode()
                                R3.node = [self.parent.children[0].node[2]]
                                R3.parent = self.parent

                                self.parent.children.pop(0)
                                self.parent.children.insert(0, R3)
                                self.parent.children.insert(0, L3)

                                del self.parent.children[0].node[1]


                        else:

                            if len(self.node) < 2:

                                self.parent.node.append(self.parent.children[1].node[1])
                                self.parent.node.sort()

                                L3 = TwoThreeFourTreeNode()
                                L3.node = [self.parent.children[1].node[0]]
                                L3.parent = self.parent

                                R3 = TwoThreeFourTreeNode()
                                R3.node = [self.parent.children[1].node[2]]
                                R3.parent = self.parent

                                self.parent.children.pop(1)
                                self.parent.children.insert(1, R3)
                                self.parent.children.insert(1, L3)

                                del self.parent.children[1].node[1]

                            else:

                                self.parent.node.append(self.node[0])
                                self.parent.node.sort()

                                L3 = TwoThreeFourTreeNode()
                                L3.node = [self.node[1]]
                                L3.parent = self.parent

                                R3 = TwoThreeFourTreeNode()
                                R3.node = [self.parent.children[1].node[0]]
                                R3.parent = self.parent

                                self.parent.children.pop(1)
                                self.parent.children.insert(1, R3)
                                self.parent.children.insert(1, L3)

                                del self.node[1]

                    else:

                        if self.parent.node[0].key < self.parent.parent.node[0].key:

                                if len(self.parent.children[0].node) > 1:

                                    self.parent.node.append(self.parent.children[0].node[0])
                                    self.parent.node.sort()

                                    L3 = TwoThreeFourTreeNode()
                                    L3.node = [self.parent.children[0].node[1]]
                                    L3.parent = self.parent

                                    R3 = TwoThreeFourTreeNode()
                                    R3.node = [self.parent.children[0].node[2]]
                                    R3.parent = self.parent

                                    self.parent.children.pop(0)
                                    self.parent.children.insert(0, R3)
                                    self.parent.children.insert(0, L3)

                                    del self.parent.children[0].node[1]

                                else:

                                    self.parent.node.append(self.parent.parent.node[0])
                                    self.parent.node.sort()

                                    L3 = TwoThreeFourTreeNode()
                                    L3.node = [self.parent.children[0].node[0]]
                                    L3.parent = self.parent

                                    R3 = TwoThreeFourTreeNode()
                                    R3.node = [self.parent.children[0].node[2]]
                                    R3.parent = self.parent

                                    self.parent.children.pop(0)
                                    self.parent.children.insert(0, R3)
                                    self.parent.children.insert(0, L3)

                                    del self.parent.children[0].node[1]

                        else:
                            self.parent.parent.node.append(self.parent.node[0])
                            self.parent.parent.node.append(self.parent.parent.children[0].node[0])
                            self.parent.parent.node.sort()

                            self.parent.parent.children.insert(2, self.parent.parent.children[0].children[0])

                            self.parent.parent.children.insert(3, self.parent.parent.children[0].children[1])

                            self.parent.parent.children.insert(4, self.parent.children[0])

                            self.parent.parent.children.insert(5, self.parent.children[1])

                        parent = self.parent.parent
                        parent.children[2].parent = parent
                        parent.children[3].parent = parent
                        parent.children[4].parent = parent
                        parent.children[5].parent = parent

                        parent.children.pop(0)
                        parent.children.pop(0)

                        self.deleteItem(searchKey)
                        return True

                if self.isLeaf():

                    if len(self.node) < 1:
                        self.parent.children.remove(self)
                        return True

                    else:
                        if len(self.node) > 1:
                            del self.node[i]

                        elif len(self.parent.node) == 1:

                                if self.node[0].key < self.parent.node[0].key:
                                    self.parent.children[1].node.append(self.parent.node[0])
                                    self.parent.children[1].node.sort()
                                    del self.parent.node[0]
                                    del self.parent.children[0]
                                    return True
                                else:
                                    self.parent.children[0].node.append(self.parent.node[0])
                                    self.parent.children[0].node.sort()
                                    del self.parent.node[0]
                                    del self.parent.children[1]
                                    return True



                        elif len(self.parent.node) == 2:

                            total = len(self.parent.node)
                            for k, citem in enumerate(self.parent.children):
                                total += len(citem.node)

                            if total > 5:
                                if self.node[0].key < self.parent.node[0].key:

                                    if len(self.parent.children[1].node) > 1:

                                        self.node.clear()
                                        self.node.append(self.parent.node[0])
                                        del self.parent.node[0]
                                        self.parent.node.append(self.parent.children[1].node[0])
                                        self.parent.node.sort()
                                        del self.parent.children[1].node[0]
                                    else:
                                        self.node.clear()
                                        self.node.append(self.parent.node[1])
                                        del self.parent.node[1]
                                        self.parent.node.append(self.parent.children[2].node[0])
                                        self.parent.node.sort()
                                        del self.parent.children[2].node[0]

                                elif self.node[0].key < self.parent.node[1].key:

                                    if len(self.parent.children[0].node) < 1:
                                        self.node.clear()
                                        self.node.append(self.parent.node[0])
                                        del self.parent.node[0]
                                        self.parent.node.append(self.parent.children[1].node[0])
                                        self.parent.node.sort()
                                        del self.parent.children[1].node[0]
                                    else:
                                        self.node.clear()
                                        self.node.append(self.parent.node[1])
                                        del self.parent.node[1]
                                        self.parent.node.append(self.parent.children[2].node[0])
                                        self.parent.node.sort()
                                        del self.parent.children[2].node[0]
                                else:

                                    self.node.clear()
                                    self.node.append(self.parent.node[1])
                                    del self.parent.node[1]

                                    if len(self.parent.children[1].node) > 1:
                                        index = len(self.parent.children[1].node)
                                        self.parent.node.append(self.parent.children[1].node[index - 1])
                                        self.parent.node.sort()
                                        del self.parent.children[1].node[index - 1]
                                    else:
                                        self.parent.node.append(self.parent.children[1].node[0])
                                        self.parent.node.sort()
                                        del self.parent.children[1].node[0]
                                        self.parent.children[1].node.append(self.parent.node[0])
                                        del self.parent.node[0]
                                        index = len(self.parent.children[0].node)
                                        self.parent.node.append(self.children[0].node[index - 1])
                                        self.parent.node.sort()
                                        del self.children[0].node[index - 1]

                                return True

                            else:
                                if self.node[0].key < self.parent.node[0].key:
                                    self.parent.children[1].node.append(self.parent.node[0])
                                    self.parent.children[1].node.sort()
                                    del self.parent.node[0]
                                    del self.parent.children[0]
                                    return True

                                elif self.node[0].key < self.parent.node[1].key:
                                    self.parent.children[0].node.append(self.parent.node[0])
                                    self.parent.children[0].node.sort()
                                    del self.parent.node[0]
                                    del self.parent.children[1]
                                    return True
                                else:
                                    self.parent.children[1].node.append(self.parent.node[1])
                                    self.parent.children[1].node.sort()
                                    del self.parent.node[1]
                                    del self.parent.children[2]
                                    return True

                        elif len(self.parent.node) == 3:

                            total = len(self.parent.node)

                            for k, citem in enumerate(self.parent.children):
                                total += len(citem.node)

                            if total > 7:
                                if self.node[0].key < self.parent.node[0].key:
                                    self.node.clear()
                                    self.node.append(self.parent.node[0])
                                    del self.parent.node[0]
                                    self.parent.node.append(self.parent.children[1].node[0])
                                    self.parent.node.sort()
                                    del self.parent.children[1].node[0]
                                    if len(self.parent.children[1].node) > 0:
                                        return True

                                    self.parent.children[1].node.append(self.parent.node[1])
                                    del self.parent.node[1]
                                    self.parent.node.append(self.parent.children[2].node[0])
                                    self.parent.node.sort()
                                    del self.parent.children[2].node[0]
                                    if len(self.parent.children[2].node) > 0:
                                        return True

                                    self.parent.children[2].node.append(self.parent.node[2])
                                    del self.parent.node[2]
                                    self.parent.node.append(self.parent.children[3].node[0])
                                    self.parent.node.sort()
                                    del self.parent.children[3].node[0]
                                    return True


                                elif self.node[0].key < self.parent.node[1].key:

                                    if len(self.parent.children[0].node) > 1:
                                        index = len(self.parent.children[0].node)
                                        self.node.clear()
                                        self.node.append(self.parent.node[0])
                                        del self.parent.node[0]
                                        self.parent.node.append(self.parent.children[0].node[index - 1])
                                        self.parent.node.sort()
                                        del self.parent.children[0].node[index - 1]
                                        return True

                                    self.node.clear()
                                    self.node.append(self.parent.node[1])
                                    del self.parent.node[1]
                                    self.parent.node.append(self.parent.children[2].node[0])
                                    self.parent.node.sort()
                                    del self.parent.children[2].node[0]
                                    if len(self.parent.children[2].node) > 0:
                                        return True

                                    self.parent.children[2].node.append(self.parent.node[2])
                                    del self.parent.node[2]
                                    self.parent.node.append(self.parent.children[3].node[0])
                                    self.parent.node.sort()
                                    del self.parent.children[3].node[0]
                                    return True

                                elif self.node[0].key < self.parent.node[2].key:

                                    if len(self.parent.children[1].node) < 1:
                                        self.node.clear()
                                        self.node.append(self.parent.node[1])
                                        del self.parent.node[1]
                                        self.parent.node.append(self.parent.children[2].node[0])
                                        self.parent.node.sort()
                                        del self.parent.children[2].node[0]
                                        if len(self.parent.children[2].node) > 0:
                                            return True

                                        self.parent.children[2].node.append(self.parent.node[2])
                                        del self.parent.node[2]
                                        self.parent.node.append(self.parent.children[3].node[0])
                                        self.parent.node.sort()
                                        del self.parent.children[3].node[0]
                                        return True
                                    else:
                                        self.node.clear()
                                        self.node.append(self.parent.node[2])
                                        del self.parent.node[2]
                                        self.parent.node.append(self.parent.children[3].node[0])
                                        self.parent.node.sort()
                                        del self.parent.children[3].node[0]
                                        return True
                                else:
                                    self.node.clear()
                                    self.node.append(self.parent.node[2])
                                    del self.parent.node[2]
                                    if len(self.parent.children[2].node) > 1:
                                        index = len(self.parent.children[2].node)
                                        self.parent.node.append(self.parent.children[2].node[index - 1])
                                        self.parent.node.sort()
                                        del self.parent.children[2].node[index - 1]
                                        return True
                                    else:
                                        self.parent.node.append(self.parent.children[2].node[0])
                                        self.parent.node.sort()
                                        del self.parent.children[2].node[0]
                                        self.parent.children[2].node.append(self.parent.node[1])
                                        del self.parent.node[1]

                                        if len(self.parent.children[1].node) > 1:
                                            index = len(self.parent.children[1].node)
                                            self.parent.node.append(self.parent.children[1].node[index - 1])
                                            self.parent.node.sort()
                                            del self.parent.children[1].node[index - 1]
                                            return True
                                        else:
                                            self.parent.node.append(self.parent.children[1].node[0])
                                            self.parent.node.sort()
                                            del self.parent.children[1].node[0]
                                            self.parent.children[1].node.append(self.parent.node[0])
                                            del self.parent.node[0]
                                        index = len(self.parent.children[0].node)
                                        self.parent.node.append(self.children[0].node[index - 1])
                                        self.parent.node.sort()
                                        del self.children[0].node[index - 1]
                                        return True
                            else:
                                if self.node[0].key < self.parent.node[0].key:
                                    self.parent.children[1].node.append(self.parent.node[0])
                                    self.parent.children[1].node.sort()
                                    del self.parent.node[0]
                                    del self.parent.children[0]
                                    return True
                                elif self.node[0].key < self.parent.node[1].key:
                                    self.parent.children[0].node.append(self.parent.node[0])
                                    self.parent.children[0].node.sort()
                                    del self.parent.node[0]
                                    del self.parent.children[1]
                                    return True
                                elif self.node[0].key < self.parent.node[2].key:
                                    self.parent.children[3].node.append(self.parent.node[2])
                                    self.parent.children[3].node.sort()
                                    del self.parent.node[2]
                                    del self.parent.children[2]
                                    return True
                                else:
                                    self.parent.children[2].node.append(self.parent.node[2])
                                    self.parent.children[2].node.sort()
                                    del self.parent.node[2]
                                    del self.parent.children[3]
                                    return True


                else:

                    if len(self.node) == 1:

                        if len(self.children[0].node) > 1:
                            del self.node[i]
                            index = len(self.children[0].node)
                            self.node.append(self.children[0].node[index - 1])
                            self.node.sort()
                            del self.children[0].node[index - 1]
                            return True
                        elif len(self.children[1].node) > 1:
                            del self.node[i]
                            self.node.append(self.children[1].node[0])
                            self.node.sort()
                            del self.children[1].node[0]
                            return True
                        else:
                            total = len(self.node)
                            for k, citem in enumerate(self.children):
                                total += len(citem.node)

                            if total == 3:
                                del self.node[i]
                                if i == 0:
                                    self.node.append(self.children[0].node[0])
                                    del self.children[0].node[0]
                                else:
                                    self.node.append(self.children[1].node[0])
                                    del self.children[1].node[0]
                                return True
                            else:
                                del self.node[i]
                                if i != 0:
                                    if len(self.children[1].node) > 1:
                                        index = len(self.children[1].node)
                                        self.node.append(self.children[1].node[index - 1])
                                        self.node.sort()
                                        del self.children[1].node[index - 1]
                                        self.node.append(self.children[2].node[0])
                                        self.node.sort()
                                        del self.children[2].node[0]
                                        self.children[2].node.append(self.node[1])
                                        del self.node[1]
                                        return True
                                    else:
                                        self.node.append(self.children[2].node[0])
                                        self.node.sort()
                                        del self.children[2].node[0]
                                        self.children[2].node.append(self.node[1])
                                        del self.node[1]
                                        self.node.append(self.children[3].node[0])
                                        del self.children[3].node[0]
                                        return True

                    elif len(self.node) == 2:

                        if i == 0:

                            if len(self.children[0].node) > 1:
                                del self.node[i]
                                index = len(self.children[0].node)
                                self.node.append(self.children[0].node[index - 1])
                                self.node.sort()
                                del self.children[0].node[index - 1]
                                return True
                            elif len(self.children[1].node) > 1:
                                del self.node[i]
                                self.node.append(self.children[1].node[0])
                                self.node.sort()
                                del self.children[1].node[0]
                                return True

                        if i == 1:
                            if len(self.children[1].node) < 1:
                                del self.node[i]
                                self.node.append(self.children[0].node[0])
                                del self.children[0].node[0]
                                return True

                            elif len(self.children[2].node) > 1:
                                del self.node[i]
                                index = len(self.children[2].node)
                                self.node.append(self.children[2].node[index - 1])
                                self.node.sort()
                                del self.children[2].node[index - 1]
                                return True

                        total = len(self.node)
                        for k, citem in enumerate(self.children):
                            total += len(citem.node)

                        if total == 5:

                            del self.node[i]

                            if i != 0:
                                self.node.append(self.children[1].node[0])
                                del self.children[1].node[0]
                            else:
                                self.node.append(self.children[0].node[0])
                                del self.children[0].node[0]
                            return True
                        else:
                            del self.node[i]
                            if i != 0:
                                if len(self.children[1].node) > 1:
                                    index = len(self.children[1].node)
                                    self.node.append(self.children[1].node[index - 1])
                                    self.node.sort()
                                    del self.children[1].node[index - 1]
                                    self.node.append(self.children[2].node[0])
                                    self.node.sort()
                                    del self.children[2].node[0]
                                    self.children[2].node.append(self.node[1])
                                    del self.node[1]
                                    return True
                                else:
                                    self.node.append(self.children[2].node[0])
                                    self.node.sort()
                                    del self.children[2].node[0]
                                    self.children[2].node.append(self.node[1])
                                    del self.node[1]
                                    self.node.append(self.children[3].node[0])
                                    del self.children[3].node[0]
                                    return True

                    elif len(self.node) == 3:

                        if i != 0:
                            if len(self.children[0].node) > 1:
                                del self.node[i]
                                index = len(self.children[0].node)
                                self.node.append(self.children[0].node[index - 1])
                                self.node.sort()
                                del self.children[0].node[index - 1]
                                return True
                            elif len(self.children[1].node) > 1:
                                del self.node[i]
                                self.node.append(self.children[1].node[0])
                                self.node.sort()
                                del self.children[1].node[0]
                                return True

                        if i == 1:
                            if len(self.children[1].node) < 1:
                                del self.node[i]
                                index = len(self.children[1].node)
                                self.node.append(self.children[1].node[index - 1])
                                self.node.sort()
                                del self.children[1].node[index - 1]
                                return True
                            elif len(self.children[2].node) > 1:
                                del self.node[i]
                                self.node.append(self.children[2].node[0])
                                self.node.sort()
                                del self.children[2].node[0]
                                return True

                        if i == 2:
                            if len(self.children[2].node) > 1:
                                del self.node[i]
                                index = len(self.children[2].node)
                                self.node.append(self.children[2].node[index - 1])
                                self.node.sort()
                                del self.children[2].node[index - 1]
                                return True
                            elif len(self.children[3].node) > 1:
                                del self.node[i]
                                self.node.append(self.children[3].node[0])
                                self.node.sort()
                                del self.children[3].node[0]
                                return True


                        total = len(self.node)
                        for k, citem in enumerate(self.children):
                            total += len(citem.node)

                        if total == 7:
                            del self.node[i]
                            if i == 0:
                                self.children[0].node.append(self.children[1].node[0])
                                del self.children[1]
                            elif i == 1:
                                self.children[1].node.append(self.children[2].node[0])
                                del self.children[2]
                            else:
                                self.children[2].node.append(self.children[3].node[0])
                                del self.children[3]
                            return True
                        else:
                            del self.node[i]
                            if i != 0:
                                if len(self.children[1].node) < 1:
                                    self.node.append(self.children[1].node[0])
                                    del self.children[1].node[0]
                                    return True
                                elif len(self.children[2].node) < 1:
                                    self.node.append(self.children[2].node[0])
                                    del self.children[2].node[0]
                                    return True
                            else:
                                if len(self.children[0].node) > 1:
                                    index = len(self.children[0].node)
                                    self.node.append(self.children[0].node[index - 1])
                                    self.node.sort()
                                    del self.children[0].node[index - 1]
                                    self.node.append(self.children[1].node[0])
                                    self.node.sort()
                                    del self.children[1].node[0]
                                    self.children[1].node.append(self.node[1])
                                    del self.node[1]
                                    return True
                                elif len(self.children[1].node) > 1:
                                    self.node.append(self.children[1].node[0])
                                    self.node.sort()
                                    del self.children[1].node[0]
                                    self.children[1].node.append(self.node[1])
                                    del self.node[1]
                                    self.node.append(self.children[2].node[0])
                                    del self.children[2].node[0]
                                    return True
                            if i == 1:
                                if len(self.children[0].node) > 1:
                                    index = len(self.children[0].node)
                                    self.node.append(self.children[0].node[index - 1])
                                    del self.children[0].node[index - 1]
                                    self.node.append(self.children[1].node[0])
                                    self.node.sort()
                                    del self.children[1].node[0]
                                    self.children[1].node.append(self.node[1])
                                    del self.node[1]
                                    return True
                                else:
                                    self.node.append(self.children[2].node[0])
                                    self.node.sort()
                                    del self.children[2].node[0]
                                    self.children[2].node.append(self.node[2])
                                    del self.node[2]
                                    self.node.append(self.children[3].node[0])
                                    del self.children[3].node[0]
                                    return True

                            else:
                                self.node.append(self.children[2].node[0])
                                self.node.sort()
                                self.children[2].node.clear()
                                self.children[2].node.append(self.node[2])
                                del self.node[2]
                                self.node.append(self.children[3].node[0])
                                del self.children[3].node[0]
                                return True

        if not self.isLeaf():
            for i in range(len(self.node)):
                if searchKey < self.node[i].key:
                    return self.children[i].deleteItem(searchKey)

            return self.children[-1].deleteItem(searchKey)
        return False


class TwoThreeFourTree:

    def __init__(self):
        """
        Precondities:
        - Geen specifieke precondities.

        Postcondities:
        - Een nieuw TwoThreeFourTree-object wordt aangemaakt met een lege wortel.
        """
        self.root = TwoThreeFourTreeNode()

    def isEmpty(self):
        """
        Precondities:
        - Geen specifieke precondities.

        Postcondities:
        - Retourneert True als de boom leeg is, anders retourneert False.
        """
        return self.root.isEmpty()

    def insertItem(self, insertTreeItemType):
        """
        Precondities:
        - insertTreeItemType is een object van een type dat kan worden ingevoegd in het boomknooppunt.

        Postcondities:
        - Voegt het gegeven insertTreeItemType toe aan het TwoThreeFourTree-object.
        """

        Inserted = self.root.insertItem(insertTreeItemType)

        if Inserted:
            if self.root.parent is not None:
                self.root = self.root.parent

        return Inserted

    def retrieveItem(self, searchKey):
        """
        Precondities:
        - searchKey is van hetzelfde type als de sleutels die kunnen worden opgevraagd in het boomknooppunt.

        Postcondities:
        - Retourneert een tuple (value, True) als searchKey wordt gevonden in de boom, anders retourneert (None, False).
        """
        return self.root.retrieveItem(searchKey)

    def inorderTraverse(self, functie):
        """
        Precondities:
        - functie is een functie die kan worden toegepast op de sleutels van de knooppunten.

        Postcondities:
        - Voert de gegeven functie uit op de sleutels van de knooppunten in inorder volgorde.
        """
        self.root.inorderTraverse(functie)

    def save(self):
        """
        Precondities:
        - Geen specifieke precondities.

        Postcondities:
        - Retourneert een dictionary die de huidige staat van het TwoThreeFourTree-object vertegenwoordigt.
        """
        return self.root.save()

    def load(self, items):
        """
        Precondities:
        - items is een dictionary met minimaal een "root" key.
        - Elk element in "root" is van hetzelfde type als de sleutels die kunnen worden ingevoegd in het boomknooppunt.

        Postcondities:
        - Maakt een nieuwe lege wortel aan en laadt de staat van het TwoThreeFourTree-object vanuit de gegeven items.
        """
        self.root = TwoThreeFourTreeNode();
        self.root.load(items)

    def deleteItem(self, searchKey):
        """
        Precondities:
        - searchKey is van hetzelfde type als de sleutels die kunnen worden ingevoegd in het boomknooppunt.

        Postcondities:
        - Verwijdert het item met de opgegeven searchKey uit het TwoThreeFourTree-object en retourneert True als het item succesvol is verwijderd, anders retourneert False.
        """
        return self.root.deleteItem(searchKey)

    def split(self):

        """
        Preconditie:
        De split-methode wordt opgeroepen op een object van de klasse TwoThreeFourTreeNode.

        Postconditie:
        Het huidige knooppunt wordt gesplitst in twee knooppunten en de middelste waarde wordt teruggegeven.
        """

        if len(self.node) == 3:
            middle = self.node.pop(1)
            left = TwoThreeFourTreeNode()
            right = TwoThreeFourTreeNode()

            left.node.append(self.node.pop(0))
            right.node.append(self.node.pop(0))

            left.children.extend(self.children[:2])
            right.children.extend(self.children[2:])

            self.node = [middle]
            self.children = [left, right]

            # Ensure children are set to None if the corresponding root entry is None
            for i, child in enumerate(self.children):
                if any(entry is None for entry in left.node + right.node):
                    self.children[i] = None

            return True
        else:
            return False

# t = TwoThreeFourTree()
# print(t.isEmpty())
# print(t.insertItem(createTreeItem(8,8)))
# print(t.insertItem(createTreeItem(5,5)))
# print(t.insertItem(createTreeItem(10,10)))
# print(t.insertItem(createTreeItem(15,15)))
# print(t.isEmpty())
# print(t.retrieveItem(5)[0])
# print(t.retrieveItem(5)[1])
# t.inorderTraverse(print)
# print(t.save())
# t.load({'root': [10],'children':[{'root':[5]},{'root':[11]}]})
# t.insertItem(createTreeItem(15,15))
# print(t.deleteItem(0))
# print(t.save())
# print(t.deleteItem(10))
# print(t.save())
# t = TwoThreeFourTree()
# t.insertItem(createTreeItem(5, 5))
# t.insertItem(createTreeItem(10, 10))
# t.insertItem(createTreeItem(2, 2))
# t.insertItem(createTreeItem(12, 12))
# t.insertItem(createTreeItem(15, 15))
# t.insertItem(createTreeItem(1, 1))
# t.insertItem(createTreeItem(3, 3))
# t.insertItem(createTreeItem(4, 4))
# t.insertItem(createTreeItem(16, 16))
# t.insertItem(createTreeItem(13, 13))
# t.inorderTraverse(print)
# print(t.save())
# t = TwoThreeFourTree()
# t.insertItem(createTreeItem(5,5))
# t.insertItem(createTreeItem(10,10))
# t.insertItem(createTreeItem(2,2))
# t.insertItem(createTreeItem(12,12))
# t.insertItem(createTreeItem(15,15))
# print(t.save())
# t = TwoThreeFourTree()
# t.load({'root': [5], 'children': [{'root': [2], 'children': [{'root': [1]}, {'root': [3, 4]}]}, {'root': [12], 'children': [{'root': [10]}, {'root': [13, 15, 16]}]}]})
# t.deleteItem(13)
# t.deleteItem(10)
# t.deleteItem(16)
# print(t.save())
# t = TwoThreeFourTree()
# t.load({'root': [2, 5], 'children': [{'root': [1]}, {'root': [3, 4]}, {'root': [12, 15]}]})
# t.insertItem(createTreeItem(10,10))
# t.insertItem(createTreeItem(13,13))
# t.deleteItem(3)
# t.deleteItem(5)
# print(t.save())


