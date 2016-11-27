
from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(fisrtname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = random.choice(old_contacts)
    id_group = app.group.select_id_group()
    app.contact.add_contact_to_group(contact.id, id_group)
    new_contacts = app.contact.get_contacts_list_in_group(id_group)
    contact_list_orm = orm.get_contacts_in_group(Group(id=id_group))
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(contact_list_orm, key=Contact.id_or_max)
