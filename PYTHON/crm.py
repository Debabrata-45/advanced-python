class Customer:
    def __init__(self, customer_id, name, email, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.communication_logs = []
        self.sales = []

    def add_communication(self, message):
        self.communication_logs.append(message)

    def add_sale(self, sale):
        self.sales.append(sale)

    def total_sales_value(self):
        total = 0
        for sale in self.sales:
            total += sale.amount
        return total

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}"


class Sale:
    def __init__(self, sale_id, product_name, amount):
        self.sale_id = sale_id
        self.product_name = product_name
        self.amount = amount

    def __str__(self):
        return f"Sale ID: {self.sale_id}, Product: {self.product_name}, Amount: {self.amount}"


class CRM:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer
        print(f"Customer {customer.name} added")

    def log_communication(self, customer_id, message):
        if customer_id in self.customers:
            self.customers[customer_id].add_communication(message)
            print("Communication logged")
        else:
            print("Customer not found")

    def add_sale_to_customer(self, customer_id, sale):
        if customer_id in self.customers:
            self.customers[customer_id].add_sale(sale)
            print("Sale added")
        else:
            print("Customer not found")

    def show_customer_details(self, customer_id):
        if customer_id in self.customers:
            customer = self.customers[customer_id]
            print("\nCustomer Details")
            print(customer)

            print("\nCommunication Logs:")
            if customer.communication_logs:
                for log in customer.communication_logs:
                    print("-", log)
            else:
                print("No communication logs")

            print("\nSales:")
            if customer.sales:
                for sale in customer.sales:
                    print(sale)
            else:
                print("No sales records")

            print(f"\nTotal Sales Value: {customer.total_sales_value()}")
        else:
            print("Customer not found")

    def sales_report(self):
        print("\nCRM Sales Report")
        for customer in self.customers.values():
            print(f"{customer.name} -> Total Sales: {customer.total_sales_value()}")