import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.auth import Auth

# Simulated user database
users_db = {'admin': 'password123', 'user1': 'mypassword'}

# Initialize the Auth class
auth = Auth(users_db)

# Test login and logout
auth.login('admin', 'password123')
auth.logout()
