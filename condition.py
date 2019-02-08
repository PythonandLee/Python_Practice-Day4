car = 'tesla'
print("Is car == 'tesla'?")
print(car == 'tesla')
print("Is car == 'ford'?")
print(car == 'ford')

print("\nIs car == 'Tesla'?")
print(car.title() == 'Tesla')
print("\n")

n = 19
if n == 19:
   print(n == 19)
   print("Nice guess, n == 19")
if n > 20:
   print(n > 20)
   print("Wrong guess, n is not larger than 20")  
if n <= 30:
   print(n <= 30)
   print("Nice guess, n <= 30")
   
if n > 5 and n < 30:
   print(n > 5 and n < 30)
   print("Nice guess, n > 5 and n < 30")
if n > 30 or n < 100:
   print(n > 30 or n < 10)
   print("Wrong guess, n is not larger than 30 or smaller than 10.") 