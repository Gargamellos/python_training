from model.contact import Contact

def test_modify_contact_name(app):
    app.contact.modify_first_contact(Contact(name ="New contact"))

def test_modify_contact_middlename(app):
    app.contact.modify_first_contact(Contact(middlename ="New middlename"))