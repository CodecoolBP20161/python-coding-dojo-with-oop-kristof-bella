
class Contact:

    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.add_contacts()

    def add_contacts(self):
        self.all_contacts.append(self)


    @classmethod
    def reset_contacts(cls):

        del cls.all_contacts[:]


class Supplier(Contact):
    pass