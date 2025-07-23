# print("Hello World")
# print("how are you")
# name = input("Enter your name: ")
# print (f"Hi {name}, so you are here already")

# # This program is to say hello to the user

# print("What is your age?") 
# myage = input()
# print(myage)

students = ["John", "Jane", "Jim", "Jill","Jack","Jipp", "Jop", "Jopper", "Jopperino", "Jopperinoino"]
# print(students)

# print(students[0:-1:2]) #skip 2 elements

# students[3] = "Dipak"
# # print(students[:4 ])

# del students[3] #delete the element at index 3
print(students)

students.remove("Jopperinoino") #remove the element "Jopperinoino"
print(students)

students.pop() #remove the last element
print(students)
# students = students *5
# students.clear() #clear the list
print(students)

girls = ["Liva", "Liza", "Lily", "Lora", "Lora"]

all_students = students + girls
print(all_students)


myname = list("dipak")
print(myname)


myname.reverse()
print(myname)

myname.sort()
print(myname)

print("d" not  in myname)
