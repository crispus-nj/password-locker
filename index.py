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
                    pass
                elif choice == 2:
                    pass
                elif choice == 3:
                    exit()
                    break
                

main()