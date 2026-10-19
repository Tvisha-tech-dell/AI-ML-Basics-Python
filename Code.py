
# Student Grade Calculator
# A beginner-friendly Python mini project

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def main():
    print("=" * 40)
    print("       STUDENT GRADE CALCULATOR")
    print("=" * 40)

    name = input("Enter student name: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("Enter student name: ").strip()

    try:
        number_of_subjects = int(
            input("Enter number of subjects: ")
        )

        if number_of_subjects <= 0:
            print("Number of subjects must be positive.")
            return

        subjects = []
        marks_list = []

        for i in range(number_of_subjects):
            subject = input(
                f"Enter name of subject {i + 1}: "
            ).strip()

            while not subject:
                print("Subject name cannot be empty.")
                subject = input(
                    f"Enter name of subject {i + 1}: "
                ).strip()

            while True:
                try:
                    marks = float(
                        input(f"Enter marks in {subject} (0-100): ")
                    )

                    if 0 <= marks <= 100:
                        break

                    print("Marks must be between 0 and 100.")

                except ValueError:
                    print("Please enter a valid number.")

            subjects.append(subject)
            marks_list.append(marks)

        total = sum(marks_list)
        maximum_marks = number_of_subjects * 100
        percentage = (total / maximum_marks) * 100
        grade = calculate_grade(percentage)

        # A student passes only if every subject has 40 or more.
        passed = all(mark >= 40 for mark in marks_list)

        print("\n" + "=" * 40)
        print("           RESULT REPORT")
        print("=" * 40)
        print(f"Student Name : {name}")

        for subject, marks in zip(subjects, marks_list):
            print(f"{subject}: {marks:g}/100")

        print("-" * 40)
        print(f"Total Marks  : {total:g}/{maximum_marks}")
        print(f"Percentage   : {percentage:.2f}%")
        print(f"Overall Grade: {grade}")
        print(f"Result       : {'PASS' if passed else 'FAIL'}")
        print("=" * 40)


if __name__ == "__main__":
    main()
