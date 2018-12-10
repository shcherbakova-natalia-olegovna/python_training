from model.contact import Contact
import random
import string


constant = [
    Contact(name="name1", middlename="middlename1", surname="surname1", nick="nick1", title="title1"),
    Contact(name="name2", middlename="middlename2", surname="surname2", nick="nick2", title="title2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(name="", middlename="", surname="", nick="", title="")] + [
    Contact(name=random_string("name", 10), middlename=random_string("middlename", 10),
          surname=random_string("surname", 10), nick=random_string("nick", 10), title=random_string("title", 10))
    for i in range(5)
    ]