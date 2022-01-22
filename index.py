from user import User
from creditials import Creditials

def main():
    # User("Crispus", "Njenga", "engineer", "1234")
    # print(User.find_user_account("engineer"))
    print("\n")
    print("Welcome to Password Locker Applictation. \n")
    User.generate_menu()

    choice = int(input("Enter a value:\n"))

    while True:
        if choice == 1 :
            print("CREATE AN ACCOUNT")
            first_name = input("Enter your First name\n")
            last_name = input("Enter your Last name\n")
            username = input("Enter your username\n")
            password = input("Enter your Your password\n")
            User(first_name, last_name, username, password)
            print("ACCOUNT CREATED!!")
            User.generate_menu_after_login()
            while True:
                choice = int(input("Enter a value:\n"))
                if choice == 1:
                    new_user = User(first_name, last_name, username, password)
                    new_user.delete_user_account()
                    print("ACCOUNT DELETED SUCCESSFULLY!!")
                elif choice == 2:
                    print("Details of the available users!!")
                    Creditials.generate_all_saved_accounts()
                elif choice == 3:
                    exit()
                    # break
        
        elif choice == 2: 
            username = input("Enter your username\n")
            password = input("Enter your Your password\n")
            for userData in User.disply_user_accounts():
                print(username)
                if userData.username == username and userData.password == password:
                    print(f"{username} is successfully logged in!!")
                    User.generate_menu_after_login()
                    choice = int(input("Enter a value:\n"))
                    while True:
                        if choice == 1:
                            pass
                        elif choice == 2:
                            pass
                        elif choice == 3:
                            exit()
                else :
                    print(f"No such username:({username}) found in the application. Please create an account or check your password!")
                    User.generate_menu()
                    choice = int(input("Enter a value:\n"))

        elif choice == 3:
            Creditials.generate_all_saved_accounts()
            break

                

main()