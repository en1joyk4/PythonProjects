
from MenuItem import MenuItem
class Diner: # THIS WILL REPRESENT THE ONE OF THE DINNERS AND ITS STATUSES
    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]

    def __init__(self, name): # representing the diner's name
        self.name = name

        self.sequence = []


        self.status = 0 # it represents the status of the dinenr



    def getterName(self): # setters and getters
        return self.name

    def setterName(self, name):
        self.name = name

    def getterOrder(self):
        return self.sequence

    def setterOrder(self, sequence):
        self.sequence = sequence

    def getterStatus(self):
        return self.status

    def setterStatus(self, status):
        self.status = status

    def changeStatus(self):
        self.status = self.status + 1

    def addToOrder(self, menuItem):
        self.sequence.append(menuItem)


    def printOrder(self):
        print(self.name, " ordered:")
        for items in self.sequence:
            print("-", items)

    def MealCost(self): #total cost of ordered neals

        totalCost = 0
        for item in self.sequence:
            totalCost = totalCost + item.getterPrice()

        return totalCost


    def __str__(self):
        return "Diner {} is currently {}.".format(self.name,Diner.STATUSES[self.status])
