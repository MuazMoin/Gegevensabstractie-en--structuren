# Abstract Data Type (ADT): MyStack
# Omschrijving: Deze ADT representeert een stapel met een gespecificeerde maximale lengte.

class MyStack:
    def __init__(self, lengte):
        """
        Initialiseert een lege stack met een opgegeven maximale lengte.

        Parameters:
        - lengte: de maximale lengte van de stack

        Preconditie:
        - De waarde van `lengte` moet een strikt positief geheel getal zijn.
        """

        self.stack = []
        self.size = lengte

    def push(self, waarde):
        """
        Voegt een waarde toe aan de bovenkant van de stack.

        Parameters:
        - waarde: de waarde die aan de stack moet worden toegevoegd

        Return:
        - tuple: (True,) als de operatie slaagt, (False,) als de stack vol is

        Preconditie:
        - De waarde van `waarde` mag niet gelijk zijn aan None.

        Postconditie:
        - Als het resultaat True is, dan is de waarde aan de bovenkant van de stack toegevoegd.
        """

        if len(self.stack) >= self.size:
            return False
        else:
            self.stack.append(waarde)
            return True

    def pop(self):
        """
        Verwijdert en geeft de waarde aan de bovenkant van de stack terug.

        Return:
        - tuple: (waarde, True) als de stack niet leeg is, (None, False) als de stack leeg is

        Postcondities:
        - Als het resultaat True is, dan is de waarde aan de bovenkant van de stack verwijderd.
        """
        if self.stack:
            return self.stack.pop(), True
        else:
            return None, False

    def isEmpty(self):
        """
        Controleert of de stack leeg is.

        Return:
        - tuple: (True,) als de stack leeg is, (False,) als de stack niet leeg is

        Postcondities:
        - De interne toestand van de stack wordt niet gewijzigd.
        """
        return not bool(self.stack)

    def getTop(self):
        """
        Geeft de waarde aan de bovenkant van de stack terug zonder deze te verwijderen.

        Return:
        - tuple: (waarde, True) als de stack niet leeg is, (None, False) als de stack leeg is

        Postcondities:
        - De interne toestand van de stack wordt niet gewijzigd.
        """

        if self.stack:
            return self.stack[-1], True
        else:
            return None, False

    def getList(self):
        """
        Geeft de stack terug als een tuple.

        Return:
        - tuple: tuple met de elementen van de stack

        Postcondities:
        - De interne toestand van de stack wordt niet gewijzigd.
        """
        return tuple(self.stack)

    def save(self):
        """
        Geeft de stack terug als een stringrepresentatie van een lijst.

        Return:
        - stringrepresentatie van de stack

        Postcondities:
        - De interne toestand van de stack wordt niet gewijzigd.
        """
        return str(self.stack)

    def load(self, waardes):
        """
        Vervangt de huidige stack door de opgegeven waardes.

        Parameters:
        - waardes: lijst van waardes om aan de stack toe te voegen

        Postcondities:
        - De interne toestand van de stack is vervangen door de opgegeven waardes.
        """
        self.stack = waardes


"""
testcode:

s = MyStack(5)
print(s.isEmpty())
print(s.getTop()[1])
print(s.pop()[1])
print(s.push(2))
print(s.push(4))
print(s.push(1))
print(s.isEmpty())
print(s.pop()[0])
s.push(5)
print(s.save())

s.load(['a', 'b', 'c'])
print(s.save())
print(s.pop()[0])
print(s.save())
print(s.getTop()[0])
print(s.save())

"""
