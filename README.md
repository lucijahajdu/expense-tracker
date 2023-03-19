# Expense Tracker #
## About ##
Exspense Tracker is a good tool to to keep track of your expenses and total money you saved. This expanses tracker is shown in Python terminal and it runs in the Code Institute mock terminal on Heroku.

![Screenshot of the website](/images/main_photo.png)

## Table of Contents ##
* [About](#About)<a name="About"></a>
* [Features](#Features)<a name="Features"></a>
   * [Rules](#Rules)<a name="Rules"></a>
* [Future Features](#Future_Features)<a name="Future Features"></a>
* [Testing](#Testing)<a name="Testing"></a>
* [Bugs](#Bugs)<a name="Bugs"></a>
   * [Fixed bugs](#Fixed_bugs)<a name="Fixed bugs"></a>
   * [Unsolved bugs](#Unsolved_bugs)<a name="Unsolved bugs"></a>
* [Deployment](#Deployment)<a name="Deployment"></a>
   * [Via gitpod](#Via_gitpod)<a name="Via gitpod"></a>
   * [Via Heroku app](#Via_Heroku_app)<a name="Via Heroku app"></a>
* [Credits](#Credits)<a name="Credits"></a>

## User stories ##

* As a user of the expense tracker I want to:
  1. Add a new transaction
  2. View all transactions in one place
  3. Remove an added transaction

  4. Add a new income
  5. View all incomes in one place
  6. Remove an income

  7. View expenses by month
  8. View income by month
  * See total expenses and incomes

## Features ##
Features were developed based on how a user would like to track their expanses and incomes.

### Main Menu ###

![Main menu](/images/menu.png)

This is the first screen that user sees. In the menu area user can select between 8 options.

![View transaction](/images/view_transaction.png)

When option or viewing transaction is selected this screen is visible.

![Transaction by month](/images/View_by_month.png)

To see expenses by month, month needs to be first entered.

### Rules ###
Entering python3 run.py into terminal Welcome message with Menu options are visible.
Options can be choosen entering a number between 1 and 8. If input is invalid error message appears.
Depending on which functions are being used certian rules apply when adding data into the terminal.
* When transaction/income wants to be added, three input fields needs to be filled in:
  * In the first input field, category needs to be added.
  * In the second input field, amount of an expense needs to be added. To add an amount only number value can be used. If not, error message appears.
  * In the last input field, month of the transaction/income needs to be added.
* To view all transactions or incomes option 2 or 5 in the menu needs be entered
* To remove an item user needs to enter 3 or 6 depending if transaction or income is beeing removed. List of already added transaction/income is shown. The approporiate number has to be entered in the input field for removing the desired item.
* To view all transactions/incomes by month option 7 or 8 needs to be entered. After selecting option, correct month needs to be entered. If not, error message appears.
* Total expense/income is always updated after a new item has been added or removed.

## Future Features ##
In future, spreadsheet could be added for more organised visibility of expenses. Additionally financial dashboard with charts to show monthly spending could be created.
In the course of the developement of the software, I was also working on organising the menu area into main and subcategories, so the two main categories would be more distinguished from each other and when searching an item could be easier by the category letter and sub category number. Unitl the deadline of the submission I was not able to develop this without bugs. In the future this feature could be added to my expense tracker as an improvement.


## Testing ##
Folowing tests were done:
* The code was entered into a PEP8 linter where 2 errors occured.
* Invalid inputs were entered into the terminal to trigger errors:
   * When selecting an option from the menu, numbers between 1 and 8 has to be entered. In case of an invalid input, error message with explanaton is shown.
   * When adding amount of transaction/income, number has to be entered. If not, error message informes user of invalid input.
   * When removing transaction/income, the number of the item from the list that needs to be removed is entered. If an inexistent input is entered, error message informs user of invalid input.
   * When viewing transaction/income by month, month needs to be entered with words (e.g.:January). If it is not written in this form, an error message appears to user.
## Bugs ##
### Fixed Bugs ###
* Loop has been added to repeat request that menu options are showed again, after selecting an option in the menu area. Therefore it is not required to write python3 run.py into the terminal repeatedly.
* When I wanted to see all transactions in the list that were previosly adeed, they were not visible. A typo has been found, and the bug was resolved.
* ValueError: could not convert string to float: '13,59'.After correcting ',' to '.' (13.59) bug was resolved.
### Unsolved Bugs ###

![Unsolved bugs](/images/ci_python.png)

When "ValueError" is added next to the "except" then an "IndexError: list assignment index out of range" appears.

## Deployment ##

### Via gitpod ###
+ Repository in Github was created and named expense-tracker. The Code-Institute-Org/python-essentials-template was used.
+ Tapping on the green "gitpod" button Gitpod is open. 
+ To run Python type: python3 -run.py.
+ To save our code type git add ., git commit -m "" and git push to push our code to the GitHub
### Via Heroku app ###
+ Reposotory first needs to be forked
+ Create a new Heroku app
+ Set the buildback to Python and NodeJS in that order
+ Link the Heroku app to the repository
+ Click on Deploy

## Credits ##

### Content ###

+ [This link](https://www.youtube.com/watch?v=-adT3bRWchI"On_this_link") was used to gain ideas for my project.

### External sources ###

+ [Stack Overflow](https://stackoverflow.com/ "Stack_Overflow")
+ [W3School](https://www.w3schools.com/ "W3School")

### Aknowledgement ###
+ I would like to thank to my mentor Richard for supporting me with his patience, valuable input and feedback during this project.





 
