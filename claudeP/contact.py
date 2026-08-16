def main():
    contacts = {}

    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    add_contact(contacts, name, phone, email)

def add_contact(contacts, name, phone, email):
    contact_info = {"phone": phone, "email": email}
    contacts[name] = contact_info


def find_contact(contacts, name):
    if name in contacts:
        return contacts[name]
    return "Contact not found"

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        return "Contact deleted"
    return "Contact not found"

if __name__ == "__main__":
    main()