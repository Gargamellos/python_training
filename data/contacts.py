
from model.contact import Contact
import random
import string


constant = [
    Contact(lastname="lastname1", firstname="firstname1", middlename="middlename1", nick="nick1", title="title1",
            company="company1", address="address1", homephone="homephone1", mobilephone="mobilephone1",
            workphone="workphone1", fax="fax1", email="email1", email2="email1", email3="email1", homepage="homepage1",
            address2="address1", phone2="phone1", notes="notes1"),
    Contact(lastname="lastname2", firstname="firstname2", middlename="middlename2", nick="nick2", title="title2",
            company="company2", address="address2", homephone="homephone2", mobilephone="mobilephone2",
            workphone="workphone2", fax="fax2", email="email2", email2="email2", email3="email2", homepage="homepage2",
            address2="address2", phone2="phone2", notes="notes2"),
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(lastname="", firstname="", middlename="", nick="", title="", company="", address="", homephone="",
                    mobilephone="", workphone="", fax="", email="", email2="", email3="", homepage="", address2="",
                    phone2="", notes="")] + [
            Contact(lastname=random_string("lastname", 10), firstname=random_string("firstname", 10),
                    middlename=random_string("middlename", 10), nick=random_string("nick", 10),
                    title=random_string("title", 10), company=random_string("company", 10),
                    address=random_string("address", 10), homephone=random_string("home", 10),
                    mobilephone=random_string("mobile", 10), workphone=random_string("work", 10),
                    fax=random_string("fax", 10), email=random_string("email", 10), email2=random_string("email2", 10),
                    email3=random_string("email3", 10), homepage=random_string("homepage",10),
                    address2=random_string("address2", 10), phone2=random_string("phone2", 10),
                    notes=random_string("notes", 10))
            for i in range(5)
]

