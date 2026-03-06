# Priyanshu pabari 590022242
contacts = {}
while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully!")
    elif choice == "2":
        name = input("Enter name to search: ")
        if name in contacts:
            print("Phone number:", contacts[name])
        else:
            print("Contact not found!")
    elif choice == "3":
        name = input("Enter name to update: ")
        if name in contacts:
            new_phone = input("Enter new phone number: ")
            contacts[name] = new_phone
            print("Contact updated successfully!")
        else:
            print("Contact not found!")
    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")
    elif choice == "5":
        print("\nAll Contacts:")
        for name in contacts:
            print(name, "->", contacts[name])
    elif choice == "6":
        print("Exiting Contact Book...")
        break
    else:
        print("Invalid choice! Please try again.")