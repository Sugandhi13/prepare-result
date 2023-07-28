# Prepare Result

Prepare Result application is developed with idea for making teachers life easy to make students result in quick and accurate manner. A user can use different options to add data of students, calculate results of all students, view student data added or result calculated. Also, the user has option to delete the student data or results calculated and start a fresh. The whole data is stored at backend on a Google Spreadsheet as well. Hence, a user has option to come back later and add more data or directly go and view student data or their results.

![Homepage-Image](/assets/images/landingview.jpg)

The Prepare Result application is live on Heroku, the links can be found [HERE](https://sugandhi13.github.io/quiz-india/)

# Table of contents

- [Prepare Result](#prepare-result)
- [Table of contents](#table-of-contents)
- [UX](#ux)
    - [Application Purpose](#application-purpose)
    - [Audience](#audience)
    - [Communication](#communication)
    - [User Goals](#user-goals)
    - [Future Goals](#future-goals)
- [Design](#design)
    - [Wireframe](#wireframe)
- [Features](#features)
  - [Common Features](#common-features)
    - [Languages Used](#languages-used)
    - [Color Scheme](#color-scheme)
    - [Navigation](#navigation)
  - [Application Functions](#application-functions)
    - [Add New Data](#add-new-data)
    - [Calculate Result](#calculate-result)
    - [View Student Data](#view-student-data)
    - [View Result](#view-result)
    - [Delete Data Stored](#delete-data-stored)
    - [End the Program](#end-the-program)
  - [Google Spreadsheet - Data Storage](#google-spreadsheet---data-storage)
    - [Student Data Worksheet](#student-data-worksheet)
    - [Student Results Data Worksheet](#student-results-data-worksheet)
- [Testing](#testing)
    - [Manual Testing](#manual-testing)
- [Validation Testing](#validation-testing)
    - [PEP8 - CI Python Linter](#pep8---ci-python-linter)
    - [String Input Validation](#string-input-validation)
    - [Integer Input Validation](#integer-input-validation)
- [Unfixed Bugs](#unfixed-bugs)
- [Libraries \& Programs Used](#libraries--programs-used)
- [Deployment](#deployment)
- [Credits](#credits)
- [Content](#content)

# UX

###  Application Purpose
The purpose of this application is to store student data (Name and Marks of 5 subjects). Calculate the results using student data added. View student data or the  result calculated. Store data on Google Spreadsheet to keep data for future use. Lastly, if users wishes, he has option to delete all data stored on Google Spreadsheet. 

### Audience
This site designed for school teachers or educational instuations. This site will help them to prepare result of students in quick and esay manner. 

### Communication
The overall design was kept extremely simple on purpose. A user has following options while using this site.
1. **Add New Data:** To add student data like Name and marks in different subject.
2. **Calculate Result:** To calculate the results (Total markes, percentage scored and assign grade as per rules defined) of all students. 
3. **View Student Data:** To view the the student data of all students added by the user.
4. **View Result:** To view the result of all students added by the user.
5. **Delete Data Stored:** To delete student data or student result data.
6. **End the Program:** To end the program.

### User Goals
The main user goal we have tried to achieve here is to help them calculating the student result fast and accurately. This application will not only calculate the total marks scored by student in 5 subjects but calculate and display the percentage scored in total and assign the grade according to the rules given.

### Future Goals
The more I was working on this application the more I was getting hopeful that what all can be done here. Listing below a few near future goals with respect to this application features.
- Flexibility for user to add subjects as per his own wish
- Edit the student data
- Delete a specific student record
- Power in the hand of user to set rules for different grades

# Design

### Wireframe

Microsoft Powerpoint was used to plan the logic for this project. Below is a screenshot of the logic.

# Features

## Common Features

### Languages Used

- Python

### Color Scheme

Different colors are used to display different kind of information on the terminal.

- The error messages text are displayed in red font (Format code: \033[1;31m).
- The thankyou message text while ending the program is displayed in green font (Format code: \033[1;32m).
- All kind of menus texts are displayed in yellow font (Format code: \033[1;33m).
- Any important text is displayed in purple font (Format code: \033[1;35m).
- Any informational message text is display in cyan font format (Format code: \033[1;36m)
- All line brakes added to separate the text is and any input asked from the user is displayed in white font format (Format code: \033[1;37m)

### Navigation

In this application a user has given 6 options upfront mentioned below. There are also some sub menus mentioned below as well.
1. **Add New Data:** To add student data like Name and marks in different subject.
    1. **Add more Student Data:** To add more student data without exiting to previous menu.
    2. **Exit:** To return to previous menu.
2. **Calculate Result:** To calculate the results (Total markes, percentage scored and assign grade as per rules defined) of all students. 
3. **View Student Data:** To view the the student data of all students added by the user.
4. **View Result:** To view the result of all students added by the user.
5. **Delete Data Stored:** To delete student data or student result data.
    1. **Delete Student Data:** To delete student data.
        1. **Confirm Delete:** To confirm from user if he really wants to delete the whole student data.
        2. **Return to Previous Menu:** To return to previous menu.
    2. **Delete Student Result Data:** To delete student result data.
        1. **Confirm Delete:** To confirm from user if he really wants to delete the whole student result data.
        2. **Return to Previous Menu:** To return to previous menu.
    3. **Exit:** To return to previous menu.
6. **End the Program:** To end the program.

## Application Functions

This application have 6 functions explained below in detail. The application is equiped with complete validation rules. Hence if a user enters any invalid value, when asked to give input either as option to move to and from in menu or while entering student data, an error message will be displayed to user with the reason of error.

### Add New Data

The user has to enter '1' if data for a student needs to be added to calculate the result. A series of questions will be asked to add student name and marks in different subjects. Each subject has been assumed to be of 100 marks. Hence, the user can only enter the marks between the range of 0 to 100. Once the information is added the same information will be stored in *student_data* worksheet (Google Spreadsheet). After that, a sub menu populate and check with user if he would like to add more student data or not.

![Add-New_Data](/assets/images/addnewdata.jpg)

- **Add more Student Data:** A user has to enter '1' if he wishes to enter more student data. If this option is entered then again the same series of question will be asked as mentioned in point 1 above and at the end again the sub menu will populate to reconfirm from user if the user want to add more student data or not.

![Add-More-Student-Data](/assets/images/addmorestudentdata.jpg)

- **Exit:** A user has to enter '0' to exit from the loop of keep adding user data, if he has no more data to add. If this option is entered then the whole student data stored on *student_data* worksheet (Google Spreadsheet) will be displayed in tabular form and then the user will route back to pervious menu.

### Calculate Result

The user has to enter '2' if the results of all students needs to be calculated. This function helps to calculate the following values for each student.
- **Total Markes:** This will be calculated by the sum of marks scored by a student in all 5 subjects.
- **Percentage Scored:** This will be calculated by the *Total Marks* scored by a student against maximum marks of 500 (total of all subjects).
- **Grade:** This will be calculated by using the *Percentage Scored* by a student against a set of per-defined rules given below.
    - Grade A+, if *Percentage Scored* is greater than or equal to 95
    - Grade A, if *Percentage Scored* is greater than or equal to 85
    - Grade B+, if *Percentage Scored* is greater than or equal to 70
    - Grade B, if *Percentage Scored* is greater than or equal to 55
    - Grade C, if *Percentage Scored* is greater than or equal to 40
    - Grade F (Fail), if *Percentage Scored* is less than 40

Once the information is added the same information will be stored in *student_result* worksheet (Google Spreadsheet). Also, the results of all students will be displayed at the end in tabular form.

![Calculate-Result](/assets/images/calculateresult.jpg)

### View Student Data

The user has to enter '3' if the user would like to see the student data. Whole data stored in *student_data* worksheet (Google Spreadsheet) will be displayed in tabular form. 
If there is no data available in *student_data* worksheet then a message will be displayed to user that *"No student data to display!"*.

![View-Student-data](/assets/images/viewstudentdata.jpg)

### View Result

The user has to enter '4' if the user would like to see the student result data. Whole data stored in *student_result* worksheet (Google Spreadsheet) will be displayed in tabular form. 
If there is no data available in *student_result* worksheet then a message will be displayed to user that *"No student result data to display!"*.

![View-Result-Data](/assets/images/viewresultdata.jpg)

### Delete Data Stored

The user has to enter '5' if the user would like to delete any data already stored on Google Spreadsheet. If the user enters this option a sub menu will populate to confirm that which data (Student Data or Student Results Data) the user want's to delete. These options are described below.

![Delete-Data-Stored](/assets/images/deletedata.jpg)

1. **Delete Student Data:** The user has to enter '1' if the user would like to delete student data stored on *student_data* worksheet (Google Spreadsheet). If the user enter this option. A confirmation message will populate to user with Warning that once the data is deleted, it cann't be recovered and another confirmation from user will be required to proceed further and actually delete the data.
    1. **Confirm Delete:** The user has to enter '1' to confirm that the data should be deleted. If the user confirms it then the data will be deleted from *student_data* worksheet (Google Spreadsheet) and only headings will remain in *student_data* worksheet (Google Spreadsheet) and a confirmation message will be displayed to user that data has been deleted successfully. If the *student_data* worksheet is already empty then a message will be displayed to user that *No data to delete.*.

    ![Delete-Student-Data](/assets/images/deletestudentdata.jpg)

    2. **Return to Previous Menu:** A user has to enter '0' to if the user changes its mind and don't want to delete the data. If this option is entered then no further action will be taken and then the user will route back to pervious menu.
2. **Delete Student Result Data:** The user has to enter '1' if the user would like to delete student result data stored on *student_result* worksheet (Google Spreadsheet). If the user enter this option. A confirmation message will populate to user with Warning that once the data is deleted, it cann't be recovered and another confirmation from user will be required to proceed further and actually delete the data.
    1. **Confirm Delete:** The user has to enter '1' to confirm that the data should be deleted. If the user confirms it then the data will be deleted from *student_data* worksheet (Google Spreadsheet) and only headings will remain in *student_data* worksheet (Google Spreadsheet) and a confirmation message will be displayed to user that data has been deleted successfully. If the *student_data* worksheet is already empty then a message will be displayed to user that *No data to delete.*.
    2. **Return to Previous Menu:** A user has to enter '0' to if the user changes its mind and don't want to delete the data. If this option is entered then no further action will be taken and then the user will route back to pervious menu.
3. **Exit:** The user has to enter '0' to return on the previous menu. 

### End the Program

A user has to enter '0' to end the program. If the user enter this option a thank you message *"Thank you! I hope you will visit again :)"* will be displayed and program will end.

![End-Program](/assets/images/endofprogram.jpg)

## Google Spreadsheet - Data Storage

Google spreadsheet has been used to store the student data entered by the user as well as the results calculated by this application for the user. The goole spreadsheet also used as storage database and it helps the user to come at any point back on the system and either add more student data and refresh the results or delete data stored.

### Student Data Worksheet

![Student-Data](/assets/images/studentdataworksheet.jpg)

### Student Results Data Worksheet

![Student-Result-Data](/assets/images/studentresultdataworksheet.jpg)

# Testing

The site has been tested for all validation rules applied. All input fields and options are required to be filled correctly by the user before submitting. Also the application has been tested for the kind of data its asked to store/display does it or not.

Writing python functions main() to make sure the that the execution sequence stay correct and the user get in and out of different menues was the biggest challenge during this project. Along with this some difficulty were also faced while writing code for delete data from a worksheet or show results in tabular form. I have referred various code available on Stackoverflow, geeksforgeeks or python official website. I've also referred couple of github project shared by my mentor "Martina Terlevic". With the help of all those code I am able to write the best fit code as per my current understanding of Python.

### Manual Testing
| Test Case | Expected Results | Results |
| ----------- | ----------- | ----------- |
| "Add New Data" open up and ask the user to fill student data When user enter option '1' | "Add New Data" section open up and ask the user to enter student name and marks in various subject one by one. Ex: Only after entring the student name the marks in 1st subject "Swedish" will be asked to enter and the same process will be followed further. Once the user enter all information a sub-menu should open up and ask the user if he wishes to add more students data. If the user confirms, repect the whole sequence once again. If user don't wish to enter any student data further, display all student data available till now and return to previous menu. | As Expected |
| "Calculate Result" action should be performed When user enter option '2' | Results calculation (total marks, percentage scored and assignment of grade as per per-defined rules) should perform using student data stored on Google Spreadsheet and user should get message of result calculation begin and completed successfully. Also, results should be displayed at the end with total_marks, percentage and grade calculated correctly. | As Expected |
| "View Student Data" action should be performed When user enter option '3' | "View Student Data" section open up and student data should be displayed. | As Expected |
| "View Result" action should be performed When user enter option '4' | "View Result" section open up and student result data should be displayed. | As Expected |
| "Clear Existing Data" action should be performed When user enter option '5' | "Clear Existing Data" section open up and a series of question should be asked to user which data (student data or results data) needs to be deleted. Also, double check with user along with Warning that data once deleted can't be recovered. If user confirms to delete the data. The respective data should be deleted from Google Spreadsheet. | As Expected |
| "End the Program" action should be performed When user enter option '0' | The program should end successfully with a thank you message. | As Expected |
| Error Message: The field should not be empty | When a user needs to be input any value either for any option or while adding student data like name or marks in different subject. If the user don't enter any data and try to move forward by pressing enter key. An error message should display that the field should not be empty | As Expected |
| Error Message: Invalid integer value | When a user needs to be input any integer value either for any option or while adding student data (marks in different subject). If the user enter any non-integer value like alphabet or special character. An error message should display that the integer value expected. | As Expected |
| Error Message: Invalid string value | When a user needs to be input any string value while adding student data (Student Name). If the user enter any integer or special character (except whitespace). An error message should display that the string value expected. | As Expected |
| Error Message: Out of range value for student marks in different subject | When a user needs to input student data (marks in different subject). If the user enter out of range value (less than 0 or greater than 100). An error message should display that the value enter is out of range. | As Expected |
| Error Message: Out of range value for different options | When a user needs to input the value for any option the user wants to select. If the user enter out of range value (outside the range of options provided). Ex: Main menu has option from 0 to 5 and user input 6. An error message should display that the invalid value entered. | As Expected |

# Validation Testing

### PEP8 - CI Python Linter

No errors were returned when code verified through the PEP8 - CI Python Linter.

![PEP8](/assets/images/codevalidation.jpg)

### String Input Validation

In application, When a user needs to input a string value, only alphabets and spaces as input are allowed in such cases. If user tries to leave it blank, enters special characters or numeric values. The error is getting generated as expected.

![String-Input-Validation](/assets/images/validationsonstudentname.jpg)

### Integer Input Validation

In application, When a user needs to input an integer value, only numbers as input are allowed in such cases. If user tries to leave it blank, enters special characters or alphabets values. The error is getting generated as expected.

![Integer-Input-Validation](/assets/images/validationsonstudentmarks.jpg)

# Unfixed Bugs

When we did the code validation using PEP8 - CI Python Linter. It has shown line lengths errors at various places in my code. I've fixed them with shorten the text in smartest way possible as well as reduced the length of some variables name to make sure the code link fits in required line width.

I've also faced some error while trying to implement validation rules on various input fields. I've fixed them by using try/catch functionality. 

There is no known unfixed bug in my code as per my understanding.

# Libraries & Programs Used

- **Github:** This is used as the code store repository.
- **Codeanywhere:** This is used create the python code, readme, creds and requirement files.
- **Gspread:** This is used to enable the opening, accessing and reading of googlesheet data.
- **Google Cloud Plateform:** This is used to create unique identifiers required to access Google sheets.
- **Tabulate *(Python Library)*:** This python library is used to convert data from list into tabular form while printing on terminal.
- **Heroku:** This is used to deploy my application to be accessed by public.
- **CI Python Linter:** This is used for python code validation.
  
# Deployment

This app is deployed to Heroku. Below are the steps taken for its deployment

- Create an account and log in to Heroku.
    - Add a Credit/Debit card details in billing information section in Heroku.
    - Connected the CI Student Developer pack with Heroku to get the credits to make app live.
- Create a new app
- Go to settings option
- Add 'key/value' pairs. 
    - First key is CREDS and its value is copied from creds.json file on Codeanywhere. 
    - The second key is PORT with 8000 as its value 
- Add build pack. Add python first and then nodejs second in that order.
- Go to the top of the page, then select 'deploy tab' and then choose deployment method 'GitHub'.
- Next, under 'App connected to GitHub' section connect with GitHub by login to your account, type your repositary name and select correct respositary and click on connect button.
- Once the connection is established. Goto 'Manual deploy' section and Click on Deploy Branch button and make sure main branch is selected.
- Wait for the project to be deployed successfully on Heroku message. 
- Once the successfull message appear. Click on View button to access the application.

# Credits

I have really enjoyed the Code Institute course up till now, and I am looking forward to the next units of the course. I wanted to thank the Slack Community for their support learning the content and my Mentor Martina for her guidance with this project and assurances that creating a python application is not as scary as I initially thought.

As a starting point I looked at the Love Sandwiches projects.

- From the Love Sandwiches Project, I took inspiration about how to make application using python.
- Bank of python, My mentor has shared the GitHub repository created by an old CI student. It helped me in great deal to think a different idea than the most popular suggestion available on the internet.
- Stackoverflow, I have referred this website to take guidance regarding how to empty a google spreadsheet from python.
- Geeksforgeeks, I have referred this website to understand the code about how to restring the user to enter only alphabets and spaces for a string input field.
- Educba, This website helped me to understand how to print output as a table.
- pypi, This website I have used to try, test and used different table formatting option available in python using tabulate library.
- Kaggle, I used kaggle.com to understand how to apply different colors for python text printing on the terminal.

# Content

Following websites have been used as to get better understanding and apply different logics while creating Prepare Result application.

- [geeksforgeeks.org](https://www.geeksforgeeks.org/python-test-if-string-contains-alphabets-and-spaces/)
- [stackoverflow.com](https://stackoverflow.com/questions/41986898/google-sheets-api-python-clear-sheet)
- [educba.com](https://www.educba.com/python-print-table/)
- [pypi.org](https://pypi.org/project/tabulate/)
- [kaggle.com](https://www.kaggle.com/discussions/general/273188)
