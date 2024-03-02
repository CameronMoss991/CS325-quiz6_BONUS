# s.py

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def remove_item(self, item_name):
        del self.items[item_name]

    def check_item_availability(self, item_name, quantity):
        if item_name in self.items and self.items[item_name].quantity >= quantity:
            return True
        return False

class Order:
    def __init__(self, customer, items, shipping_address):
        self.customer = customer
        self.items = items
        self.shipping_address = shipping_address

    def calculate_total_order_cost(self):
        total_cost = sum(item.price * item.quantity for item in self.items)
        # Apply taxes, discounts, etc.
        return total_cost

    def validate_order_data(self, inventory):
        for item in self.items:
            if not inventory.check_item_availability(item.name, item.quantity):
                return False
        # Add more validation checks for customer address, etc.
        return True

    def send_order_confirmation_email(self):
        # Send email logic here
        print("Sent an order confirmation")

    def update_inventory(self, inventory):
        for item in self.items:
            inventory.remove_item(item.name)

def main():
    customer = Customer("Dummy Man", "Man_dummy@example.com", "443 Frold St")
    items = [Item("Item 1", 10.0, 2), Item("Item 2", 20.0, 1)]
    shipping_address = "456 Elm St"

    inventory = Inventory()
    inventory.add_item(Item("Item 1", 10.0, 10))
    inventory.add_item(Item("Item 2", 20.0, 5))

    order = Order(customer, items, shipping_address)
    if order.validate_order_data(inventory):
        total_cost = order.calculate_total_order_cost()
        order.send_order_confirmation_email()
        order.update_inventory(inventory)
        print("Order processed successfully.")
    else:
        print("Order validation failed. Please check item availability.")

if __name__ == "__main__":
    main()
