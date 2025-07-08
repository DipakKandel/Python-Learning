# Practicing try catch
while True:
    try:
        first_value = float(input("Enter First Number: "))
        break
    except ValueError:
        print("❌ Please enter a valid number.")

while True:
   try:
      second_value = float(input("Enter Second Number: "))
      break
   except ValueError:
      print("Please enter a valid number: ")

try:
  first_value = first_value
  second_value = second_value
  result = first_value/second_value
  print (f"Result is:{result:.3f}")
except ValueError:
  print("Please enter numerical value")
except ZeroDivisionError:
  print("Numbers can't be divided by zero")
finally:
  print("Division work is complete")


def set_age(age):
    if age <= 0:
        raise ValueError("Age cannot be negative!")
    return age

while True:
  try:
      age = int(input("Enter your age: "))
      set_age(age)
      print("Age accepted!")
      break
  except ValueError as e:
      print(f"❌ Error: {e}")

while True:
  try:
    total_employees = int(input ("Enter total number of students: "))
    break
  except ValueError:
    print("Please input a valid number: ")

employees = {}
for each in range (total_employees):
  name = input("Enter name:")
  while True:
    try:
      salary = float(input("Enter salary: "))
      assert salary>0, "Salary must be a positive number!"
      break
    except ValueError:
      print("Please enter a valid salary")
    except AssertionError as e:
      print(e)

  employees[name]=salary
print("\n📊 Employee Salary Report")
for emp, sal in employees.items():
    print(f"{emp}: ${sal:.2f}")

print(f"Average salary is :  {sum(employees.values())/total_employees:.3f}")
print(f"Highest salary is : { max(employees.values())}")
print(f"Lowest salary is : {min(employees.values())}")