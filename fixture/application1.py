from selenium.webdriver.chrome.webdriver import WebDriver

from fixture.contact import ContactHelper
from fixture.session import SessionHelper


class Application1:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/edit.php")


    def destroy(self):
        self.wd.quit()