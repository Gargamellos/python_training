

class Contact:
    def __init__(self, name=None, middlename=None, surname=None, nick=None, title=None, company=None, address=None, homephone=None,
                 mobilephone=None, workphone=None, fax=None, email=None, email2=None, email3=None, homepage=None, address2=None,
                 phone2=None, notes=None, id=None):
        self.name = name
        self.middlename = middlename
        self.surname = surname
        self.nick = nick
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name