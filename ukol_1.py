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
        final_price = self.price + price_per_ingredient
        return super().__str__() + f", celková cena včetně extra ingrediencí je {final_price} Kč"

class Drink (Item):
    def __init__(self, name, volume, price):
        super().__init__(name, price)
        self.volume = volume
    def __str__(self):
        return f"{self.name}, {self.volume} ml za {self.price} Kč"

class Order:
    def __init__(self, customer_name, delivery_address, items, status="Delivered"):
        self.customer_name = customer_name
        self.delivery_address = delivery_address
        self.items = items
        self.status = status
    def mark_delivered(self):
        if self.status == "Delivered":
            return "Objednávka doručena"
        else:
            return "Objednávka nedoručena"
    def __str__(self):
        return f"{self.customer_name}, {self.delivery_address}, {self.items}"

class DeliveryPerson:
    def __init__(self, name, phone_number, current_order, available = True):
        self.name = name
        self.phone_number = phone_number
        self.current_order = current_order
        self.available = available
    def assign_order(self):
        if self.available == True:
            return self.current_order == "Na cestě"
    def complete_delivery(self):
        if self.current_order == "Doručeno":
            return self.available == True
    def __str__(self):
        return f"{self.name}, {self.phone_number}, {self.available}"