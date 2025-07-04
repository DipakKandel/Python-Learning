user_age = int(input("Enter your age: "))
if user_age<13:
  print("You can watch cartoon movies")
elif 13 <= user_age < 18:
  print("You can watch anime and drama")
else:
  print("You can watch any movie")
is_student = input("Are you a student? (yes/no): ").lower()

if is_student == "yes" or is_student =="y" :
    print("You get a student discount!")
