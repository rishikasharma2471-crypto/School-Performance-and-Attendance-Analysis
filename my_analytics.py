import csv
#storing the name of our downloaded Kaggle dataset file
file_name = "student_data.csv"
# opening the CSV file in read mode using a safe gatekeeper "with"
with open(file_name, mode="r", encoding="UTF-8") as file:
    #convert CSV rows into data dictionaries
    reader = csv.DictReader(file)
    #print headings of the excel sheets
    print(reader.fieldnames)

#empty list to store all students data
    students_database = []

    #loop to read file line by line
    for row in reader:
        #save each student record into database list
        students_database.append(row)
#show success status
print("\n=============================================")
print(f"Success! Total {len(students_database)} students loaded into Python database.")
print("=============================================")

#continuous app loop for interactive menu
while True:
    print("\n=============================================")
    print("SCHOOL ANALYTICS CENTRAL DASHBOARD")
    print("=============================================")
    print("1. View first 5 student profiles (Data Slicing)")
    print("2. Find high academic risk students (Failures > 0)")
    print("3. Analyze final exam performance (G3 Passing Status)")
    print("4. Exit application")

    #take the input from the user
    choice = input("\nEnter your option (1-4): ")

    #data slicing (Reads index 0 to 4)
    if choice == "1":
        print("\n--- Displaying Sample Student Profiles ---")
        for student in students_database[:5]:
            print(
                f"Age: {student['age']} | Study Time: {student['studytime']} | Failures: {student['failures']} | Final Grade (G3): {student['G3']}"
            )

    #filter students using If-Else condition
    elif choice == "2":
        print("\n--- Academic Risk Alert (Students with past failures)---")
        risk_count = 0
        for student in students_database:
            #change text data into int number for calculation
            if int(student["failures"]) > 0:
                print(
                    f"Student Age: {student['age']} | Total Past Failures: {student['failures']}"
                )
                risk_count += 1
        print(f"\nTotal vulnerable students flagged: {risk_count}")

    #counter logic to check overall pass/fail ratio
    elif choice == "3":
        print("\n--- Final Exam Grade Evaluation (G3 out of 20)---")
        passed = 0
        failed = 0
        for student in students_database:
            # Is dataset me 20 me se 10 score standard passing marks mana jata hai
            if int(student["G3"]) >= 10:
                passed += 1
            else:
                failed += 1
        print(f"Total Students Passed: {passed}")
        print(f"Total Students Failed: {failed}")

    #break keyword to stop loop and turn off system
    elif choice == "4":
        print(
            "\nShutting down analytics console. Good luck with your SOET placements!"
        )
        break

#handle wrong inputs automatically
else:
        print("Invalid selection! Please choose a number between 1 and 4.")
