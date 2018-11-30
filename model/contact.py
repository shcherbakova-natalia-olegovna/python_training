from sys import maxsize


class Contact:
    def __init__(self, name=None, middlename=None, surname=None, address=None, email=None, email1=None, email2=None, email3=None, all_emails_from_home_page=None, nick=None, title=None, all_phones_from_home_page=None, homephone=None, mobilephone=None, workphone=None, secondaryphone=None, id=None):
        self.name = name
        self.middlename = middlename
        self.surname = surname
        self.address = address
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page = all_emails_from_home_page
        self.nick = nick
        self.title = title
        self.all_phones_from_home_page = all_phones_from_home_page
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.surname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name and self.surname == other.surname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
