# ADT: MyQueue - Abstract Data Type for a Queue
class MyQueue:
    def __init__(self, lengte):

        """
         Initialiseert een lege queue met een opgegeven maximale lengte.

         Parameters:
         - lengte: Maximale lengte van de queue
         """

        self.queue = []
        self.lengte = lengte


    def enqueue(self, value):

        """
        Voegt een waarde toe aan de achterkant van de queue.

        Parameters:
        - value: De waarde die aan de queue moet worden toegevoegd

        Return:
        - Een tuple (resultaat, TOF). Resultaat is True als de waarde succesvol is toegevoegd,
          anders False. TOF is altijd True.

        Preconditie:
        - De waarde van `value` mag niet gelijk zijn aan None.

        Postconditie:
        - Als het resultaat True is, dan is de waarde aan de achterkant van de queue toegevoegd.
        """

        if len(self.queue) >= self.lengte:
            return False
        else:
            self.queue.insert(0, value)
            return True

    def dequeue(self):

        """
        Verwijdert en geeft de voorkant van de queue terug.

        Return:
        - Een tuple (waarde, TOF). Waarde is de voorkant van de queue als de queue niet leeg is,
          anders None. TOF is True als de operatie succesvol is, anders False.

        Preconditie:
        - Geen specifieke precondities.

        Postconditie:
        - Als het resultaat True is, dan is de voorkant van de queue verwijderd.
        """

        if self.queue:
            return (self.queue.pop(), True)
        else:
            return None, False

    def getFront(self):

        """
        Geeft de waarde aan de voorkant van de queue terug.

        Return:
        - Een tuple (waarde, TOF). Waarde is de voorkant van de queue als de queue niet leeg is,
          anders None. TOF is True als de operatie succesvol is, anders False.

        Preconditie:
        - Geen specifieke precondities.

        Postconditie:
        - De interne toestand van de queue wordt niet gewijzigd.
        """

        if self.queue:
            return (self.queue[-1], True)
        else:
            return (None, False)

    def isEmpty(self):
        """
        Controleert of de queue leeg is.

        Return:
        - Een tuple (leeg, TOF). Leeg is True als de queue leeg is, anders False.
          TOF is altijd True.

        Postconditie:
        - De interne toestand van de queue wordt niet gewijzigd.
        """

        return not bool(self.queue)

    def save(self):

        """
        Geeft de queue terug als een stringrepresentatie van een lijst met de voorkant van de queue vooraan.

        Return:
        - Een tuple (representatie, TOF). Representatie is de stringrepresentatie van de queue.
          TOF is altijd True.

        Postconditie:
        - De interne toestand van de queue wordt niet gewijzigd.

        """

        return str(self.queue)

    def load(self, values):
        """
        Voegt elementen toe van de ingevoerde waardes aan de achterkant van de queue.

        Parameters:
        - values: Lijst van waardes om aan de queue toe te voegen

        Return:
        - Een tuple (resultaat, TOF). Resultaat is True als de waardes succesvol zijn toegevoegd,
          anders False.  is altijd True.


        Postconditie:
        - De waardes zijn aan de achterkant van de queue toegevoegd.
        """

        self.queue = values


        #indien er geen specifieke preconditie aanwezig was, dan heb ik deze niet genoteerd om zo mijn aantal lijnen code te berperken (of ik heb het weergegeven als 'Geen specifieke precondities').


"""

testcode:

q = MyQueue(10)
print(q.isEmpty())
print(q.getFront()[1])
print(q.dequeue()[1])
print(q.enqueue(2))
print(q.enqueue(4))
print(q.isEmpty())
print(q.dequeue()[0])
q.enqueue(5)
print(q.save())

q.load(['a', 'b', 'c'])
print(q.save())
print(q.dequeue()[0])
print(q.save())
print(q.getFront()[0])
print(q.save())

"""
