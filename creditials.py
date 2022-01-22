from user import User

class Creditials:
    '''
    '''
    allUser = User.user
    def __init__(self) -> None:
        pass
    
    def login(self):
        '''
        '''
            
        # print(User.disply_user_accounts())

    def password_generate(self, name):
        '''
        generate password will generate the user password. 
        args:
            name: will receive one parameter of username;
        method: 
            will compare. if the username matches the one in the list then the function will display the users password.    
        '''
        for user in User.disply_user_accounts():
            if user.username == name:
                return user.password
            else :
                error = f"No such {name} found!!"
                return error
    

new_creditials = Creditials()
print(new_creditials.password_generate("enginer"))