import csv
import os

# CSV Files
student_file = "studentinfo.csv"
account_file = "accountinfo.csv"

# Create files if they don't exist
if not os.path.exists(student_file):
    with open(student_file, "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Student Number", "Student Name", "Grade1", "Grade2", "Grade3"])

if not os.path.exists(account_file):
    with open(account_file, "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Username", "Password", "Role"])

# Create account
def create_account():
    username = input("Username: ")
    password = input("Password: ")
    role = ""
    while role not in ["teacher", "student"]:
        role = input("Role (teacher/student): ").lower()
    with open(account_file, "a", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([username, password, role])
    print(f"Account created successfully as {role}!\n")

# Login check
def login_check(expected_role):
    inusername = input("Username: ")
    inpassword = input("Password: ")
    with open(account_file, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            dbusername, dbpassword, role = row
            if inusername == dbusername and inpassword == dbpassword:
                if role != expected_role:
                    print(f"This account cannot log in as {expected_role}!\n")
                    return False
                print("Login successful!\n")
                return True
    print("Wrong username or password!\n")
    return False

# Add Grades
def grade_write():
    snumber = input("Student number: ")
    sname = input("Student name: ")
    try:
        grade1 = float(input("Grade 1: "))
        grade2 = float(input("Grade 2: "))
        grade3 = float(input("Grade 3: "))
    except ValueError:
        print("Invalid grade entered! Please enter a number.")
        return
    with open(student_file, "a", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([snumber, sname, grade1, grade2, grade3])
    print(f"{sname} added correctly!\n")

# Read Grades
def grade_read():
    with open(student_file, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        print("\nAll Students And Grades:")
        for row in csv_reader:
            snumber, sname, g1, g2, g3 = row
            try:
                average = (float(g1) + float(g2) + float(g3)) / 3
            except ValueError:
                average = 0
            print(f"{snumber} | {sname} | Grades: {g1}, {g2}, {g3} | Average: {average:.2f}")

# Main Menu
while True:
    choice = input("\nSelect an option:\n1. Teacher login\n2. Student login\n3. Create account\n4. Exit\nChoice: ")
    
    if choice == "1":
        if login_check("teacher"):
            while True:
                choice2 = input("\n1. Grade write\n2. Grade read\n3. Exit\nChoice: ")
                if choice2 == "1":
                    grade_write()
                elif choice2 == "2":
                    grade_read()
                elif choice2 == "3":
                    break
                else:
                    print("Invalid choice!")
    elif choice == "2":
        if login_check("student"):
            while True:
                choice3 = input("\n1. View grades\n2. Exit\nChoice: ")
                if choice3 == "1":
                    grade_read()
                elif choice3 == "2":
                    break
                else:
                    print("Invalid choice!")
    elif choice == "3":
        create_account()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
