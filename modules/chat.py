import tkinter as tk
from tkinter import scrolledtext

class Chat:
    def __init__(self, chat_file="chat_log.txt"):
        self.chat_file = chat_file

    def send_message(self, message):
        """Saves a new message to the chat log."""
        with open(self.chat_file, "a") as file:
            file.write(f"{message}\n")

    def load_chat(self):
        """Loads chat messages from the log file."""
        with open(self.chat_file, "r") as file:
            return file.read()