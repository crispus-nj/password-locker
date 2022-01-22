from user import User

class Creditials:
    '''
    '''
    allUser = User.user
    def __init__(self):
        pass
    
    def login(self, username: str, password):
        '''
        Login function will be used to authenticate the user. 
        use the saved credials and allow the user to login the appliaction
        '''
        for user in User.disply_user_accounts():
            if user.username == username and user.password == password:
                success = f"{username} have successfully logged in the application"
                return success
            else :
                error = f"No such username:({username}) found in the application or wrong password."
                return error    
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
print(new_creditials.login("engineer", "1234"))