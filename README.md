# Expense Tracker #
## About ##
Exspense Tracker is a good tool to to keep track of your expenses and total money you saved. This expanses tracker is shown in Python terminal and it runs in the Code Institute mock terminal on Heroku.

## Table of Contents ##
* [About](#About)<a name="About"></a>
* [Features](#Features)<a name="Features"></a>
   * [Rules](#Rules)<a name="Rules"></a>
* [Future Features](#Future_Features)<a name="Future Features"></a>


## Features ##
Features were developed based on how a user would like to track their expanses and incomes.

* As a user of the expense tracker I want to:
  1. Add a new transaction
  2. View all transactions in one place
  3. Remove an added transaction
  4. Add a new income
  5. View all incomes in one place
  6. Remove an income
  * See total expenses and incomes

### Rules ###
Entering python3 run.py into terminal Welcome message with Menu options are visible.
Options can be choosen entering a number between 1 and 6. If input is invalid error message appears.
Depending on which functions are being used certian rules apply when adding data into the terminal.
* When transaction/income wants to be added, three input fields needs to be filled in:
  * In the first input field, category needs to be added.
  * In the second input field, amount of an expense needs to be added. To add an amount only number value can be used. If not, error message appears.
  * In the last input field, month of the transaction/income needs to be added.
* To view all transactions or incomes option 2 or 5 in the menu needs be entered
* To remove an item user needs to enter 3 or 6 depending if transaction or income is beeing removed. List of already added transaction/income is shown. The approporiate number has to be entered in the input field for removing the desired item.
* Total expense/income is always updated after a new item has been added or removed.

## Future Features ##
In future, spreadsheet could be added for more organised visibility of expenses. Additionally financial dashboard with charts to show monthly spending could be created.

## Testing ##
Folowing tests were done:
* The code passed through a PEP8 linter
* Invalid inputs were entered into the terminal to trigger errors:
   * When selecting an option from the menu, numbers between 1 and 6 has to be entered. In case of an invalid input, error message with explanaton is shown.
   * When adding amount of transaction/income, number has to be entered. If not, error message informes user of invalid input.
   * When removing transaction/income, the number of the item from the list that needs to be removed is entered. If an inexistent input is entered, error message informs user of invalid input.

## Bugs ##
### Fixed Bugs ###
* Loop has been added to repeat request that menu options are showed again, after selecting an option in the menu area. Therefore it is not required to write python3 run.py into the terminal repeatedly.
* When I wanted to see all transactions in the list that were previosly adeed, they were not visible. A typo has been found, and the bug was resolved.
* ValueError: could not convert string to float: '13,59'.After correcting ',' to '.' (13.59) bug was resolved.
## Deployment ##

### Via gitpod ###
+ Repository in Github was created and named expense-tracker. The Code-Institute-Org/python-essentials-template was used.
+ Tapping on the green "gitpod" button Gitpod is open. 
+ To run Python type: python3 -run.py.
+ To save our code type git add ., git commit -m "" and git push to push our code to the GitHub
### Via Heroku app###
+ Reposotory first needs to be forked
+ Create a new Heroku app
+ Set the buildback to Python and NodeJS in that order
+ Link the Heroku app to the repository
+ Click on Deploy

## Credits ##




 
