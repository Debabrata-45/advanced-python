class SeatNotAvailableError(Exception):
    pass
class InvalidPassengerDetailsError(Exception):
    pass
class PaymentFailureError(Exception):
    pass
class Flight:
    def __init__(self, flight_number, source, destination, available_seats):
        self.flight_number = flight_number
        self.source = source
        self.destination = destination
        self.available_seats = available_seats


class Passenger:
    def __init__(self, name, age):
        if not name.strip():
            raise InvalidPassengerDetailsError("Passenger name cannot be empty.")
        if age <= 0:
            raise InvalidPassengerDetailsError("Invalid age entered.")

        self.name = name
        self.age = age


class FlightBookingSystem:
    def __init__(self):
        self.flights = {
            "AI101": Flight("AI101", "Delhi", "Mumbai", 2),
            "AI202": Flight("AI202", "Bhubaneswar", "Bangalore", 3)
        }

    def process_payment(self, amount, payment_status):
        if payment_status.lower() != "success":
            raise PaymentFailureError("Payment failed.")
        print(f"Payment of ₹{amount} successful.")

    def book_ticket(self, flight_number, passenger_name, age, payment_status):
        if flight_number not in self.flights:
            raise ValueError("Invalid flight number.")

        flight = self.flights[flight_number]

        if flight.available_seats <= 0:
            raise SeatNotAvailableError("No seats available on this flight.")

        passenger = Passenger(passenger_name, age)
        self.process_payment(5000, payment_status)

        flight.available_seats -= 1

        print("Ticket booked successfully.")
        print(f"Passenger: {passenger.name}")
        print(f"Flight: {flight.flight_number}")
        print(f"Route: {flight.source} -> {flight.destination}")

    def cancel_ticket(self, flight_number):
        if flight_number not in self.flights:
            raise ValueError("Invalid flight number.")

        self.flights[flight_number].available_seats += 1
        print("Ticket cancelled successfully.")

    def view_flights(self):
        for f in self.flights.values():
            print(
                f"Flight: {f.flight_number}, Route: {f.source} -> {f.destination}, Seats: {f.available_seats}"
            )


def main():
    system = FlightBookingSystem()

    while True:
        print("\n--- Flight Booking System ---")
        print("1. View Flights")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                system.view_flights()

            elif choice == "2":
                flight_no = input("Enter flight number: ")
                name = input("Enter passenger name: ")
                age = int(input("Enter passenger age: "))
                payment = input("Enter payment status (success/fail): ")
                system.book_ticket(flight_no, name, age, payment)

            elif choice == "3":
                flight_no = input("Enter flight number to cancel ticket: ")
                system.cancel_ticket(flight_no)

            elif choice == "4":
                print("Exiting Flight Booking System.")
                break

            else:
                print("Invalid choice.")

        except (SeatNotAvailableError, InvalidPassengerDetailsError, PaymentFailureError, ValueError) as e:
            print("Error:", e)
        except Exception as e:
            print("Unexpected error:", e)


if __name__ == "__main__":
    main()