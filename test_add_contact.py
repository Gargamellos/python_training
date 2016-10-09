# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("http://localhost:8080/addressbook/edit.php")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_contact_page(self, wd):
        wd.find_element_by_link_text("nowy wpis").click()

    def create_contact(self, wd, name, middlename, surname, nick, title, company, address, homephone, mobilephone,
                       workphone, fax, email, email2, email3, homepage, address2, phone2, notes):
        # fill contact firm
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").send_keys(middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(surname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nick)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").send_keys(homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(mobilephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").send_keys(workphone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").send_keys(fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").send_keys(email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").send_keys(email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(homepage)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(notes)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Wyloguj się").click()

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username = "admin", password = "secret")
        self.open_contact_page(wd)
        self.create_contact(wd, name = "asd", middlename = "\\9", surname = "asda", nick = "adsa", title = "swed",
                            company = "aswq", address = "asa", homephone = "\\9", mobilephone = "45654",
                            workphone = "\\9", fax = "\\9", email = "asdas", email2 = "\\9", email3 = "\\9",
                            homepage = "sdfsd", address2 = "gfd", phone2 = "gfd",
                            notes = "gfd")
        self.return_to_home_page(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username = "admin", password = "secret")
        self.open_contact_page(wd)
        self.create_contact(wd, name = "", middlename = "", surname = "", nick = "", title = "",
                            company = "", address = "", homephone = "", mobilephone = "",
                            workphone = "", fax = "", email = "", email2 = "", email3 = "",
                            homepage = "", address2 = "", phone2 = "",
                            notes = "")
        self.return_to_home_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

