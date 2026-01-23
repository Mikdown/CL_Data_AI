def calculate_total_sales(filename):

import csv

class SalesAnalyzer:
	"""
	A class to analyze sales data from a CSV file.
    
	Attributes:
		filename (str): The path to the sales data CSV file.
		data (list): List of sales records loaded from the CSV file.
	"""
	def __init__(self, filename: str):
		"""
		Initialize the SalesAnalyzer with the given filename.
		Args:
			filename (str): Path to the sales data CSV file.
		"""
		self.filename = filename
		self.data = []

	def load_data(self) -> None:
		"""
		Load sales data from the CSV file into the data attribute.
		Assumes the CSV has 'product_name', 'price', and 'quantity' columns.
		"""
		with open(self.filename, mode='r') as file:
			csv_reader = csv.DictReader(file)
			self.data = [row for row in csv_reader]

	def calculate_total_sales(self) -> float:
		"""
		Calculate the total sales from the loaded data.
		Returns:
			float: The total sales value.
		"""
		total = 0.0
		for row in self.data:
			price = float(row['price'])
			quantity = int(row['quantity'])
			total += price * quantity
		return total

	def find_top_product(self) -> str:
		"""
		Find the product with the highest total sales (price * quantity).
		Returns:
			str: The name of the top-selling product.
		"""
		top_product = None
		top_sales = 0.0
		for row in self.data:
			sales = float(row['price']) * int(row['quantity'])
			if sales > top_sales:
				top_sales = sales
				top_product = row['product_name']
		return top_product


if __name__ == "__main__":
	sales_data_file = 'sales_data.csv'
	analyzer = SalesAnalyzer(sales_data_file)
	analyzer.load_data()
	total_sales = analyzer.calculate_total_sales()
	top_product = analyzer.find_top_product()
	print(f"Total sales from {sales_data_file}: ${total_sales:.2f}")
	print(f"Top-selling product: {top_product}")
