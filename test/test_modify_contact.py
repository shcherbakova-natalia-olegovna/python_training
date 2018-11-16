# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contact(Contact(name="maria"))
    app.session.logout()


def test_modify_contact_middlename(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contact(Contact(middlename="ivanovna"))
    app.session.logout()

