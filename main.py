class ContactList(list):

    def search(self, search_string):
        matches = []
        for contact in self:
            if search_string in contact.name:
                matches.append(search_string)
        return matches

    def longest_name(self):
        longest = ""
        for contact in self:
            if len(contact.name) > len(longest):
                longest = contact.name
        if longest:
            return longest


class Contact:

    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.add_contacts()

    def add_contacts(self):
        self.__class__.all_contacts.append(self)

    @classmethod
    def reset_contacts(cls):
        del cls.all_contacts[:]


class Supplier(Contact):

    all_orders = {}

    def order(self, order):
        if self.email in self.all_orders.keys():
            self.all_orders[self.email].append(order)
        else:
            self.all_orders.update({self.email: [order]})
