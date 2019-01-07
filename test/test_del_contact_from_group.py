# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture


orm_db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_del_contact_from_group(app, db):
    if len(orm_db.get_contact_list()) == 0:
        app.contact.create(Contact(name="test"))
    if len(orm_db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = orm_db.get_group_list()
    group = random.choice(groups)
    if len(orm_db.get_contacts_in_group(group)) > 0:
        contacts = orm_db.get_contacts_in_group(group)
        contact = random.choice(contacts)
        app.contact.del_contact_from_group(contact, group)
    else:
        print("В выбранной гуппе нет контактов")
        contacts1 = orm_db.get_contact_list()
        contact1 = random.choice(contacts1)
        app.contact.add_contact_to_group(contact1, group)
        print("Случайный контакт добавлен в группу")
        app.contact.del_contact_from_group(contact1, group)
        print("Случайный контакт удален из группы")
