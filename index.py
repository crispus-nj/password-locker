from user import User
from creditials import Creditials

def main():
    User("Crispus", "Njenga", "engineer", "1234")
    print(User.find_user_account("engineer"))

main()