# importing required libraries
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
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


def confirm_data_delete(data_to_delete):
    """
    Check from user if he is surely want to delete data.
    """

    sheet_name = data_to_delete.upper()
    while True:
        print("\n----------------------------------------------")
        print(f"Are you sure you want to delete {sheet_name}?")
        print("Once deleted this data can't be recovered!")
        print(f"\nEnter '1' to delete {sheet_name}.")
        print("Enter '0' to return on previous menu.")
        print("----------------------------------------------")
        delete_data_check = input("\nConfirm your action : ")

        if (delete_data_check == '0'):
            break

        elif (delete_data_check == '1'):
            return True

        else:
            validate_student_data("delete_data_check", delete_data_check)


def clear_worksheet(sheet_to_clear):
    """
    Remove all data except heading row from the worksheet.
    """

    headings = SHEET.worksheet(sheet_to_clear).get_all_values()[0]
    worksheet_to_clear = SHEET.worksheet(sheet_to_clear)
    worksheet_to_clear.clear()
    worksheet_to_clear.append_row(headings)


def validate_student_data(check, value):
    """
    Inside the try block raise error if,
    user try to give input of missing value, special characters or
    a numeric value that is out of range (0-100) for subject marks.
    """

    try:
        if not value:
            raise ValueError("this field should not be empty")
        elif (check == "option_value_check"):
            if ((int(value) < 0) | (int(value) > 5)):
                raise ValueError(f"enter a valid option value, you provided '{value}'")
        elif (check == "add_data_check"):
            if int(value):
                raise ValueError(f"enter a valid option value, you provided '{value}'")
        elif (check == "clear_sheet_check"):
            if int(value):
                raise ValueError(f"enter a valid option value, you provided '{value}'")
        elif (check == "delete_data_check"):
            if int(value):
                raise ValueError(f"enter a valid option value, you provided '{value}'")
        elif (check == "string_value_check"):
            if (all(chr.isalpha() or chr.isspace() for chr in value) is False):
                raise ValueError(f"only alphabets are allowed, you provided '{value}'")
        elif (check == "int_value_check"):
            if (int(value) < 0):
                raise ValueError(f"value should be greater than 0, you provided '{value}'")
            if (int(value) > 100):
                raise ValueError(f"value should be less than 100, you provided '{value}'")

    except ValueError as ve:
        print(f"\nInvalid data: {ve}. Please try again!")
        return False

    return True


def get_student_data():
    """
    Get student deatils (Name and Marks in different subjects) from teacher.
    """

    headings = SHEET.worksheet('student_data').get_all_values()[0]
    std_cmplt_data = []

    print("\n----------------------------------------------")
    for i in range(len(headings)):

        while True:

            if i == 0:
                std_data = input("Enter Student Full Name : ")

                if (validate_student_data("string_value_check", std_data)):
                    break

            else:
                std_data = input(f"Enter Marks in {headings[i]} : ")

                if (validate_student_data("int_value_check", std_data)):
                    break

        std_cmplt_data.append(std_data)

    print("----------------------------------------------")
    return std_cmplt_data


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


def show_student_data():
    """
    Show student(s) data.
    """

    full_student_data = SHEET.worksheet('student_data').get_all_values()
    print()

    if (len(full_student_data) > 1):
        header = full_student_data[0]
        data = full_student_data[1:]
        print(tabulate(data, header, tablefmt="fancy_outline"))

    else:
        print("No student data to display!")


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

    print("\n----------------------------------------------")
    print("Calculating student(s) result...")
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
            percentage = total_marks / 500
            result.append(percentage)
            grade = calculate_grades(percentage)
            result.append(grade)
            final_result.append(result)

        print("\nStudent(s) result calculated successfully.")

    else:
        print("\nNo student data available to calculate result!")

    return final_result


def update_student_result(new_row, worksheet):
    """
    Update student result in worksheets.
    """

    worksheet_name = worksheet.upper()
    print(f"\nUpdating {worksheet_name} worksheet...")

    clear_worksheet(worksheet)
    worksheet_to_update = SHEET.worksheet(worksheet)

    for row in new_row:
        worksheet_to_update.append_row(row)

    print(f"\n{worksheet_name} worksheet updated successfully.")


def show_result():
    """
    Show student(s) results.
    """

    full_result = SHEET.worksheet('student_result').get_all_values()
    print()

    if (len(full_result) > 1):
        header = full_result[0]
        data = full_result[1:]

        print(tabulate(data, header, tablefmt="fancy_outline"))

    else:
        print("No result data to display!")


def main():
    """
    Run all program functions.
    """

    while True:
        print("\n==============================================")
        print("Enter '1' to Add New Data")
        print("Enter '2' to Calculate Result")
        print("Enter '3' to View Student Data")
        print("Enter '4' to View Result")
        print("Enter '5' to Clear Existing Data")
        print("Enter '0' to End the Program")
        print("==============================================")

        option = None
        option_selected = input("\nPlease, enter an option : ")

        if (validate_student_data("option_value_check", option_selected)):
            option = int(option_selected)

        if (option == 1):

            student_data = get_student_data()
            update_student_data(student_data, "student_data")

            while True:
                print("\n==============================================")
                print("Enter '1' to Add more Student Data.")
                print("Enter '0' to Exit.")
                print("==============================================")
                add_data_check = input("\nPlease, enter your choice : ")

                if ((add_data_check != '1') & (add_data_check != '0')):
                    validate_student_data("add_data_check", add_data_check)

                elif (add_data_check == '0'):
                    break

                else:
                    student_data = get_student_data()
                    update_student_data(student_data, "student_data")

            show_student_data()

        elif (option == 2):
            student_result = calculate_result()

            if (student_result):
                update_student_result(student_result, "student_result")
                show_result()

        elif (option == 3):
            show_student_data()

        elif (option == 4):
            show_result()

        elif (option == 5):

            while True:
                print("\n==============================================")
                print("Enter '1' to Delete Student Data.")
                print("Enter '2' to Delete Student Result Data.")
                print("Enter '0' to Exit")
                print("==============================================")
                clear_sheet_check = input("\nPlease, enter your choice : ")

                if (clear_sheet_check == '0'):
                    break

                elif (clear_sheet_check == '1'):

                    if (confirm_data_delete("student_data")):
                        data = SHEET.worksheet("student_data").get_all_values()

                        if (len(data) > 1):
                            print("\n----------------------------------------------")
                            print("Deleting Student Data...")
                            clear_worksheet("student_data")
                            print("\nStudent Data deleted successfully.")

                        else:
                            print("\n----------------------------------------------")
                            print("Student Data worksheet is already empty!")
                            print("No data to delete.")

                elif (clear_sheet_check == '2'):

                    if (confirm_data_delete("student_result")):
                        data = SHEET.worksheet("student_result").get_all_values()

                        if (len(data) > 1):
                            print("\n----------------------------------------------")
                            print("Deleting Student Result Data...")
                            clear_worksheet("student_result")
                            print("\nStudent Result Data deleted successfully.")

                        else:
                            print("\n----------------------------------------------")
                            print("Student Result Data worksheet is already empty!")
                            print("No data to delete.")

                else:
                    validate_student_data("clear_sheet_check", clear_sheet_check)

        elif (option == 0):
            print("\n----------------------------------------------")
            print("Thank you! I hope you will visit again :)")
            print("----------------------------------------------\n")
            break


main()  # calling main function to run the whole program
