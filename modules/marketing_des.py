import pandas as pd
import matplotlib.pyplot as plt
import requests

class MarketingDES:
    def __init__(self):
        self.data = pd.DataFrame()

    def load_data(self):
        """Loads data from a local CSV file."""
        try:
            self.data = pd.read_csv('data/marketing_data.csv')
            print("Local marketing data loaded successfully")
        except Exception as e:
            print(f"Failed to load local marketing data: {e}")

    def load_remote_data(self):
        """Fetches remote data from an API and loads it into a DataFrame."""
        try:
            response = requests.get("https://jsonplaceholder.typicode.com/posts")
            response.raise_for_status()
            data = response.json()
            self.data = pd.DataFrame(data)[['id', 'title']]
            print("Remote marketing data loaded successfully")
        except Exception as e:
            print(f"Failed to load remote marketing data: {e}")

    def display_graph(self, data_source="local"):
        """Displays a bar chart based on the loaded data with a label for local or remote data."""
        if self.data.empty:
            print("No data to display")
            return
        if data_source == "local":
            # Plot for local marketing data
            self.data.plot(x='Date', y='Engagement', kind='line')
            plt.title("Local Marketing Data Over Time")
            plt.xlabel("Date")
            plt.ylabel("Engagement")
        else:
            # Plot for remote marketing data
            self.data['title_length'] = self.data['title'].apply(len)
            self.data.plot(x='id', y='title_length', kind='bar')
            plt.title("Remote Marketing Data (Title Lengths)")
            plt.xlabel("Post ID")
            plt.ylabel("Title Length")
        plt.show()