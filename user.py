class User:
    '''
    User class responsible for handling user functions
    '''
    def __init__(self):
        '''
        constructor function responsible for creation of all user instances
        '''
    def generate_menu(self):
        '''
        generate menu function is responsible for displaying menu to the user for any function the user is interested in.
        '''
        print("Welcome to Password Locker Applictation. \n")
        print("1 - Create an Account")
        print("2 - Login to an Account")
        print("3 - Display Account Username")
        print("4 - Display Accounts")
        print("5 - Delete an Account")

new_user = User()
new_user.generate_menu()
