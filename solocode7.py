from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculatecost(self):
        pass



class ByWeightItem(Item):
    def __init__(self, name, weight, costperpound):
        super().__init__(name)
        self.weight = weight
        self.costperpound = costperpound

    def calculatecost(self):
        return self.weight * self.costperpound


class ByQuantityItem(Item):
    def __init__(self, name, quantity, costeach):
        super().__init__(name)
        self.quantity = quantity
        self.costeach = costeach

    def calculatecost(self):
        return self.quantity * self.costeach



class Grapes(ByWeightItem):
    def __init__(self, weight):
        super().__init__("Grapes", weight, 2.99)


class Bananas(ByWeightItem):
    def __init__(self, weight):
        super().__init__("Bananas", weight, 0.59)


class Oranges(ByQuantityItem):
    def __init__(self, quantity):
        super().__init__("Oranges", quantity, 0.75)


class Cantaloupes(ByQuantityItem):
    def __init__(self, quantity):
        super().__init__("Cantaloupes", quantity, 3.50)



class Order:
    def __init__(self):
        self.items = []

    def additem(self, item):
        self.items.append(item)

    def calculatetotal(self):
        total = 0
        for item in self.items:
            total = total + item.calculatecost()
        return total

    def get_items(self):
        return self.items

    def __len__(self):
        return len(self.items)



order = Order()

order.additem(Grapes(2))
order.additem(Bananas(3))
order.additem(Oranges(5))
order.additem(Cantaloupes(1))

print("Receipt")
print("--------")

for item in order.get_items():
    cost = item.calculatecost()
    print(item.name, "-", "$" + format(cost, ".2f"))

print("--------")
print("Total:", "$" + format(order.calculatetotal(), ".2f"))
print("Number of items:", len(order))