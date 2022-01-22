class User:
    '''
    User class responsible for handling user functions
    '''
    user = [] # where the user will be stored
    
    # constructor
    def __init__(self, first_name : str, last_name : str, username : str, password : str):
        '''
        constructor function responsible for creation of all user instances
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        User.user.append(self)

    def generate_menu(self):
        '''
        generate menu function is responsible for displaying menu to the user for any function the user is interested in.
        '''
        print("\n")
        print("Welcome to Password Locker Applictation. \n")
        print("1 - Create an Account")
        print("2 - Login to an Account")
        print("3 - Display Account Username")
        print("4 - Display Accounts")
        print("5 - Display Accounts")
        print("6 - Display user password")


    def save_user(self):
        '''
        save user function will be saving the user to the user list
        '''
        User.user.append(self)
    
    def delete_user_account(self):
        '''
        delete user account will perform deleting of a users account
        '''
        User.user.remove(self)

    @classmethod
    def find_user_account(cls, username):
        '''
        find user function responsible for finding the user by username
        Args:
            username: name to search
        Returns :
            the username that matches the name
        '''
        for name in User.user:
            # print(name.username)
            if name.username == username:
                return username

    @classmethod
    def disply_user_accounts(cls):
        '''
        display user accounts returns all the saved user accounts
        '''
        return User.user


new_user = User("Crispus", "Njenga", "engineer", "1234")
# print(new_user.save_user())
# new_user.generate_menu()
# print(User.find_user_account("engineer"))
# print(new_user.save_user())
# print(User.disply_user_accounts())
