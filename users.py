current_users = ['john', 'david', 'rotex', 'gelen', 'mike']
new_users = ['John', 'may', 'David', 'wat']

for new_user in new_users:
   if new_user.lower() in current_users:
       print('Sorry, the name "'+ new_user + '" is taken. Please change.')
   else:
       print('This name "' + new_user + '" is available.')