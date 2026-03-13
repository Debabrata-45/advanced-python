class InvalidStudentIDError(Exception):
    pass
class EmptyGradeError(Exception):
    pass
class GradeTypeError(Exception):
    pass
class StudentGradeManager:
    def __init__(self):
        self.records = {}

    def add_or_update_grade(self, student_id, grade):
        if not isinstance(student_id, int) or student_id <= 0:
            raise InvalidStudentIDError("Student ID must be a positive integer.")

        if grade == "" or grade is None:
            raise EmptyGradeError("Grade cannot be empty.")

        if not isinstance(grade, (int, float)):
            raise GradeTypeError("Grade must be a number.")

        self.records[student_id] = grade
        print(f"Grade saved successfully for Student ID {student_id}.")

    def delete_grade(self, student_id):
        if not isinstance(student_id, int) or student_id <= 0:
            raise InvalidStudentIDError("Invalid student ID.")

        if student_id not in self.records:
            raise InvalidStudentIDError("Student ID not found.")

        del self.records[student_id]
        print(f"Grade deleted successfully for Student ID {student_id}.")

    def view_all(self):
        if not self.records:
            print("No student records found.")
        else:
            for sid, grade in self.records.items():
                print(f"Student ID: {sid}, Grade: {grade}")


def main():
    manager = StudentGradeManager()

    while True:
        print("\n--- Student Grade Management System ---")
        print("1. Add/Update Grade")
        print("2. Delete Grade")
        print("3. View All Grades")
        print("4. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                student_id = int(input("Enter Student ID: "))
                grade_input = input("Enter Grade: ")

                if grade_input.strip() == "":
                    grade = ""
                else:
                    grade = float(grade_input)

                manager.add_or_update_grade(student_id, grade)

            elif choice == "2":
                student_id = int(input("Enter Student ID to delete: "))
                manager.delete_grade(student_id)

            elif choice == "3":
                manager.view_all()

            elif choice == "4":
                print("Exiting program.")
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Input error: Please enter proper numeric values.")
        except (InvalidStudentIDError, EmptyGradeError, GradeTypeError) as e:
            print("Error:", e)
        except Exception as e:
            print("Unexpected error:", e)


if __name__ == "__main__":
    main()