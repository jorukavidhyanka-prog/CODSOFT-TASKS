import json
import os

CONTACTS_FILE = "contacts.json"


def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\n--- Contact List ---")
    for index, contact in enumerate(contacts, start=1):
        print(
            f"{index}. {contact['name']} | "
            f"Phone: {contact['phone']} | "
            f"Email: {contact['email']}"
        )


def search_contact(contacts):
    keyword = input("Enter name to search: ").lower()

    results = [
        contact for contact in contacts
        if keyword in contact["name"].lower()
    ]

    if results:
        print("\nSearch Results:")
        for contact in results:
            print(
                f"Name: {contact['name']}, "
                f"Phone: {contact['phone']}, "
                f"Email: {contact['email']}"
            )
    else:
        print("No matching contact found.")


def delete_contact(contacts):
    name = input("Enter contact name to delete: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")


def main():
    contacts = load_contacts()

    while True:
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()