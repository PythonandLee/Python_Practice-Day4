# Use 'for...in' to run every elements in the list.
# Use 'if' to create different situations.

# Use 'if-else' to create 2 conditions, if the elements 
# belong to different situations.

# Put 'print' out of the loop to operate it anyway.
food_list = ['pizza', 'soup', 'curry']

for food in food_list:
    if food == 'soup':
        print("Sorry, soup is sold out!")
    else:
        print("Buy some " + food + "!")

print("\nAll food on the list are checked!")