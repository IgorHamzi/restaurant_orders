class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.orders = list()
        self.foods = []

    def add_new_order(self, customer, order, day):
        self.orders.append((customer, order, day))
        self.foods.append(order)

    def get_quantities_to_buy(self):
        for i in self.foods:
            for j in self.INGREDIENTS[i]:
                self.MINIMUM_INVENTORY[j] -= 1

        for k in self.MINIMUM_INVENTORY:
            if k == 'queijo':
                self.MINIMUM_INVENTORY[k] = 100 - self.MINIMUM_INVENTORY[k]
            else:
                self.MINIMUM_INVENTORY[k] = 50 - self.MINIMUM_INVENTORY[k]

        return self.MINIMUM_INVENTORY
