def greet(name):
    print(f"Hello, {name}!")


greet("dipak")

def add_numbers(a, b):
    return int(a) + int(b)

total = add_numbers(input("Enter a Number : "),input("Enter another number: "))
print("Total is:", total)

def is_even(number):
    if number % 2 == 0:
        return "Number is Even"
    else:
        return "Number is odd"

print(is_even(int(input("Enter number to check if number is even: "))))  

# Asks the user how many students are in a class For each student:
# Asks for name
# Asks for score (0–100)

# Then:
# Prints a report with name, score, and letter grade (A–F)
# Shows the class average
# Shows the student with the highest score

number_of_students = int(input("Enter number of students: "))
grade_score = {}
def get_letter_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"

for i in range(number_of_students):
  student_name = input("Enter Student Name: ")
  student_score = int(input("Enter Marks: "))
  student_grade = get_letter_grade(student_score)
  grade_score[student_name] = {
        "score": student_score,
        "grade": student_grade
    }
                 
print("Student Report")
for name, scores in sorted(grade_score.items()):
    print(f"{name}: Score = {scores['score']}, Grade = {scores['grade']}")




  


