contact_book = {}

def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone: ").strip()
    email = input("Enter Email: ").strip()
    
    contact_book[name.lower()] = {
        'phone': phone,
        'email': email
    }
    print("Contact added successfully.")

def search_contact():
    name = input("Enter Name to Search: ").strip().lower()
    contact = contact_book.get(name)
    
    if contact:
        print(f"Name: {name.title()}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter Name to Delete: ").strip().lower()
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def display_contacts():
    if not contact_book:
        print("No contacts available.")
        return

    print("\nAll Contacts")
    for name, details in contact_book.items():
        print(f"Name: {name.title()}, Phone: {details['phone']}, Email: {details['email']}")

def main():
    while True:
        print("\n Contact Book Menu")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display All Contacts")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            display_contacts()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":

    main()