import tkinter as tk
from tkinter import messagebox
from modules.auth import Auth
from modules.data_handler import DataHandler

# Sample user database for testing
users_db = {'admin': 'password123', 'user1': 'mypassword'}

# Initialize the Auth class
auth = Auth(users_db)

# Path to the sample data file
data_path = 'data/sales_data.csv'

# Function to start the main application after login
def start_main_app():
    print("Main application started!")
    
    # Initialize DataHandler with the data file path
    data_handler = DataHandler(data_path)
    
    # Load data and display the graph
    data_handler.load_data()
    data_handler.display_graph('Date', 'Sales') 

# Function to handle the login process
def handle_login():
    username = entry_username.get()
    password = entry_password.get()
    if auth.login(username, password):
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
        root.destroy()  # Close the login window on successful login
        start_main_app()  # Now this will work because start_main_app is defined
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Set up the tkinter window for login
root = tk.Tk()
root.title("Login")
root.geometry("400x200")

# Username label and entry
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Password label and entry
label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")  # Show * for password input
entry_password.pack(pady=5)

# Login button
login_button = tk.Button(root, text="Login", command=handle_login)
login_button.pack(pady=10)

# Run the tkinter main loop
root.mainloop()