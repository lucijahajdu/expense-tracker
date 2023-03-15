expenses = []
expense1 = {'amount': '43.00', 'category': 'travel', 'month':'February'}
expenses.append(expense1)
expense2 = {'amount' : '13,59', 'category': 'groceries', 'month':'March'}
expenses.append(expense2)

def add_expense(amount, category, month):
    expense = {'amount': amount, 'category': category, 'month': month}
    exspenses.append(expense)  
    

def print_menu():
    """
    Menu area to choose an option
    """

    print('\nWelcome to Expense Tracker.\n')
    print('----- Menu -----')
    print('1. Add a new transaction')
    print('2. View all transaction')
    print('3. Remove a transaction\n')

    selection = input('Please choose an option: ')
   
    
    if (selection == '1'):
        category = input('\n Enter exspense category: ')
        amount = float(input('\nEnter the expense amount:'))
        month = input('\n Enter the month of the exspense: ')
        
    elif (selection =='2'):
        view_all_transaction()
    elif (selection == '3'):
        remove_transaction()
    else:
        print("Invalid option. Please enter a number between 1 and 3.")

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
    




print_menu()
