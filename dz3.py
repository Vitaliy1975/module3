import re

def normalize_phone(phone_number):
    pattern=r"[+\d]+"
    digits=re.findall(pattern,phone_number)
    digits_joined="".join(digits)
    if len(digits_joined)==10:
        digits_joined="+38"+digits_joined
    elif len(digits_joined)==12:
        digits_joined="+"+digits_joined
    return digits_joined

