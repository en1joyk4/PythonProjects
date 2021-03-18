from MenuItem import MenuItem

class Menu:

    MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree", "Dessert"] #item types i need to show


    def __init__(self,fileName):

        self.menuItemDictionary = {} # for the dictionary
        fileopen = open(fileName, "r" )
        for line in fileopen:
            splitting=line.strip().split(",")

            menuItem = MenuItem(splitting[0].strip(), splitting[1].strip(), float(splitting[2].strip()), splitting[3].strip())

            if menuItem.getterKind() in self.menuItemDictionary:
                self.menuItemDictionary[menuItem.getterKind()].append(menuItem)
            else:
                self.menuItemDictionary[menuItem.getterKind()] = [menuItem]

        fileopen.close()


    def getMenuItem(self,kind,index):
        return self.menuItemDictionary[kind][index]

    def printMenuItemsByType(self, kind): # print the types of meny items
        print("-----{}S-----".format(kind.upper()))
        counter = 0
        for items in self.menuItemDictionary[kind]:
            print("{} {})".format(counter, items))
            counter = counter + 1

    def getNumMenuItemsByType(self,kind): # the number of menuitesm
        return len(self.menuItemDictionary[kind])
