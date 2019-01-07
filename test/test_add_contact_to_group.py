# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture


orm_db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    if len(orm_db.get_contact_list()) == 0:
        app.contact.create(Contact(name="test"))
    if len(orm_db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    contacts = orm_db.get_contact_list()
    groups = orm_db.get_group_list()
    contact = random.choice(contacts)
    group = random.choice(groups)
    if not contact in orm_db.get_contacts_in_group(group):
        app.contact.add_contact_to_group(contact, group)
    else:
        print("Контакт уже в группе")
