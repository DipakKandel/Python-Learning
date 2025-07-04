todo_list = []
todo_list.append("Pack the Items")

for each in enumerate (todo_list,1):
  print(f"{each}")
word = "Python"
for letter in word:
    print(letter)

# Asks the user to enter 5 favorite fruits (one by one)

# Stores them in a list

# Prints the final list in reverse order (last fruit first)
favourites = []
while True:
  favourite_fruit=input("Enter your favourite food else type don : ").lower()
  if(favourite_fruit=='done'):
    break
  favourites.append(favourite_fruit)

print("\nYour favourite fruits in reverse order:")
for fruit in reversed(favourites):
   print(fruit)

for i, fruit in enumerate(reversed(favourites), 1):
    print(f"{i}. {fruit}")

# Asks the user to enter 5 numbers (one at a time)
# Stores them in a list
# Prints:
# The numbers
# The average of the numbers
# The highest number
# The lowest number
values = []
# Loop 5 times (0 to 4)
for i in range(5):
    input_number = int(input("Enter a number and press enter: "))
    values.append(input_number)

# Loop through the list
for item in values:
    print(item)

total = 0
for item in values:
    total += item

average = total / len(values)
print(f"Average is: {average}")

print(f"Highest value is :{max(values)} ")
print(f"Smallest value is :{min(values)} ")