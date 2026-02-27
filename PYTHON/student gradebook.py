students = []

def calculate_grade(avg):
    if avg >= 90: return "A"
    elif avg >= 75: return "B"
    elif avg >= 60: return "C"
    elif avg >= 40: return "D"
    else: return "Fail"

def add_student():
    name = input("Name: ")
    n = int(input("Number of subjects: "))
    
    subjects = []
    marks = []
    
    for i in range(n):
        sub = input(f"Subject {i+1} name: ")
        mark = float(input(f"Marks in {sub}: "))
        subjects.append(sub)
        marks.append(mark)
    
    avg = sum(marks) / len(marks)
    students.append([name, subjects, marks, round(avg,2), calculate_grade(avg)])
    print("Student added!\n")

def display_students():
    for s in students:
        print("\nName:", s[0])
        for sub, mark in zip(s[1], s[2]):
            print(f"{sub}: {mark}")
        print("Average:", s[3])
        print("Grade:", s[4])

while True:
    choice = input("\n1.Add  2.Display  3.Exit : ")
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        break