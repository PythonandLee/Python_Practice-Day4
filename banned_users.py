# Use command 'if' to determine 'True' or 'False'.
banned_users = ['tim', 'joe', 'andy']
user = 'harry'

# Use 'in' or 'not in' to make conditions.
if user not in banned_users:
    print(user.title() + ', please join our discussion.')