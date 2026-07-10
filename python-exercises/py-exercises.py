'''
#Return Statements
def calculate_area(length, width):
  return length*width
length = float(input("Enter length: "))
width = float(input("Enter width: "))
result = calculate_area(length, width)
print(result)
'''

#Conditional Statements (if, nested if) & Loops
age = input("Enter your age: ")
has_validID = False
if age >= "18":
    if has_validID:
        print("Has valid ID.")
    else:
        print("Invalid ID.")
else:
    print("Ineligible to vote.")
'''
#Functions
def message():
    print("Python is fun!")
message()
'''


