# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_name(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    app.contact.modify_contact(Contact(name="maria"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_middlename(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    app.contact.modify_contact(Contact(middlename="ivanovna"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

