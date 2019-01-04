# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random


def test_del_contact_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(name="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.del_contact_from_group()