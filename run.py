#importing required libraries
import gspread
from google.oauth2.service_account import Credentials
import json

#defining constant variables
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

        while True:
            std_data = input(f"\nEnter {w1} {w2} {w3} : ")
            if i == 0:
                if (validate_student_data("string_value_check",std_data)):
                    break
            else:
                if (validate_student_data("int_value_check",std_data)):
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
            if (all(chr.isalpha() or chr.isspace() for chr in value) == False):
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
    Update student data in the Prepare_Results's worksheets.
    """

    print(f"\nUpdating '{worksheet}' worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)

    # adds new row to the end of the current data
    worksheet_to_update.append_row(new_row)

    print(f"\n'{worksheet}' worksheet updated successfully\n")

def main():
    """
    Run all program functions.
    """

    student_data = get_student_data()
    update_student_data(student_data, "student_data")

main() #calling main function to run the whole program