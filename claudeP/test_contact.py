from contact import add_contact, find_contact, delete_contact 

def test_add():
    contacts = {}
    add_contact(contacts, "Abz", "08012345678", "abz@email.com")
    assert contacts["Abz"]["phone"] == "08012345678"

def test_find():
    contacts = {}
    add_contact(contacts, "Abz", "08012345678", "abz@email.com")
    assert find_contact(contacts, "Tobi") == "Contact not found"

def test_delete():
    contacts = {}
    add_contact(contacts, "Abz", "08012345678", "abz@email.com")
    assert delete_contact(contacts, "Abz") == "Contact deleted"
    assert delete_contact(contacts, "Tobi") == "Contact not found"