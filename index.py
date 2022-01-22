from user import User
from creditials import Creditials

def user_instance():
    first_name = input("Enter your First name\n")
    last_name = input("Enter your Last name\n")
    username = input("Enter your username\n")
    password = input("Enter your Your password\n")

    new_user = User(first_name, last_name, username, password)
    new_user.save_user()

def main():
    print("\n")
    print("Welcome to Password Locker Applictation. \n")
    User.generate_menu()

    choice = int(input("Enter a value:\n"))

    while True:
        if choice == 1 :
            print("***CREATE AN ACCOUNT***")
            # first_name = input("Enter your First name\n")
            # last_name = input("Enter your Last name\n")
            # username = input("Enter your username\n")
            # password = input("Enter your Your password\n")
            # User(first_name, last_name, username, password)
            user_instance()
            print("ACCOUNT CREATED!!")
            User.generate_menu_after_login()
            while True:
                choice = int(input("Enter a value:\n"))
                if choice == 1:
                    User.delete_user_account()
                    print("ACCOUNT DELETED SUCCESSFULLY!!")
                    break
                elif choice == 2:
                    print("Details of the available users!!")
                    Creditials.generate_all_saved_accounts()
                    break
                elif choice == 3:
                    User.generate_menu()
                    choice = int(input("Enter a value:\n"))
                    break

        elif choice == 2: 
            print("***LOGIN TO THE ACCOUNT***")
            username = input("Enter your username\n")
            password = input("Enter your Your password\n")
            for userData in User.disply_user_accounts():
                print(username)
                if userData.username == username and userData.password == password:
                    print(f"{username} is successfully logged in!!\n")
                    User.generate_menu_after_login()
                    choice = int(input("Enter a value:\n"))
                    while True:
                        if choice == 1:
                            # new_user = User(username, password)
                            # new_user.delete_user_account()
                            print("ACCOUNT DELETED SUCCESSFULLY!!\n")
                            break
                        elif choice == 2:
                            print("***YOUR ACCOUNT DATA***")
                            Creditials.generate_all_saved_accounts()
                            break
                        elif choice == 3:
                            User.generate_menu()
                            choice = int(input("Enter a value:\n"))

                else :
                    print(f"No such username:({username}) found in the application. Please create an account or check your password!\n")
                    User.generate_menu()
                    choice = int(input("Enter a value:\n"))

        elif choice == 3:
            print("***GET YOUR ACCOUNT DATA***")
            Creditials.generate_all_saved_accounts()
            while True:
                    User.generate_menu()
                    choice = int(input("Enter a value:\n"))
                    break

        elif choice == 4:
            print("***GET YOUR PASSWORD***")
            username = input("Enter your username\n")
            new_username = Creditials()
            print("Your password: "+new_username.password_generate(username)+"\n")
            while True:
                    User.generate_menu()
                    choice = int(input("Enter a value:\n"))
                    break

        elif choice == 5:
            print("***ABOUT THE APPLICATION***")
            print("This is a project which run on a terminal, where a user can create an account with a preferred a username. The application can display various saved accounts. And, lastly the user can delete the account.")
            print("\n")
            while True:
                    User.generate_menu()
                    choice = int(input("Enter a value:\n"))
                    break          

main()