import re
from random import randrange


def test_contact_all(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.surname == contact_from_edit_page.surname
    assert contact_from_home_page.name == contact_from_edit_page.name
    assert clear_probel(contact_from_home_page.address) == clear_probel(contact_from_edit_page.address)
    assert clear_probel(contact_from_home_page.all_emails_from_home_page) == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def clear_probel(s):
    return re.sub("[ ]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_probel(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))

