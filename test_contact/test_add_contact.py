# -*- coding: utf-8 -*-
import pytest

from fixture_contact.application1 import Application1
from model_contact.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application1()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.create_contact(Contact(name = "asd", middlename = "\\9", surname = "asda", nick = "adsa", title = "swed",
                        company = "aswq", address = "asa", homephone = "\\9", mobilephone = "45654",
                         workphone = "\\9", fax = "\\9", email = "asdas", email2 = "\\9", email3 = "\\9",
                        homepage = "sdfsd", address2 = "gfd", phone2 = "gfd",
                        notes = "gfd"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.create_contact(Contact(name = "", middlename = "", surname = "", nick = "", title = "",
                        company = "", address = "", homephone = "", mobilephone = "",
                        workphone = "", fax = "", email = "", email2 = "", email3 = "",
                        homepage = "", address2 = "", phone2 = "",
                        notes = ""))
    app.session.logout()

