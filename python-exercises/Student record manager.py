'''
numbers = [1, 2, 3, 4, 5]
numbers.insert(5, 6)
numbers.pop(2)
print(numbers)
students = [{"name": "Omotolani", "age": "19", "department": "Computer Science", "level": "400"},
            {"name": "Teniola", "age": "17", "department": "Statistics", "level": "200" }
            {'name': "David", "age": "16", "department": "Law", "level": "100"}]
print(students)
'''
from random import choice

students_record = []
while True:
    student = {}
    student["name"] = input("Enter student's full name: ")
    student["matric.no/phone.no"] = input("Enter student's matric/phone.no: ")
    student["age"] = input("Enter student's age: ")
    student["department"] = input("Enter student's department: ")
    student["level"] = input("Enter student's current level: ")
    student["parent's/guardian's contact info"] = input("Enter parent's/guardian's contact: ")

    students_record.append(student)
    choice = input("Would you like to add another student's details? (YES/NO): ").upper()
    if choice == "NO":
        break
print(students_record)