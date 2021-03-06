from model.contact import Contact
import re
from selenium.webdriver.support.ui import Select
import random


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # add new contact
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_contact_field("firstname", contact.name)
        self.change_contact_field("middlename", contact.middlename)
        self.change_contact_field("lastname", contact.surname)
        self.change_contact_field("nickname", contact.nick)
        self.change_contact_field("title", contact.title)

    def change_contact_field(self, contact_field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(contact_field_name).click()
            wd.find_element_by_name(contact_field_name).clear()
            wd.find_element_by_name(contact_field_name).send_keys(text)

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0, contact)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.app.open_home_page()
        #wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def add_contact_to_group(self, contact, group):
        wd = self.app.wd
        self.app.open_home_page()
        # select contact by id_contact
        wd.find_element_by_css_selector("input[value='%s']" % contact.id).click()
        # open list of groups
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_visible_text(group.name)
        wd.find_element_by_xpath("(//option[@value=%s])[2]" % group.id).click()
        wd.find_element_by_name("add").click()
        wd.find_element_by_xpath("//div[@id='content']/div/i/a").click()
        self.app.return_to_home_page()


    def del_contact_from_group(self, contact, group):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("group").click()
        Select(wd.find_element_by_name("to_group")).select_by_visible_text(group.name)
        wd.find_element_by_xpath("//option[@value=%s]" % group.id).click()
        wd.find_element_by_id("%s" % contact.id).click()
        self.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.return_to_home_page()
        pass

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        #wd.switch_to_alert().accept()
        wd.switch_to.alert.accept()
        #Здесь добавлен лишний переход на страницу со списком групп, без этого перехода не выполняются assert
        #в тесте удаления первого контакта (контакт визуально удаляется, но при этом попадает в новый список контактов)
        #После добавления перехода на страницу со списком групп - ошибка в тесте удаления контакта пропала
        self.open_groups_page()
        self.app.open_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        #wd.switch_to_alert().accept()
        wd.switch_to.alert.accept()
        #Здесь добавлен лишний переход на страницу со списком групп, без этого перехода не выполняются assert
        #в тесте удаления первого контакта (контакт визуально удаляется, но при этом попадает в новый список контактов)
        #После добавления перехода на страницу со списком групп - ошибка в тесте удаления контакта пропала
        self.open_groups_page()
        self.app.open_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.return_to_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                cells = element.find_elements_by_tag_name("td")
                last_name = cells[1].text
                first_name = cells[2].text
                address = cells[3].text
                all_emails_from_home_page = cells[4].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(name=first_name, surname=last_name, address=address,
                                                  all_emails_from_home_page=all_emails_from_home_page, id=id, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/groups.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(name=firstname, surname=lastname, address=address, email=email, email2=email2, email3=email3, id=id,
                       homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone)






