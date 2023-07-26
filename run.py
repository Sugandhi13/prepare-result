# importing required libraries
import gspread
from google.oauth2.service_account import Credentials
import json

# defining constant variables
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('prepare_result')


def get_student_data():
    """
    Get student deatils (Name and Marks in different subjects) from teacher.
    """

    headings = SHEET.worksheet('student_data').get_all_values()[0]
    std_cmplt_data = []

    for i in range(len(headings)):
        w1, w2, w3 = headings[i].split('_')

        print()
        while True:
            std_data = input(f"Enter {w1} {w2} {w3} : ")
            if i == 0:
                if (validate_student_data("string_value_check", std_data)):
                    break
            else:
                if (validate_student_data("int_value_check", std_data)):
                    break

        std_cmplt_data.append(std_data)

    return std_cmplt_data


def validate_student_data(check, value):
    """
    Inside the try block,
    First check for missing value input and raise error if its empty,
    Secondly check for string value for special characters and raise error if exists,
    At last check if numeric value is out of range (0-100) and raise error if it does.
    """

    try:
        if not value:
            raise ValueError("This field should not be empty")
        elif (check == "string_value_check"):
            if (all(chr.isalpha() or chr.isspace() for chr in value) is False):
                raise ValueError(f"This field should not contains any number(s) or special charater(s), you provided '{value}'")
        elif (check == "int_value_check"):
            if (int(value) < 0):
                raise ValueError(f"The value should be greater than 0, you provided '{value}'")
            if (int(value) > 100):
                raise ValueError(f"The value should be less than 100, you provided '{value}'")

    except ValueError as ve:
        print(f"\nInvalid data: {ve}. Please try again!")
        return False

    return True


def update_student_data(new_row, worksheet):
    """
    Update student data in worksheet.
    """

    worksheet_name = worksheet.upper()
    print(f"\nUpdating {worksheet_name} worksheet...")
    worksheet_to_update = SHEET.worksheet(worksheet)

    # adds new row to the end of the current data
    worksheet_to_update.append_row(new_row)

    print(f"\n{worksheet_name} worksheet updated successfully.")


def update_student_result(new_row, worksheet):
    """
    Update student result in worksheets.
    """

    worksheet_name = worksheet.upper()
    print(f"\nUpdating {worksheet_name} worksheet...")
    worksheet_to_update = SHEET.worksheet(worksheet)

    # adds new row to the end of the current data
    for row in new_row:
        worksheet_to_update.append_row(row)

    print(f"\n{worksheet_name} worksheet updated successfully.")


def calculate_grades(std_percentage):
    """
    Calculate and return the grade value baesd upon percentage of marks.
    """

    std_grade = ''

    if std_percentage >= 95:
        std_grade = 'A+'
    elif std_percentage >= 85:
        std_grade = 'A'
    elif std_percentage >= 70:
        std_grade = 'B+'
    elif std_percentage >= 55:
        std_grade = 'B'
    elif std_percentage >= 40:
        std_grade = 'C'
    else:
        std_grade = 'F'

    return std_grade


def calculate_result():
    """
    Calculate the result of students using marks in each subject.
    Firstly calculated the total marks,
    then percentage of marks out of max total marks of 500.
    At last, called calculate_grades() function to assign grades to students.
    """

    print("\nCalculating student(s) result...")
    marks = SHEET.worksheet('student_data').get_all_values()
    final_result = []

    if (len(marks) > 1):

        for i in range(1, len(marks)):
            std_name = ''
            total_marks = 0
            result = []

            for j in range(len(marks[i])):

                if j == 0:
                    std_name = marks[i][j]
                else:
                    total_marks += int(marks[i][j])

            result.append(std_name)
            result.append(total_marks)
            percentage = round(((total_marks / 500) * 100), 2)
            result.append(percentage)
            grade = calculate_grades(percentage)
            result.append(grade)
            final_result.append(result)
    
        print("\nStudent(s) result calculation completed successfully.")

    else:
        print("\nNo student data available to calculate result!")

    return final_result


def show_result():
    """
    Show student(s) results.
    """

    full_result = SHEET.worksheet('student_result').get_all_values()
    if (len(full_result) > 1):
        print()
        for i in range(len(full_result)):
            if (i != 0):
                print(f"| {full_result[i][0]} \t| {full_result[i][1]} \t| {full_result[i][2]} \t| {full_result[i][3]} | ")
    else:
        print("\nNo result data to display!")


def main():
    """
    Run all program functions.
    """

    while True:
        print("\nEnter '1' to add student data")
        print("Enter '2' to calculate result")
        print("Enter '3' to view result")
        print("Enter '4' to exit")
        select_choice = int(input("\nPlease, enter an option : "))

        if (select_choice == 1):

            while True:
                student_data = get_student_data()
                update_student_data(student_data, "student_data")

                print("\nEnter 'Y' to add more student data.")
                print("Enter 'N' exit.")
                add_data_check = input("\nPlease, enter your choice : ")

                if (add_data_check.lower() != 'y'):
                    break

        elif (select_choice == 2):
            student_result = calculate_result()

            if (student_result):
                update_student_result(student_result, "student_result")
                show_result()

        elif (select_choice == 3):
            show_result()

        elif (select_choice == 4):
            break


main()  # calling main function to run the whole program
