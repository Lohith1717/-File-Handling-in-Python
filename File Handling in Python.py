FILENAME = "students.txt"

def add_student():
    with open(FILENAME, "a") as file:   # append mode
        name = input("Enter Name: ")
        roll = input("Enter Roll No: ")
        marks = input("Enter Marks: ")

        record = name + "," + roll + "," + marks + "\n"
        file.write(record)

    print("✅ Student details saved successfully!\n")


def view_students():
    try:
        with open(FILENAME, "r") as file:   # read mode
            data = file.readlines()

            if not data:
                print("⚠ File is empty\n")
                return

            print("\n----- Student Records -----")
            for line in data:
                name, roll, marks = line.strip().split(",")
                print(f"Name: {name} | Roll: {roll} | Marks: {marks}")
            print()

    except FileNotFoundError:
        print("⚠ No file found. Add students first!\n")

while True:
    print("====== STUDENT FILE MENU ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice\n")
