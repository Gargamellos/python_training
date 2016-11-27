
from model.contact import Contact
import re


def test_verification_on_home_page(app,db):
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db_list = db.get_contact_list()
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_db_list, key=Contact.id_or_max)
    print(sorted(contact_from_home_page, key=Contact.id_or_max))
    print(sorted(contact_from_db_list, key=Contact.id_or_max))
    assert [x for x in (sorted(contact_from_home_page, key=Contact.id_or_max), sorted(contact_from_db_list, key=Contact.id_or_max))]

#def test_verification_on_home_page(app):
#    old_contacts = app.contact.get_contact_list()
#    index = randrange(len(old_contacts))
#    contact_from_home_page = app.contact.get_contact_list()[index]
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
#    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
#    assert contact_from_home_page.address == contact_from_edit_page.address
#    assert contact_from_home_page.all_mails_from_home_page == merge_mails_like_on_home_page(contact_from_edit_page)
#    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_mails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.phone2]))))