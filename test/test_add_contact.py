# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name ="Jan", middlename ="Marian", surname ="Kowalski", nick ="Kowal", title ="abcd",
                               company = "aaa", address = "aaa", homephone = "111", mobilephone = "2222",
                               workphone = "333", fax = "444", email = "bbb", email2 = "ccc", email3 = "ddd",
                               homepage = "eee", address2 = "fff", phone2 = "ggg",
                               notes = "zzz")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(name ="", middlename ="", surname ="", nick ="", title ="",
#                               company = "", address = "", homephone = "", mobilephone = "",
#                               workphone = "", fax = "", email = "", email2 = "", email3 = "",
#                               homepage = "", address2 = "", phone2 = "",
#                               notes = "")
#    app.contact.create(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

