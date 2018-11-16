# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(name="natali", middlename="olegovna", surname="scherbakova", nick="nick", title="title"))


