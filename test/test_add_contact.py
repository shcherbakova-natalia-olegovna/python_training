# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
#from data.contacts import testdata


#@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])

def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

#def test_add_contact(app, json_contacts):
    #contact = json_contacts
    #old_contacts = app.contact.get_contact_list()
    #app.contact.create(contact)
    #assert len(old_contacts) + 1 == app.contact.count()
    #new_contacts = app.contact.get_contact_list()
    #old_contacts.append(contact)
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


