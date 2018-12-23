# -*- coding: utf-8 -*-
from typing import List
from random import randrange
from model.contact import Contact
import random


def test_delete_contact_by_index(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(name="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


#def test_delete_contact_by_index(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(name="test"))
    #old_contacts = app.contact.get_contact_list()
    #index = randrange(len(old_contacts))
    #app.contact.delete_contact_by_index(index)
    #assert len(old_contacts) - 1 == app.contact.count()
    #new_contacts = app.contact.get_contact_list()
    #old_contacts[index:index + 1] = []
    #assert old_contacts == new_contacts






