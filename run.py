expenses = []
expense1 = {'amount': '43.00', 'category': 'travel', 'month':'February'}
expenses.append(expense1)
expense2 = {'amount' : '13,59', 'category': 'groceries', 'month':'March'}
expenses.append(expense2)


def print_menu():
    """
    Menu area to chose an option
    """
    print('----- Menu -----')
    print('1. Add a new transaction')
    print('2. View all transaction')
    print('3. View expenses by month')
    print('4. Remove a transaction\n')
    selection = input('Please chose an option: ')

print_menu()