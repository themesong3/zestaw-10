class new_contact():

    def __init__(self, name, mail, phone):
        self.name = name
        self.mail = mail
        self.phone = phone

    def __str__(self):
        return f"{self.name}   {self.mail}   {self.phone}"