import re


# name validation

def NameValidation(Name):
    ptr = "^[a-zA-Z\ ]+$"
    if re.match(ptr,Name):
        return True
    else:
        return False

def UserNameValidation(Username):
    ptr = "^[a-zA-Z\ ]+@[0-9]+$"
    if re.match(ptr,Username):
        return True
    else:
        return False

def EmailValidation(Email):
    ptr = "^[a-z0-9\_\.]+@[a-z]+\.+[com|in|org]+$"
    if re.match(ptr,Email):
        return True
    else:
        return False

def ContactValidation(Contact):
    ptr = "^[6-9]+[0-9]{9}"
    if re.match(ptr,Contact):
        return True
    else:
        return False

def Passwordvalidation(Password,Confirm_Password):
    if Password == Confirm_Password:
        if len(Password) >= 8:
            return True
        else:
            return False
def addharValidation(no):
     regex = ("^[2-9]{1}[0-9]{3}\\" +
             "s[0-9]{4}\\s[0-9]{4}$")
     if re.match(regex,no):
         return True
     else:
         return False