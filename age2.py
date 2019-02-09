# Use 'if-elif-else' to make mutiple conditions.
# Be aware of using 'else', it is a powerful command.
# When 'else' is operated, it means the condition is not in 'if-elif', 
# otherwise will be include in 'else' condition.
# Also if conditions are not throughly considered, it may bring 
# unexpected results or errors.  

age = 2
if age < 2:
    print("They are babies.")
elif age < 4:
    print("They are toddlers.")
elif age < 13:
    print("They are children.")
elif age < 20:
    print("They are adolescents.")
elif age < 65:
    print("They are adults.")
else:
    print("They are elders.")