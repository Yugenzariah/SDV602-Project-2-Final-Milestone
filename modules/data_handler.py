import matplotlib.pyplot as plt
import pandas as pd

class DataHandler:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = pd.DataFrame()

    def load_data(self):
        """Loads data from a CSV file."""
        try:
            self.data = pd.read_csv(self.data_path)
            print("Data loaded successfully")
        except Exception as e:
            print(f"Failed to load data: {e}")

    def merge_data(self, new_data_path):
        """Merges new data with existing data, removing duplicates."""
        try:
            new_data = pd.read_csv(new_data_path)
            self.data = pd.concat([self.data, new_data]).drop_duplicates().reset_index(drop=True)
            print("Data merged successfully")
        except Exception as e:
            print(f"Failed to merge data: {e}")

    def display_graph(self, column_x, column_y):
        """Displays a basic line graph for specified columns."""
        if self.data.empty:
            print("No data to display")
            return
        self.data.plot(x=column_x, y=column_y, kind='line')
        plt.title(f"{column_y} over {column_x}")
        plt.xlabel(column_x)
        plt.ylabel(column_y)
        plt.show()
