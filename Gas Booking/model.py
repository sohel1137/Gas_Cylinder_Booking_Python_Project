

class customer:
    def __init__(self,Name,Email,Address,Contact,Password,Gas_Type):
        self.Name = Name
        self.Email = Email
        self.Address = Address
        self.Gas_Type = Gas_Type
        self.Contact = Contact
        self.Password = Password

    def __repr__(self):
        return f'customer[{self.Name}{self.Email}{self.Address}{self.Gas_Type}{self.Contact}{self.Password}]'
    

class Admin:
    def __init__(self,Email,Password):
        #self.Name = Name
        self.Email = Email
        #self.Contact = Contact
        self.Password = Password

    def __repr__(self):
        return f'Admin[{self.Email}{self.Password}]'