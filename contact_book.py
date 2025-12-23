def show_menu():
    print("\n------ Contact Book ------")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

contacts = []

def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print(f"✅ Contact '{name}' added!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\nAll Contacts:")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']} | {c['address']}")

def search_contact():
    query = input("Enter name or phone to search: ").strip()
    found = [c for c in contacts if query.lower() in c['name'].lower() or query in c['phone']]
    if found:
        print("Found Contacts:")
        for c in found:
            print(f"{c['name']} | {c['phone']} | {c['email']} | {c['address']}")
    else:
        print("No contact found.")

def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    for c in contacts:
        if c['name'].lower() == name.lower():
            c['phone'] = input(f"New Phone ({c['phone']}): ") or c['phone']
            c['email'] = input(f"New Email ({c['email']}): ") or c['email']
            c['address'] = input(f"New Address ({c['address']}): ") or c['address']
            print(f"✅ Contact '{name}' updated!")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    global contacts
    contacts = [c for c in contacts if c['name'].lower() != name.lower()]
    print(f"✅ Contact '{name}' deleted (if it existed).")

# Main program
while True:
    show_menu()
    choice = input("Choose an option (1-6): ").strip()
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
        print("❌ Invalid option. Try again.")
