# Define a dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[name] = {"phone": phone, "email": email}
        print("Contact added successfully!")

# Function to display all contacts
def display_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContacts:")
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f" Phone: {details['phone']}")
            print(f" Email: {details['email']}")
            print("-" * 20)

# Function to search for a contact by name
def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        details = contacts[name]
        print(f"Name: {name}")
        print(f" Phone: {details['phone']}")
        print(f" Email: {details['email']}")
    else:
        print("Contact not found!")

# Function to delete a contact by name
def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

# Main menu
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        display_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

  #Run the contact book menu
        menu()
