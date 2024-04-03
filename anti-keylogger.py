import random

def anti_keylogger(input_string):
    return ''.join(random.sample(input_string, len(input_string)))

input_string = "confidentialpassword123"
protected_string = anti_keylogger(input_string)
print(protected_string)
