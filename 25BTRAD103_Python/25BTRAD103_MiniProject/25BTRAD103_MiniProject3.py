
# Attendance Tracker

attendance = {}

def add_student():
    name = input("Enter student name: ")
    if name not in attendance:
        attendance[name] = {"Present": 0, "Total": 0}
        print("Student added successfully!")
    else:
        print("Student already exists.")

def update_attendance():
    name = input("Enter student name: ")

    if name in attendance:
        status = input("Enter attendance (P/A): ").upper()

        if status == "P":
            attendance[name]["Present"] += 1
            attendance[name]["Total"] += 1
            print("Marked Present.")
        elif status == "A":
            attendance[name]["Total"] += 1
            print("Marked Absent.")
        else:
            print("Invalid attendance status.")
    else:
        print("Student not found.")

def display_attendance():
    print("\n--- Attendance Records ---")

    if not attendance:
        print("No student records found.")
        return

    for name, record in attendance.items():
        total = record["Total"]
        present = record["Present"]

        if total > 0:
            percentage = (present / total) * 100
        else:
            percentage = 0

        print("Name:", name)
        print("Present:", present)
        print("Total Classes:", total)
        print("Attendance:", round(percentage, 2), "%")
        print("----------------------")

def check_shortage():
    threshold = float(input("Enter attendance threshold: "))

    print("\nStudents below", threshold, "%:")

    for name, record in attendance.items():
        total = record["Total"]

        if total > 0:
            percentage = (record["Present"] / total) * 100
        else:
            percentage = 0

        if percentage < threshold:
            print(name, "-", round(percentage, 2), "%")

while True:
    print("\n1. Add Student")
    print("2. Update Attendance")
    print("3. Display Attendance")
    print("4. Check Attendance Shortage")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_attendance()
    elif choice == "3":
        display_attendance()
    elif choice == "4":
        check_shortage()
    elif choice == "5":
        print("Exiting Attendance Tracker.")
        break
    else:
        print("Invalid choice.")



# Sales Data Analyzer

sales = {}

def add_product():
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity sold: "))
    price = float(input("Enter price per product: "))

    if quantity < 0 or price < 0:
        print("Quantity and price cannot be negative.")
        return

    if name in sales:
        sales[name]["Quantity"] += quantity
        sales[name]["Price"] = price
    else:
        sales[name] = {
            "Quantity": quantity,
            "Price": price
        }

    print("Sales record added/updated successfully!")

def display_sales():
    print("\n--- Product Sales Details ---")

    if not sales:
        print("No sales records found.")
        return

    total_sales = 0

    for name, details in sales.items():
        revenue = details["Quantity"] * details["Price"]
        total_sales += revenue

        print("Product:", name)
        print("Quantity Sold:", details["Quantity"])
        print("Price:", details["Price"])
        print("Revenue:", revenue)
        print("----------------------")

    print("Total Sales Revenue:", total_sales)

def highest_selling():
    if not sales:
        print("No products available.")
        return

    highest = max(sales, key=lambda x: sales[x]["Quantity"])

    print("Highest Selling Product:", highest)
    print("Quantity Sold:", sales[highest]["Quantity"])

def compare_sales():
    if not sales:
        print("No products available.")
        return

    print("\n--- Product-wise Sales Performance ---")

    for name, details in sales.items():
        revenue = details["Quantity"] * details["Price"]
        print(name, "-> Revenue:", revenue)

while True:
    print("\n1. Add/Update Product")
    print("2. Display Sales")
    print("3. Highest Selling Product")
    print("4. Compare Product Sales")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        display_sales()
    elif choice == "3":
        highest_selling()
    elif choice == "4":
        compare_sales()
    elif choice == "5":
        print("Exiting Sales Data Analyzer.")
        break
    else:
        print("Invalid choice.")
