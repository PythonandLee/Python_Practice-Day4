# Make a list, and use 'if' to determine T/F.
# If 'if' is True, continue 'for' loop.
# Use '\' to make new line in case code is too long.
names = ['admin', 'tim', 'roy', 'john']

if names:
    for name in names:
        if name == 'admin':
            print("Hello " + name.title() +\
             ", would you like to see a status report?")
        else: 
            print("Hello " + name.title() +\
             ", thank you for logging in again.")
else:
    print("We need to find some users!")        