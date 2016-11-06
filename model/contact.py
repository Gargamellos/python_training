from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nick=None, title=None, company=None,
                 address=None, homephone=None, mobilephone=None, workphone=None, fax=None, email=None, email2=None,
                 email3=None, homepage=None, address2=None, phone2=None, notes=None, all_phones_from_home_page=None,
                 all_mails_from_home_page=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
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
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_mails_from_home_page = all_mails_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % (self.id, self.lastname, self.firstname,
                             self.middlename, self.nick, self.title, self.company, self.address,
                             self.homephone, self.mobilephone, self.workphone, self.fax, self.email, self.email2,
                             self.email3, self.homepage, self.address2, self.phone2, self.notes)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname\
               and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
