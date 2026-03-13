class InvalidCouponError(Exception):
    pass
class OutOfStockError(Exception):
    pass
class InvalidPaymentMethodError(Exception):
    pass
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
class OrderManager:
    def __init__(self):
        self.products = {
            1: Product(1, "Laptop", 50000, 5),
            2: Product(2, "Phone", 25000, 0),
            3: Product(3, "Headphones", 2000, 10)
        }
        self.valid_coupons = {"SAVE10": 10, "SAVE20": 20}
        self.valid_payment_methods = ["UPI", "CARD", "COD"]

    def place_order(self, product_id, quantity, coupon_code, payment_method):
        if product_id not in self.products:
            raise ValueError("Invalid product ID.")

        product = self.products[product_id]

        if product.stock < quantity:
            raise OutOfStockError("Requested quantity is not available in stock.")

        discount = 0
        if coupon_code:
            if coupon_code not in self.valid_coupons:
                raise InvalidCouponError("Coupon code is invalid.")
            discount = self.valid_coupons[coupon_code]

        if payment_method.upper() not in self.valid_payment_methods:
            raise InvalidPaymentMethodError("Payment method is invalid.")

        total = product.price * quantity
        final_total = total - (total * discount / 100)

        product.stock -= quantity

        print("Order placed successfully.")
        print(f"Product: {product.name}")
        print(f"Quantity: {quantity}")
        print(f"Total Amount: {final_total}")

    def return_order(self, product_id, quantity):
        if product_id not in self.products:
            raise ValueError("Invalid product ID.")

        self.products[product_id].stock += quantity
        print("Return processed successfully.")

    def view_products(self):
        for p in self.products.values():
            print(f"ID: {p.product_id}, Name: {p.name}, Price: {p.price}, Stock: {p.stock}")
def main():
    manager = OrderManager()

    while True:
        print("\n--- E-Commerce Order Management ---")
        print("1. View Products")
        print("2. Place Order")
        print("3. Return Order")
        print("4. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                manager.view_products()

            elif choice == "2":
                product_id = int(input("Enter product ID: "))
                quantity = int(input("Enter quantity: "))
                coupon = input("Enter coupon code (or leave blank): ").strip()
                payment = input("Enter payment method (UPI/CARD/COD): ").strip().upper()
                manager.place_order(product_id, quantity, coupon, payment)

            elif choice == "3":
                product_id = int(input("Enter product ID: "))
                quantity = int(input("Enter returned quantity: "))
                manager.return_order(product_id, quantity)

            elif choice == "4":
                print("Exiting E-Commerce System.")
                break

            else:
                print("Invalid choice.")

        except (InvalidCouponError, OutOfStockError, InvalidPaymentMethodError, ValueError) as e:
            print("Error:", e)
        except Exception as e:
            print("Unexpected error:", e)


if __name__ == "__main__":
    main()