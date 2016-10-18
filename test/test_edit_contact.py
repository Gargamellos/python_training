from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.edit_first_contact(Contact(name ="edit", middlename ="edit", surname ="edit", nick ="edit", title ="edit",
                               company = "edit", address = "edit", homephone = "edit", mobilephone = "edit",
                               workphone = "edit", fax = "edit", email = "edit", email2 = "edit", email3 = "edit",
                               homepage = "edit", address2 = "edit", phone2 = "edit",
                               notes = "edit"))
    app.session.logout()