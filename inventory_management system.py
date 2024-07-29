contact_book =[]
def add_contact():
    name = input('Name: ')
    phone = input('Phone: ')
    email = input('Email: ')

    contact_book.append({'Name': name, 'phone': phone, 'email': email})



add_contact()

print(contact_book)





