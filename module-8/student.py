import json

with open("student.json", "r") as student_file:
    student_list = json.load(student_file)

def print_students(student_list):
    for student in student_list:
        print("{}, {} : ID = {} , Email = {}".format(
            student["L_Name"],
            student["F_Name"],
            student["Student_ID"],
            student["Email"]
        ))

print("\n-- ORIGINAL STUDENT LIST --")
print_students(student_list)

student_list.append({
    "F_Name": "Arrington",
    "L_Name": "Capehart",
    "Student_ID": 99999,
    "Email": "acapehart@my365.bellevue.edu"
})

print("\n-- UPDATED STUDENT LIST --")
print_students(student_list)

with open("student.json", "w") as student_file:
    json.dump(student_list, student_file, indent=4)

print("\n-- STUDENT.JSON FILE UPDATED --")