class Product:
    def __init__(self, product_id, name, quantity):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.movement_history = []

    def add_stock(self, amount):
        self.quantity += amount
        self.movement_history.append(("IN", amount))

    def remove_stock(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            self.movement_history.append(("OUT", amount))
        else:
            print(f"Not enough stock for {self.name}")

    def forecast_demand(self):
        total_out = 0
        out_count = 0

        for move_type, amount in self.movement_history:
            if move_type == "OUT":
                total_out += amount
                out_count += 1

        if out_count == 0:
            return 0

        return total_out / out_count

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Quantity: {self.quantity}"


class Warehouse:
    def __init__(self, warehouse_name):
        self.warehouse_name = warehouse_name
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product
        print(f"{product.name} added to warehouse")

    def move_goods_in(self, product_id, amount):
        if product_id in self.products:
            self.products[product_id].add_stock(amount)
            print(f"{amount} units added to {self.products[product_id].name}")
        else:
            print("Product not found")

    def move_goods_out(self, product_id, amount):
        if product_id in self.products:
            self.products[product_id].remove_stock(amount)
            print(f"{amount} units removed from {self.products[product_id].name}")
        else:
            print("Product not found")

    def inventory_report(self):
        print(f"\nInventory Report - {self.warehouse_name}")
        for product in self.products.values():
            print(product)

    def demand_forecast_report(self):
        print(f"\nDemand Forecast Report - {self.warehouse_name}")
        for product in self.products.values():
            forecast = product.forecast_demand()
            print(f"{product.name} -> Estimated future demand: {forecast:.2f} units")