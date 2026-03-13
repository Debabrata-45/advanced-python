class DuplicateContactError(Exception):
    pass


class EmptyFieldError(Exception):
    pass


class InvalidPhoneNumberError(Exception):
    pass


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class ContactBook:
    def __init__(self):
        self.contacts = {}

    def validate_contact(self, name, phone):
        if not name.strip() or not phone.strip():
            raise EmptyFieldError("Name and phone number cannot be empty.")

        if name in self.contacts:
            raise DuplicateContactError("Contact already exists.")

        if not phone.isdigit() or len(phone) != 10:
            raise InvalidPhoneNumberError("Phone number must be exactly 10 digits.")

    def add_contact(self, name, phone):
        self.validate_contact(name, phone)
        self.contacts[name] = Contact(name, phone)
        print("Contact added successfully.")

    def edit_contact(self, name, new_phone):
        if name not in self.contacts:
            raise EmptyFieldError("Contact not found.")

        if not new_phone.isdigit() or len(new_phone) != 10:
            raise InvalidPhoneNumberError("New phone number must be exactly 10 digits.")

        self.contacts[name].phone = new_phone
        print("Contact updated successfully.")

    def search_contact(self, name):
        if name not in self.contacts:
            raise EmptyFieldError("Contact not found.")

        contact = self.contacts[name]
        print(f"Name: {contact.name}, Phone: {contact.phone}")

    def view_all_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts.values():
                print(f"Name: {contact.name}, Phone: {contact.phone}")


def main():
    book = ContactBook()

    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Search Contact")
        print("4. View All Contacts")
        print("5. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                book.add_contact(name, phone)

            elif choice == "2":
                name = input("Enter contact name to edit: ")
                new_phone = input("Enter new phone number: ")
                book.edit_contact(name, new_phone)

            elif choice == "3":
                name = input("Enter contact name to search: ")
                book.search_contact(name)

            elif choice == "4":
                book.view_all_contacts()

            elif choice == "5":
                print("Exiting Contact Book.")
                break

            else:
                print("Invalid choice.")

        except (DuplicateContactError, EmptyFieldError, InvalidPhoneNumberError) as e:
            print("Error:", e)
        except Exception as e:
            print("Unexpected error:", e)


if __name__ == "__main__":
    main()