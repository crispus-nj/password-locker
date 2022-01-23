from user import User
from creditials import Creditials

new_user1 = User.user


def user_instance():
    '''
    user_instance function will create an instance of user. when a user creates an account this function saves the user information into the list
    '''
    first_name = input("Enter your First name\n")
    last_name = input("Enter your Last name\n")
    username = input("Enter your username\n")
    password = input("Enter your Your password\n")

    new_user = User(first_name, last_name, username, password)
    new_user.save_user()
    new_user1.append(new_user)


def main():
    print("\n")
    print("Welcome to Password Locker Applictation. \n")
    User.generate_menu()

    choice = int(input("Enter a value:\n"))

    while True:
        # User.generate_menu()
        if choice == 1:
            print("***CREATE AN ACCOUNT***")
            user_instance()
            print("ACCOUNT CREATED!!")
            User.generate_menu_after_login()
            choice_creation = int(input("Enter a value:\n"))
            while True:
                if choice_creation == 1:
                    User.delete_user_account()
                    # new_user1.remove(new)
                    print("ACCOUNT DELETED SUCCESSFULLY!!")
                    User.generate_menu()
                    choice = int(input("Enter a value:\n"))
                    break
                elif choice_creation == 2:
                    # print("Details of the available users!!")
                    Creditials.generate_all_saved_accounts()
                    # User.generate_menu_after_login()
                    User.generate_menu()
                    choice = int(input("Enter a value:\n"))
                    break
                elif choice_creation == 3:
                    User.generate_menu()
                    choice = int(input("Enter a value:\n"))
                    break

        elif choice == 2:
            print("***LOGIN TO THE ACCOUNT***")
            username = input("Enter your username\n")
            password = input("Enter your Your password\n")
            for userData in User.disply_user_accounts():
                if userData.username == username and userData.password == password:
                    print(f"{username} is successfully logged in!!\n")
                    User.generate_menu_after_login()
                    choice_login = int(input("Enter a value:\n"))
                    while True:
                        if choice_login == 1:
                            User.delete_user_account()
                            print("ACCOUNT DELETED SUCCESSFULLY!!\n")
                            User.generate_menu()
                            choice = int(input("Enter a value:\n"))
                            break
                        elif choice_login == 2:
                            print("***YOUR ACCOUNT DATA***")
                            Creditials.generate_all_saved_accounts()
                            User.generate_menu()
                            choice = int(input("Enter a value:\n"))
                            break
                        elif choice_login == 3:
                            User.generate_menu()
                            choice = int(input("Enter a value:\n"))
                            break

                else:
                    print(
                        f"No such username:({username}) found in the application. Please create an account or check your password!\n")
                    User.generate_menu()
                    choice = int(input("Enter a value:\n"))
                    break

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

        elif choice == 6:
            print("\n")
            print("APPLICATION CLOSED...\n***SEE YOU AGAIN***")
            exit()
        else:
            print("###Invalid input...Please check the selection number and try again***")
            User.generate_menu()
            choice = int(input("Enter a value:\n"))


main()
# print(user_instance())
# print(new_user1)
