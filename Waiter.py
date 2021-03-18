from Diner import Diner
from Menu import Menu

class Waiter: # it will be a simulator of usual waiter in the restaraunt
    def __init__(self,menu):

        self.menu = menu

        self.diners = []

    def addDiner(self, diner): # adds a new thing to the waiter
        self.diners.append(diner)


    def getterAmountDiners(self): # the number of things in operation
        return len(self.diners)


    def printDinerStatuses(self): # grouped by the statuses
        amountStatuses={}
        for status in Diner.STATUSES:
            amountStatuses[status] = []
        for diner in self.diners:
            amountStatuses[Diner.STATUSES[diner.getterStatus()]].append(diner)

        for status in Diner.STATUSES:
            print("Diners who are", status, ":")
            for diner in amountStatuses[status]:
                print(diner)


    def getterOrder(self):

        for diner in self.diners:

            if Diner.STATUSES[diner.getterStatus()] == "ordering": #checking the status of the dinner

                for menutype in Menu.MENU_ITEM_TYPES:

                    self.menu.printMenuItemsByType(menutype)

                    print("{}, please select a {} menu item number.".format(diner.getterName(),menutype))

                    choice = -1
                    while choice <0 or choice > self.menu.getNumMenuItemsByType(menutype):
                        choice = int(input("> "))

                    diner.addToOrder(self.menu.getMenuItem(menutype,choice))
                diner.printOrder()


    def ringDiners(self):

        for diner in self.diners: # checking the status of the dinner that is paying
            if Diner.STATUSES[diner.getterStatus()] == "paying":

                print(diner.getterName(), " , your meal cost $", diner.MealCost)

    def removeDiners(self):
        for diner in self.diners:
            if Diner.STATUSES[diner.getterStatus()]== "leaving":
                # For each diner that is leaving, print a message thanking the diner.
                print( diner.getterName, ", thank you for dining with us! Come again soon!")
        # Loop through the list of diners backwards.
        for numbers in range(len(self.diners)-1, -1, -1):

            if Diner.STATUSES[self.diners[numbers].getterStatus()] == "leaving":
                self.diners.pop(numbers)

    def changeStatus(self): # in order to change the statuses of the dinner

        self.printDinerStatuses()
        self.getterOrder()
        self.ringDiners()
        self.removeDiners()
        for diner in self.diners:
            diner.changeStatus()
