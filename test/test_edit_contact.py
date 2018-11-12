# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact(Contact(name="maria", middlename="ivanovna", surname="sidorova", nick="newnick", title="newtitle"))
    app.session.logout()

