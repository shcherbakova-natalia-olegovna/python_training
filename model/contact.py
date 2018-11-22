from sys import maxsize


class Contact:
    def __init__(self, name=None, middlename=None, surname=None, nick=None, title=None, id=None):
        self.name = name
        self.middlename = middlename
        self.surname = surname
        self.nick = nick
        self.title = title
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
