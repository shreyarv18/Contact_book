import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load existing contacts
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

# Save contacts to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    contact = {"name": name, "phone": phone, "email": email}

    contacts = load_contacts()
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts():
    contacts = load_contacts()
    if contacts:
        print("\n--- Contact List ---")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("\nNo contacts found!")
        

# Search for a contact by name
def search_contact():
    name_to_search = input("Enter the name to search: ")
    contacts = load_contacts()

    # Search for the contact
    matching_contacts = [contact for contact in contacts if contact["name"].lower() == name_to_search.lower()]

    if matching_contacts:
        print("\n--- Search Results ---")
        for contact in matching_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("\nNo contact found with that name!")


# Main menu
def menu():
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact by Name")  # New option
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()  # Calls the new search function
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


# Start the app
if __name__ == "__main__":
    menu()
