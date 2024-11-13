import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.data_handler import DataHandler

# Initialize DataHandler with sample data
data_handler = DataHandler('data/sales_data.csv')
data_handler.load_data()

# Display a graph
data_handler.display_graph('Date', 'Sales')