def validate_atm_pin_code(pin):
    valid=True
    if len(pin)==4 or len(pin)==6: 
        for i in pin:
            if i.isalpha():
                valid=False
                break
    else:
        valid=False
    return valid

pin = input()
print("Valid PIN Code" if validate_atm_pin_code(pin) else "Invalid PIN Code")
