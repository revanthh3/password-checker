import string
import getpass
print("Please enter a password:")
passwd=getpass.getpass()
spz=string.punctuation
print("Please re-enter your password")
passwd1=getpass.getpass()
def condition(check):
    if len(check)<8:
        return("Password complexity is not meet")
    if not any(char.isdigit() for char in check):
        return("Password complexity is not meet")
    if not any(char.isalpha() for char in check):
        return("Password complexity is not meet")
    if not any(char.isupper() for char in check):
        return("Password complexity is not meet")
    if not any(char.islower() for char in check):
        return("Password complexity is not meet")
    if not any(char in spz for char in check):
        return("Password complexity is not meet")
    else:
        return("Password is successfully created")

if passwd == passwd1:
    print(condition(passwd))
else:
    print("the match is not matching")


