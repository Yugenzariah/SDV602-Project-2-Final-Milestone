class Auth:
    def __init__(self, users_db):
        # Simulating a user database as a dictionary
        self.users_db = users_db
        self.logged_in_user = None

    def login(self, username, password):
        """Attempts to log in the user."""
        if username in self.users_db and self.users_db[username] == password:
            self.logged_in_user = username
            print(f"Login successful for {username}")
            return True
        else:
            print("Login failed")
            return False

    def logout(self):
        """Logs out the currently logged-in user."""
        if self.logged_in_user:
            print(f"Logging out {self.logged_in_user}")
            self.logged_in_user = None
        else:
            print("No user is currently logged in")