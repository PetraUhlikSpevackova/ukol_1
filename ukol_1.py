class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name}:{self.price} Kč"

class Pizza (Item):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price)
        self.ingredients = ingredients
    
    def __str__(self):
        return f"{self.name} pizza za {self.price} Kč, ingredience jsou {self.ingredients}"
    
    def add_extra(self, ingredient, quantity, price_per_ingredient):
        self.ingredients[ingredient] = quantity*price_per_ingredient
        self.price += quantity*price_per_ingredient

class Drink (Item):
    def __init__(self, name, volume, price):
        super().__init__(name, price)
        self.volume = volume
    def __str__(self):
        return f"{self.name}, {self.volume} ml za {self.price} Kč"

class Order:
    def __init__(self, customer_name, delivery_address, items, status="New"):
        self.customer_name = customer_name
        self.delivery_address = delivery_address
        self.items = items
        self.status = status
    def mark_delivered(self):
        self.status = "Delivered"
    def __str__(self):
        return f"{self.customer_name}, {self.delivery_address}, {self.items}, {self.status}"

class DeliveryPerson:
    def __init__(self, name, phone_number, current_order, available = True):
        self.name = name
        self.phone_number = phone_number
        self.current_order = current_order
        self.available = available
    def assign_order(self, order):
        if self.available == True:
            self.current_order = order
            self.available = False
            print("Přiřazeno")
        else:
            print("Nepřiřazeno")
    def complete_delivery(self):
        self.current_order.mark_delivered()
        self.available = True
        print("Objednávka doručena")
    def __str__(self):
        return f"{self.name}, {self.phone_number}, {self.available}"