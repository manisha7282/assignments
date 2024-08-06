import re
def valid_or_not(s):
    if len(s)<20:
        return False
    if not re.search(r"\d",s):
        return False
    if not re.search(r"[!@#$%^&*()..?.{}|<>]",s):
        return False
    
    return True
user=input("enter a string:")
if valid_or_not(user):
    print("Is correct")
else:
    print("not Correct")    

