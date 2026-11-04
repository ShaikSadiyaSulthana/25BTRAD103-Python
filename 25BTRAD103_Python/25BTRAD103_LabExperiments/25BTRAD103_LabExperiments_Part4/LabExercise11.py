
# Log File Reader Program

# Creating a sample log file
with open("application.log", "w") as file:
    file.write("INFO: Application started\n")
    file.write("ERROR: Database connection failed\n")
    file.write("WARNING: Low memory\n")
    file.write("INFO: User logged in\n")
    file.write("ERROR: File not found\n")
    file.write("INFO: Application closed\n")

# Counting log categories
count = {
    "ERROR": 0,
    "WARNING": 0,
    "INFO": 0
}

try:
    with open("application.log", "r") as file:
        lines = file.readlines()

        if not lines:
            print("Log file is empty.")

        else:
            for line in lines:
                for keyword in count:
                    if keyword in line:
                        count[keyword] += 1

            print("\nLog Summary:")
            for keyword, total in count.items():
                print(keyword, ":", total)

except FileNotFoundError:
    print("Log file not found!")
