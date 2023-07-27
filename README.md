# Prepare Result

Prepare Result application is developed with idea for making teachers life easy to make students result in quick and easy manner. A user can use different options to add data of students, calculate results of all students, view student data added or result calculated. Also, the user has option to delete the student data or results calculated and start a fresh. The whole data is stored at backend on a Google Spreadsheet as well. Hence, a user has option to come back later and add more data or directly go and view student data or their results.

![Homepage-Image-AmIResponsible](/assets/images/quizindiahomepage.jpg)

The Prepare Result site is live, the links can be found [HERE](https://sugandhi13.github.io/quiz-india/)

# Table of contents

- [Prepare Result](#prepare-result)
- [Table of contents](#table-of-contents)
- [UX](#ux)
    - [Site Purpose](#site-purpose)
    - [Audience](#audience)
    - [Communication](#communication)
    - [User Goals](#user-goals)
    - [Future Goals](#future-goals)
- [Design](#design)
    - [Text \& Background color](#text--background-color)
- [Features](#features)
  - [Common Features](#common-features)
    - [Languages Used](#languages-used)
    - [Navigation](#navigation)
  - [Home Page](#home-page)
    - [Landing Page](#landing-page)
    - [Quiz Page](#quiz-page)
    - [Results Message](#results-message)
    - [404 Page](#404-page)
- [Testing](#testing)
    - [Manual Testing](#manual-testing)
- [Validator Testing](#validator-testing)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Lighthouse](#lighthouse)
- [Unfixed Bugs](#unfixed-bugs)
- [Libraries \& Programs Used](#libraries--programs-used)
- [Deployment](#deployment)
- [Credits](#credits)
- [Content](#content)

# UX

###  Purpose
The purpose of this application is to store student data (Name and Marks of 5 subjects). Calculate the results using student data added. View student data or the  result calculated. Store data on Google Spreadsheet to keep data for future use. Lastly, if users wishes, he has option to delete all data stored on Google Spreadsheet. 

### Audience
This site designed for school teachers or educational instuations. This site will help them to prepare result of students in quick and esay manner. 

### Communication
The overall design was kept extremely simple on purpose. A user has following options while using this site.
1. **Add New Data:** To add student data like Name and marks in different subject.
2. **Calculate Result:** To calculate the results (Total markes, percentage scored and assign grade as per rules defined) of all students. 
3. **View Student Data:** To view the the student data of all students added by the user.
4. **View Result:** To view the result of all students added by the user.
5. **Clear Existing Data:** To delete student data or student result data.
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

### Navigation

In this application a user has given 6 options upfront mentioned below. There are also some sub menus mentioned below as well.
1. **Add New Data:** To add student data like Name and marks in different subject.
    1. **Add more Student Data:** To add more student data without exiting to previous menu.
    2. **Exit:** To return to previous menu.
2. **Calculate Result:** To calculate the results (Total markes, percentage scored and assign grade as per rules defined) of all students. 
3. **View Student Data:** To view the the student data of all students added by the user.
4. **View Result:** To view the result of all students added by the user.
5. **Clear Existing Data:** To delete student data or student result data.
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
- **Add more Student Data:** A user has to enter '1' if he wishes to enter more student data. If this option is entered then again the same series of question will be asked as mentioned in point 1 above and at the end again the sub menu will populate to reconfirm from user if the user want to add more student data or not.
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

### View Student Data

The user has to enter '3' if the user would like to see the student data. Whole data stored in *student_data* worksheet (Google Spreadsheet) will be displayed in tabular form. 
If there is no data available in *student_data* worksheet then a message will be displayed to user that *"No student data to display!"*.

### View Result

The user has to enter '4' if the user would like to see the student result data. Whole data stored in *student_result* worksheet (Google Spreadsheet) will be displayed in tabular form. 
If there is no data available in *student_result* worksheet then a message will be displayed to user that *"No student result data to display!"*.

### Clear Existing Data

The user has to enter '5' if the user would like to delete any data already stored on Google Spreadsheet. If the user enters this option a sub menu will populate to confirm that which data (Student Data or Student Results Data) the user want's to delete. These options are described below.
1. **Delete Student Data:** The user has to enter '1' if the user would like to delete student data stored on *student_data* worksheet (Google Spreadsheet). If the user enter this option. A confirmation message will populate to user with Warning that once the data is deleted, it cann't be recovered and another confirmation from user will be required to proceed further and actually delete the data.
    1. **Confirm Delete:** The user has to enter '1' to confirm that the data should be deleted. If the user confirms it then the data will be deleted from *student_data* worksheet (Google Spreadsheet) and only headings will remain in *student_data* worksheet (Google Spreadsheet) and a confirmation message will be displayed to user that data has been deleted successfully. If the *student_data* worksheet is already empty then a message will be displayed to user that *No data to delete.*.
    2. **Return to Previous Menu:** A user has to enter '0' to if the user changes its mind and don't want to delete the data. If this option is entered then no further action will be taken and then the user will route back to pervious menu.
2. **Delete Student Result Data:** The user has to enter '1' if the user would like to delete student result data stored on *student_result* worksheet (Google Spreadsheet). If the user enter this option. A confirmation message will populate to user with Warning that once the data is deleted, it cann't be recovered and another confirmation from user will be required to proceed further and actually delete the data.
    1. **Confirm Delete:** The user has to enter '1' to confirm that the data should be deleted. If the user confirms it then the data will be deleted from *student_data* worksheet (Google Spreadsheet) and only headings will remain in *student_data* worksheet (Google Spreadsheet) and a confirmation message will be displayed to user that data has been deleted successfully. If the *student_data* worksheet is already empty then a message will be displayed to user that *No data to delete.*.
    2. **Return to Previous Menu:** A user has to enter '0' to if the user changes its mind and don't want to delete the data. If this option is entered then no further action will be taken and then the user will route back to pervious menu.
3. **Exit:** The user has to enter '0' to return on the previous menu. 

### End the Program

A user has to enter '0' to end the program. If the user enter this option a thank you message *"Thank you! I hope you will visit again :)"* will be displayed and program will end.

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

# Validator Testing

### HTML

No errors were returned when passing through the official W3C validator.

![HTML](/assets/images/w3cvalidator.jpg)

### CSS

No errors were found when passing through the official W3C CSS (Jigsaw) validator.

![css](/assets/images/cssvalidationresults.jpg)

### JavaScript

No errors were found when passing through the official JavaScript (JSHint) validator.

![JavaScript](/assets/images/jshint.jpg)

### Lighthouse

The page achieved great performance on mobile and desktop.

- **Desktop**:
  
  ![Desktop](/assets/images/lighthousereportdesktop.jpg)

- **Mobile**:
  
  ![Mobile](/assets/images/lighthousereportmobile.jpg)

# Unfixed Bugs

I've struggled with alignment all buttons with same width either radio or submit buttons. 

I will try to improve further on this in coming days and considering it as a challenge to handle.

# Libraries & Programs Used

- **Github**: Store Repository
- **Codeanywhere**: Create the html, CSS and JavaScript files
- **Favicon.io** - To create the favicon.
- **Google Chrome Dev Tools**: To aid the initial styling for media queries and testing at various screen sizes
- **Microsoft Edge**: Site testing on an alternative browser
- **Snipping Tool**: To take screenshot for images of various results
- **Am I Responsive**: To ensure website looks good on different devices
- **W3C Validator**: To validate HMTL pages
- **W3C CSS Validator**: To validate CSS
- **JSHint**: To validate JavaScript

# Deployment

The site is deployed to GitHub pages. The steps to deploy are as follows:

- In the GitHub repository, select the quiz-india project from left pane 'Top Repositories' section
- Click on Settings tab in navigation menu.
- Select the 'Pages' tab in the 'Code and Automation' section.
- From the Build and deployment section, go to source and select 'Deploy from a branch' in drop-down menu.
- Next select the 'Main' branch under Branch drow-down menu.
- Once the 'Main' branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.
- The live link for the site can be found here - [/sugandhi13.github.io/quiz-india](https://sugandhi13.github.io/quiz-india/)

# Credits

I have really enjoyed the Code Institute course up till now, and I am looking forward to the next units of the course. I wanted to thank the Slack Community for their support learning the content and my Mentor Martina for her guidance with this project and assurances that creating a website is not as scary as I initially thought.

As a starting point I looked at the Love Maths projects.

- From the Love Maths Project, I took inspiration about how to include JavaScript along with HTML and CSS.
- Friends Trivia Quiz, My mentor has shared the GitHub repository created by Ila Bura. It helped me in great deal to understand and write JavaScripts functions and handle media queries in better way.
- W3School and Stackoverflow, I have referred these website to fix various issue that I faced while writing various types of code (CSS/JavaScript) for the website.

# Content

Following websites have been used as source for quiz questions, answers with multiple options.

- [firstcry.com](https://www.firstcry.com/intelli/articles/50-must-know-gk-questions-about-india-with-answers-for-kids/)
