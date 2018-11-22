# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    contact = Contact(name="maria")
    old_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[0].id
    contact.surname = old_contacts[0].surname
    app.contact.modify_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_middlename(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(name="test"))
    #contact = Contact(middlename="ivanovna")
    #old_contacts = app.contact.get_contact_list()
    #contact.id = old_contacts[0].id
    #contact.surname = old_contacts[0].surname
    #contact.name = old_contacts[0].name
    #app.contact.modify_contact(contact)
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)
    #old_contacts[0] = contact
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

