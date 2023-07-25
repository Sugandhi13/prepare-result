import gspread
from google.oauth2.service_account import Credentials
import json

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('prepare_result')


def student_data():
    """
    get Student details
    """
    data = []
    std_name = input("Enter Student Full Name: \n")
    data.append(std_name)
    swedish_marks = input("Enter Marks in Swedish: \n")
    data.append(swedish_marks)
    english_marks = input("Enter Marks in English: \n")
    data.append(english_marks)
    mathematics_marks = input("Enter Marks in Mathematics: \n")
    data.append(mathematics_marks)
    science_marks = input("Enter Marks in Science: \n")
    data.append(science_marks)
    technology_marks = input("Enter Marks in Technology: \n")
    data.append(technology_marks)
    print(std_name, swedish_marks, english_marks, mathematics_marks, science_marks, technology_marks)
    return data


stddata = student_data()


def update_studentdata(new_row, worksheet):
    """
    Update the  worksheet,
    data entered by teacher.
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)

    # adds new row to the end of the current data
    worksheet_to_update.append_row(new_row)

    print(f"{worksheet} worksheet updated successfully\n")


update_studentdata(stddata, "student_data")

