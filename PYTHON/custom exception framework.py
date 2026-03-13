class OutOfStockError(Exception):
    pass
class InvalidProductIDError(Exception):
    pass
class EmptyProductNameError(Exception):
    pass
class Product:
    def __init__(self, product_id, name, quantity):
        if not name.strip():
            raise EmptyProductNameError("Product name cannot be empty.")

        self.product_id = product_id
        self.name = name
        self.quantity = quantity
class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, quantity):
        if product_id in self.products:
            raise InvalidProductIDError("Product ID already exists.")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.products[product_id] = Product(product_id, name, quantity)
        print("Product added successfully.")

    def sell_product(self, product_id, amount):
        if product_id not in self.products:
            raise InvalidProductIDError("Product ID not found.")

        product = self.products[product_id]

        if product.quantity < amount:
            raise OutOfStockError("Not enough stock available.")

        product.quantity -= amount
        print("Product sold successfully.")

    def restock_product(self, product_id, amount):
        if product_id not in self.products:
            raise InvalidProductIDError("Product ID not found.")

        if amount <= 0:
            raise ValueError("Restock amount must be positive.")

        self.products[product_id].quantity += amount
        print("Product restocked successfully.")

    def view_inventory(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            for p in self.products.values():
                print(f"ID: {p.product_id}, Name: {p.name}, Quantity: {p.quantity}")


def main():
    inventory = Inventory()

    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add Product")
        print("2. Sell Product")
        print("3. Restock Product")
        print("4. View Inventory")
        print("5. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                pid = int(input("Enter product ID: "))
                name = input("Enter product name: ")
                qty = int(input("Enter quantity: "))
                inventory.add_product(pid, name, qty)

            elif choice == "2":
                pid = int(input("Enter product ID: "))
                amt = int(input("Enter quantity to sell: "))
                inventory.sell_product(pid, amt)

            elif choice == "3":
                pid = int(input("Enter product ID: "))
                amt = int(input("Enter quantity to restock: "))
                inventory.restock_product(pid, amt)

            elif choice == "4":
                inventory.view_inventory()

            elif choice == "5":
                print("Exiting Inventory System.")
                break

            else:
                print("Invalid choice.")

        except (OutOfStockError, InvalidProductIDError, EmptyProductNameError, ValueError) as e:
            print("Error:", e)
        except Exception as e:
            print("Unexpected error:", e)


if __name__ == "__main__":
    main()