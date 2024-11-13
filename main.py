import tkinter as tk
from tkinter import messagebox
from modules.auth import Auth
from modules.sales_des import SalesDES
from modules.marketing_des import MarketingDES
from modules.product_des import ProductDES
from modules.chat import Chat

# User database for authentication
users_db = {'admin': 'password123', 'user1': 'mypassword'}

# Initialize the Auth class
auth = Auth(users_db)

# Function to start the chat window
def start_chat_window():
    chat = Chat()
    chat_window = tk.Tk()
    chat_window.title("Chat")

    # Chat display area
    chat_display = tk.scrolledtext.ScrolledText(chat_window, state="disabled", width=50, height=15)
    chat_display.pack()

    # Function to refresh chat display
    def refresh_chat():
        chat_display.config(state="normal")
        chat_display.delete(1.0, tk.END)
        chat_display.insert(tk.END, chat.load_chat())
        chat_display.config(state="disabled")

    # Entry for typing messages
    message_entry = tk.Entry(chat_window, width=50)
    message_entry.pack()

    # Send button to send message
    def send_message():
        message = message_entry.get()
        if message:
            chat.send_message(message)
            message_entry.delete(0, tk.END)
            refresh_chat()

    send_button = tk.Button(chat_window, text="Send", command=send_message)
    send_button.pack()

    # Refresh chat every few seconds
    chat_window.after(2000, refresh_chat)

    chat_window.mainloop()

# Function to start the main application after login
def start_main_app():
    print("Main application started!")

    # Initialize DES instances
    sales_des = SalesDES()
    marketing_des = MarketingDES()
    product_des = ProductDES()

    # Load initial data for each DES
    sales_des.load_data()
    marketing_des.load_data()
    product_des.load_data()

    # Functions to show each DES with either local or remote data
    def show_local_sales():
        sales_des.display_graph(data_source="local")

    def show_remote_sales():
        sales_des.load_remote_data()
        sales_des.display_graph(data_source="remote")

    def show_local_marketing():
        marketing_des.display_graph(data_source="local")

    def show_remote_marketing():
        marketing_des.load_remote_data()
        marketing_des.display_graph(data_source="remote")

    def show_local_product():
        product_des.display_graph(data_source="local")

    def show_remote_product():
        product_des.load_remote_data()
        product_des.display_graph(data_source="remote")

    # Main application window with buttons for each DES and chat
    app_window = tk.Tk()
    app_window.title("Data Explorer Screen")

    # Application buttons
    tk.Button(app_window, text="View Local Sales DES", command=show_local_sales).pack(pady=5)
    tk.Button(app_window, text="View Remote Sales DES", command=show_remote_sales).pack(pady=5)
    tk.Button(app_window, text="View Local Marketing DES", command=show_local_marketing).pack(pady=5)
    tk.Button(app_window, text="View Remote Marketing DES", command=show_remote_marketing).pack(pady=5)
    tk.Button(app_window, text="View Local Product DES", command=show_local_product).pack(pady=5)
    tk.Button(app_window, text="View Remote Product DES", command=show_remote_product).pack(pady=5)
    tk.Button(app_window, text="Open Chat", command=start_chat_window).pack(pady=10)

    app_window.mainloop()

# Function to handle the login process
def handle_login():
    username = entry_username.get()
    password = entry_password.get()
    if auth.login(username, password):
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
        root.destroy()
        start_main_app() 
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Set up the tkinter window for login
root = tk.Tk()
root.title("Login")
root.geometry("300x200")

# Username label and entry
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Password label and entry
label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*") 
entry_password.pack(pady=5)

# Login button
login_button = tk.Button(root, text="Login", command=handle_login)
login_button.pack(pady=10)

# Run the tkinter main loop
root.mainloop()