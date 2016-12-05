
from model.contact import Contact
import re


def test_verification_on_home_page(app,db):
    contact_from_home_page = sorted(app.contact.get_contact_list(),key=Contact.id_or_max)
    contact_from_db = sorted(db.get_contact_list(),key=Contact.id_or_max)
    assert len(contact_from_home_page) == len(contact_from_db)
    for i in range (len(contact_from_db)):
        db_contact = contact_from_db[i]
        ui_contact = (sorted(contact_from_home_page, key=Contact.id_or_max))[i]
        assert ui_contact.firstname == db_contact.firstname
        assert ui_contact.lastname == db_contact.lastname
        assert ui_contact.address == db_contact.address
        assert ui_contact.all_mails_from_home_page == merge_mails_like_on_home_page(db_contact)
        assert ui_contact.all_phones_from_home_page == merge_phones_like_on_home_page(db_contact)

def clear(s):
    return re.sub("[() -]", "", s)
def merge_mails_like_on_home_page(db):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [db.email, db.email2, db.email3]))))

def merge_phones_like_on_home_page(db):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [db.homephone, db.mobilephone, db.workphone, db.phone2]))))

#def merge_mails_like_on_home_page(contact):
#    return "\n".join(filter(lambda x: x != "",
#                            map(lambda x: clear(x),
#                                filter(lambda x: x is not None,
#                                       [contact.email, contact.email2, contact.email3]))))

#def merge_phones_like_on_home_page(contact):
#    return "\n".join(filter(lambda x: x != "",
#                            map(lambda x: clear(x),
#                                filter(lambda x: x is not None,
#                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.phone2]))))



