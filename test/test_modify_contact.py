# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
import random


def test_modify_contact_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(name="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact1 = Contact(name="maria")
    contact1.id = contact.id
    app.contact.modify_contact_by_id(contact.id, contact1)
    new_contacts = db.get_contact_list()
    contact.name = contact1.name
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


#def test_modify_contact_name(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(name="test"))
    #contact = Contact(name="maria")
    #old_contacts = app.contact.get_contact_list()
    #index = randrange(len(old_contacts))
    #contact.id = old_contacts[index].id
    #contact.surname = old_contacts[index].surname
    #app.contact.modify_contact_by_index(index, contact)
    #assert len(old_contacts) == app.contact.count()
    #old_contacts[index] = contact
    #new_contacts = app.contact.get_contact_list()
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


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

