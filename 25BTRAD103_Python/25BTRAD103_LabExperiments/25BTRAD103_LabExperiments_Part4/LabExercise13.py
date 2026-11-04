
# CSV-Based Payroll Management System

import csv

# Creating employee CSV file
with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Basic", "Allowance"])

    writer.writerow([101, "Ali", 20000, 5000])
    writer.writerow([102, "Sara", 25000, 6000])
    writer.writerow([103, "Ahmed", 30000, 7000])

# Reading employee records
try:
    with open("employees.csv", "r") as file:
        reader = csv.DictReader(file)

        print("\n--- PAYROLL SUMMARY ---")

        for emp in reader:
            basic = float(emp["Basic"])
            allowance = float(emp["Allowance"])

            gross = basic + allowance

            deduction = gross * 0.10

            net = gross - deduction

            print("\nEmployee ID:", emp["ID"])
            print("Name:", emp["Name"])
            print("Basic Salary:", basic)
            print("Allowance:", allowance)
            print("Gross Salary:", gross)
            print("Deduction:", deduction)
            print("Net Salary:", net)

except FileNotFoundError:
    print("Employee CSV file not found!")
