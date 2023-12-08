# Abstract Data Type (ADT): LinkedChain
#
# Doel:
#     De LinkedChain ADT implementeert een dubbel gelinkte lijst, waarin elk element (Node) een waarde kan opslaan.
#     De lijst ondersteunt basisbewerkingen zoals invoegen, verwijderen, ophalen en beheren van de lengte.
#
# Gebruik:
#     - Initialiseer een LinkedChain met LinkedChain()
#     - Voeg een element in op een specifieke index met insert(index, waarde)
#     - Verwijder een element op een specifieke index met delete(index)
#     - Haal de lengte van de lijst op met getLength()
#     - Haal de waarde op van een element op een specifieke index met retrieve(index)
#     - Sla de waarden van de lijst op in een lijst met save()
#     - Laad waarden in de lijst vanuit een lijst met load(waardes)
class Node:
    def __init__(self, waarde):
        """
        Node constructor.

        Preconditie: waarde is het te bewaren element.
        Postconditie: Initialiseert een nieuwe node met de gegeven waarde en standaard next- en prev-pointers.

        Parameters:
        - waarde: Het element dat moet worden bewaard in de node.
        """
        self.waarde = waarde
        self.next = None
        self.prev = None


class LinkedChain:
    def __init__(self):
        """
        LinkedChain constructor.

        Postconditie: Initialiseert een lege LinkedChain met head ingesteld op None en length ingesteld op 0.
        """
        self.head = None
        self.length = 0

    def isEmpty(self):
        """
        Controleert of de LinkedChain leeg is.

        Postconditie: Geeft True terug als de LinkedChain leeg is, anders False.
        """
        return self.head is None

    def insert(self, index, waarde):
        """
        Voegt een nieuwe node met de gegeven waarde in op de opgegeven index in de LinkedChain.

        Preconditie: index is een geldige index (1 tot length + 1) waar de node moet worden ingevoegd.
                     waarde is het element dat moet worden bewaard in de nieuwe node.
        Postconditie: Als de invoeging succesvol is, geeft True terug; anders geeft het False terug.

        Parameters:
        - index: De index waar de nieuwe node moet worden ingevoegd.
        - waarde: Het element dat moet worden bewaard in de nieuwe node.
        """
        if index > (self.length + 1) or index < 1:
            return False

        new_node = Node(waarde)

        if self.isEmpty():
            # Invoegen in een lege LinkedChain
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            current = self.head

            for _ in range(index - 1):
                current = current.next

            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node

            if index == 1:
                self.head = new_node

        self.length += 1
        return True

    def delete(self, index):
        """
        Verwijdert de node op de opgegeven index in de LinkedChain.

        Preconditie: index is een geldige index (1 tot length) waar de node moet worden verwijderd.
        Postconditie: Als de verwijdering succesvol is, geeft True terug; anders geeft het False terug.

        Parameters:
        - index: De index van de node die moet worden verwijderd.
        """
        if self.isEmpty() or index > self.length or index < 1:
            return False

        current = self.head

        for _ in range(index - 1):
            current = current.next

        current.prev.next = current.next
        current.next.prev = current.prev

        if index == 1:
            self.head = self.head.next

        self.length -= 1

        if self.length == 0:
            self.head = None

        return True

    def getLength(self):
        """
        Geeft de lengte van de LinkedChain terug.

        Postconditie: Geeft de lengte van de LinkedChain terug.
        """
        return self.length

    def retrieve(self, index):
        """
        Haalt de waarde op die is opgeslagen in de node op de opgegeven index.

        Preconditie: index is een geldige index (1 tot length) om de waarde op te halen.
        Postconditie: Als het ophalen succesvol is, geeft het de waarde en True terug; anders geeft het None en False terug.

        Parameters:
        - index: De index om de waarde op te halen.
        """
        if self.isEmpty() or index < 1 or index > self.length:
            return None, False

        current = self.head

        for _ in range(index - 1):
            current = current.next

        return current.waarde, True

    def save(self):
        """
        Slaat de waarden van alle nodes in de LinkedChain op in een lijst.

        Postconditie: Geeft een lijst terug met de waarden van alle nodes in de LinkedChain.
        """
        if self.isEmpty():
            return []

        waardes = []
        current = self.head

        for _ in range(self.length):
            waardes.append(current.waarde)
            current = current.next

        return waardes

    def load(self, waardes):
        """
        Laadt waarden uit een lijst in de LinkedChain.

        Preconditie: waardes is een lijst van waarden die moeten worden ingevoegd in de LinkedChain.
        Postconditie: Wist de bestaande LinkedChain en voegt waarden in vanuit de lijst.

        Parameters:
        - waardes: Een lijst van waarden die moeten worden ingevoegd in de LinkedChain.
        """
        self.head = None
        self.length = 0

        for waarde in waardes:
            self.insert(self.length + 1, waarde)


l = LinkedChain()
print(l.isEmpty())
print(l.getLength())
print(l.retrieve(4)[1])
print(l.insert(4, 500))
print(l.isEmpty())
print(l.insert(1, 500))
print(l.retrieve(1)[0])
print(l.retrieve(1)[1])
print(l.save())
print(l.insert(1, 600))
print(l.save())
l.load([10, -9, 15])
l.insert(3, 20)
print(l.delete(0))
print(l.save())
print(l.delete(1))
print(l.save())
