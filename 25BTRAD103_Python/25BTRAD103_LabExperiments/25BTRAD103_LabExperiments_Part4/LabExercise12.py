
# Student Data Manager Using Files

FILE_NAME = "students.txt"

while True:
    print("\n--- STUDENT DATA MANAGER ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter roll number: ")
        name = input("Enter student name: ")
        marks = input("Enter marks: ")

        with open(FILE_NAME, "a") as file:
            file.write(roll + "," + name + "," + marks + "\n")

        print("Student added successfully!")

    elif choice == "2":
        try:
            with open(FILE_NAME, "r") as file:
                print("\nStudent Records:")
                for line in file:
                    print(line.strip())

        except FileNotFoundError:
            print("No student records found!")

    elif choice == "3":
        roll = input("Enter roll number to search: ")
        found = False

        try:
            with open(FILE_NAME, "r") as file:
                for line in file:
                    data = line.strip().split(",")

                    if data[0] == roll:
                        print("Student Found:", data)
                        found = True
                        break

            if not found:
                print("Student not found!")

        except FileNotFoundError:
            print("File not found!")

    elif choice == "4":
        roll = input("Enter roll number to update: ")
        found = False

        try:
            with open(FILE_NAME, "r") as file:
                records = file.readlines()

            with open(FILE_NAME, "w") as file:
                for line in records:
                    data = line.strip().split(",")

                    if data[0] == roll:
                        name = input("Enter new name: ")
                        marks = input("Enter new marks: ")
                        file.write(roll + "," + name + "," + marks + "\n")
                        found = True
                    else:
                        file.write(line)

            if found:
                print("Student record updated!")
            else:
                print("Student not found!")

        except FileNotFoundError:
            print("File not found!")

    elif choice == "5":
        print("Exiting Student Data Manager.")
        break

    else:
        print("Invalid choice!")
