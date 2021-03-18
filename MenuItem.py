
class MenuItem: # it will show the alone item

    def __init__(self, name, kind, cost, explanation): #name, kind, cost and an explanation of the item

        self.name = name

        self.kind = kind

        self.cost = cost

        self.explanation = explanation

    # getters and setters for each of the 4 things
    def getterName(self):
        return self.name

    def getterKind(self):
        return self.kind

    def getterPrice(self):
        return self.cost

    def getDescription(self):
        return self.explanation


    def __str__(self):
        return f"{self.name} ({self.kind}): ${self.cost}\n         {self.explanation}"

