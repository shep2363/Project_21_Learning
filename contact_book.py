contact = []
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contact.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully")

def search_contact():
    name = input("Enter name: ")
    for i in contact:
        if i["name"] == name:
            print(i)
            break
    else:
        print("Contact not found")
        

def delete_contact():
    name = input("Enter name: ")
    for i in contact:
        if i["name"] == name:
            contact.remove(i)
            print("Contact deleted successfully")
            break
    else:
        print("Contact not found")

def display_contact():
    for i in contact:
        print(i)

def main():
    while True:
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. Display contact")
        print("5. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            add_contact()
        elif choice == 2:
            search_contact()
        elif choice == 3:
            delete_contact()
        elif choice == 4:
            display_contact()
        elif choice == 5:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()