from model.contact import Contact
import re



class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("nowy wpis").click()

    def open_stronaglowna_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("strona główna").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nick)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_stronaglowna_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_stronaglowna_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_stronaglowna_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_stronaglowna_page()
        self.contact_cache = None

    def add_contact_to_group(self, id, id_group):
        wd = self.app.wd
        self.open_stronaglowna_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath('//select[@name="to_group"]/option[@value="%s"]' % id_group).click()
        wd.find_element_by_name("add").click()
        self.open_stronaglowna_page()
        self.contact_cache = None

    def del_contact_from_group(self, id, id_group):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath('//select[@name="group"]/option[@value="%s"]' % id_group).click()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@name='remove']").click()
        self.open_stronaglowna_page()
        self.contact_cache = None

#        wd = self.app.wd
#        self.open_stronaglowna_page()
#        wd.find_element_by_xpath("//form[@id='right']/select//option[3]").click()
#        wd.find_element_by_name("selected[]").click()
#        wd.find_element_by_name("remove").click()
#        wd.find_element_by_link_text("group page \"name\"").click()
#        wd.find_element_by_xpath("//form[@id='right']/select//option[2]").click()
#        self.open_stronaglowna_page()
#        self.contact_cache = None

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_stronaglowna_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit edit
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # edit contact
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nick)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").send_keys(contact.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobilephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").send_keys(contact.workphone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.return_to_home_page()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_stronaglowna_page()
        self.select_contact_by_index(index)
        # open modification form
        self.open_contact_to_edit_by_index(index)
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.open_stronaglowna_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_stronaglowna_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                address = cells[3].text
                all_mails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id,
                                                  address=address, all_mails_from_home_page=all_mails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contacts_list_in_group(self, id_group):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_stronaglowna_page()
            wd.find_element_by_xpath('//select[@name="group"]/option[@value="%s"]' % id_group).click()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                address = cells[3].text
                all_mails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id,
                                                  address=address, all_mails_from_home_page=all_mails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_stronaglowna_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_stronaglowna_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                       email=email, email2=email2, email3=email3,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, phone2=phone2)

    def get_contact_from_view_page(self,index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, phone2=phone2)






