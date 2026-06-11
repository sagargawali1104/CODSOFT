# Contact Book Project

contacts = {}

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    print(f"Contact '{name}' added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\n--- Contact List ---")
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f" Phone: {info['Phone']}")
        print(f" Email: {info['Email']}")
        print(f" Address: {info['Address']}\n")

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"\nContact found: {name}")
        print(f" Phone: {info['Phone']}")
        print(f" Email: {info['Email']}")
        print(f" Address: {info['Address']}\n")
    else:
        print("Contact not found.\n")

def update_contact():
    name = input("Enter name to update: ").strip()
    if name in contacts:
        print("Leave blank if you don't want to change a field.")
        phone = input("New phone number: ").strip()
        email = input("New email: ").strip()
        address = input("New address: ").strip()

        if phone: contacts[name]["Phone"] = phone
        if email: contacts[name]["Email"] = email
        if address: contacts[name]["Address"] = address

        print(f"Contact '{name}' updated successfully!\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!\n")
    else:
        print("Contact not found.\n")

def main():
    while True:
        print("=== Contact Book ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
