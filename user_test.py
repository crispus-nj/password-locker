import unittest # module for testing 
from user import User

class TestUser(unittest.TestCase):
    '''
    Testuser forn testing user cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases
        '''
        self.new_user = User("Crispus", "njenga", "engineer", "1234")

    def tearDown(self):
        '''
        tear down function for clearing the list after every test
        '''
        User.user = []
    def test_init(self):
        '''
        test_init test the instances of user class before each test runs
        '''    
        self.assertEqual(self.new_user.first_name, "Crispus")
        self.assertEqual(self.new_user.last_name, "njenga")
        self.assertEqual(self.new_user.username, "engineer")
        self.assertEqual(self.new_user.password, "1234")

    def test_save_user(self):
        '''
        test_save_user case to test if the user object is saved into
        the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user), 2)


if __name__ == '__main__':
    unittest.main()