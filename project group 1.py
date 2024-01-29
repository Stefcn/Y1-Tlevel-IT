import csv

def login():
    correct_username = "ADMIN"
    correct_password = "PASSWORD123"
    
    while True:
        entered_username = str(input("Enter username: "))
        entered_password = str(input("Enter password: "))
        
        if entered_username == correct_username and entered_password == correct_password:
            print("Login successful!")
            return True
        else:
            print("Wrong password or username.")


def enter_student_details():
    with open("StudentsData.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        print("\nEnterdetails:")
        id = input("Enter ID number: ")
        Firstname = input("Entr Firstname: ")
        Surname = input("Enter Surname: ")
        date_of_birth = input("Enter date of birth (Day/Month/year): ")
        address = input("Enter address: ")
        phone_number = input("Enter phone number: ")
        gender = input("Enter gender: ")
        tutor_group = input("Enter tutor group: ")
        
        writer.writerow([id, Firstname, Surname, date_of_birth, address, phone_number, gender, tutor_group])
        print("Student details have been added to the system")

def view_student_details():
    try:
        with open("Students.csv", mode='r') as file:
            reader = csv.reader(file)
            print("\nStudent details:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("student details cannot be found.")

def main():
    if login():
        while True:
            print("\nMenu:")
            print("1. Enter details")
            print("2. View details")
            print("3. Logout")
            choice = input("Enter your choice 1,2,3: ")
            
            if choice == "1":
                enter_student_details()
            elif choice == "2":
                view_student_details()
            elif choice == "3":
                print("Logged out.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()