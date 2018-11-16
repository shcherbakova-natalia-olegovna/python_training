# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_name(app):
    app.contact.modify_contact(Contact(name="maria"))


def test_modify_contact_middlename(app):
    app.contact.modify_contact(Contact(middlename="ivanovna"))

