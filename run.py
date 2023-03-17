expenses = [{'amount': '43.00', 'category': 'travel', 'month':'February'}, {'amount' : '13,59', 'category': 'groceries', 'month':'March'}]
incomes = [{'amount': '1500.53', 'category': 'salary', 'month':'February'}, {'amount' : '600.50', 'category': 'salary', 'month':'March'}]


def add_expense(amount, category, month):
    """
    Adds a new expense to the list
    """
    expense = {'amount': amount, 'category': category, 'month': month}
    expenses.append(expense)  


def print_welcome():
    """
    Welcome message
    """
    print('\nWelcome to Expense Tracker.')
    print_menu()

def calculate_total_expenses():
    """
    Calculates the total expenses
    """
    total = 0
    for expense in expenses:
        total += float(expense['amount'])
    return total


def calculate_total_income():
    """
    Calculates the total income
    """
    total = 0
    for income in incomes:
        total += float(income['amount'])
    return total

def print_menu():
    """
    Menu area to choose an option
    """
    total = calculate_total_expenses()
    income_total = calculate_total_income()

    print('----- Menu -----')
    print('1. Add a new transaction')
    print('2. View all transaction')
    print('3. Remove a transaction\n')
    print('4. Add an income')
    print('5. View all incomes.')
    print('6. Remove an income.\n ')
    print('Total expenses: €', total)
    print('Total income: €', income_total)
    print('difference: €', income_total - total)

    selection = input('Please choose an option: ')
   
    if (selection == '1'):
        category = input('\n Enter exspense category: ')
        amount = float(input('\nEnter the expense amount:'))
        month = input('\n Enter the month of the exspense: ')
        
    elif (selection =='2'):
        view_all_transaction()
        print('\n\n')
        input('Press any key to continue.')
        print_menu()
    elif (selection == '3'):
        remove_transaction()
    elif (selection == '4'):
        category = input('\n Enter income category: ')
        amount = input('\n Enter the income amount: ')
        month = input('\n Enter the month of the income: ')
    elif (selection == '5'):
    elif (selection == '6'):
    else:
        print("Invalid option. Please enter a number between 1 and 3.")

def add_transaction():
    """ 
    Adds a new transaction
    """
    complete = False
    while not complete:
        category = input('\n Enter expense category: ')
        amount = input('\n Enter the expense amount: ')
        if isfloat(amount):
            amount = float(amount)
            complete = True
            month = input('\n Enter the month of the expenses: ')
            add_expense(amount, category, month)
            print_menu()
        else:
            print('Invalid input. Please try again.')
            continue

def view_all_transaction():
    print('\nHere is a view of all transactions.')
    print("------------------------------------")
    counter = 0
    for expense in expenses:
        print(counter, " - ", expense['amount'], " - ", expense['category']," - ", expense['month'])
        counter += 1
    print('\n\n')


def remove_transaction():
    while True:
        view_all_transaction()
    
        try:
            remove = int(input('Remove transaction: '))
            del expenses[remove]
            break
        except:
            print('Invalid input. Please try again.')
        return False
    


print_welcome()



