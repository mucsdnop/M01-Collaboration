# John Martin III
# Dean's List and Honor Roll checker
# This application will ask for a student's last and first name followed by their GPA and check whether they're on either the Dean's List or Honor Roll

last_name = input("Enter the student's last name: ")
while last_name != "ZZZ":
    first_name = input("Enter the student's first name: ")
    gpa = float(input("Enter the student's GPA: "))
    if gpa >= 3.5:
        print("This student has made the Dean's list!")
    elif gpa >= 3.25:
        print("This student has made the Honor Roll!")
    last_name = input("Enter the student's last name: ")