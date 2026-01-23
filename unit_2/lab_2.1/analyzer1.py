# Add a function to identify the top-selling product by total revenue
from typing import List, Dict, Any, Optional

def get_top_selling_product(sales_data: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """
    Identifies the top-selling product by total revenue (price * quantity).
    Args:
        sales_data: List of sales records, each a dict with at least 'product', 'price', and 'quantity' keys.
    Returns:
        The sales record (dict) for the product with the highest total revenue, or None if input is empty.
    """
    if not sales_data:
        return None
    revenue_by_product = {}
    for record in sales_data:
        product = record.get('product')
        price = float(record.get('price', 0))
        quantity = int(record.get('quantity', 0))
        revenue = price * quantity
        if product in revenue_by_product:
            revenue_by_product[product]['revenue'] += revenue
            revenue_by_product[product]['quantity'] += quantity
        else:
            revenue_by_product[product] = {
                'product': product,
                'revenue': revenue,
                'quantity': quantity
            }
    # Find the product with the highest revenue
    top_product = max(revenue_by_product.values(), key=lambda x: x['revenue'])
    return top_product
import csv

def calculate_total_sales(filename):
    """
    Reads a CSV file and calculates the total sales.

    Assumes the CSV has 'product_name', 'price', 'quantity' columns.

    Args:
        filename (str): Path to the CSV file.

    Returns:
        float: Total sales amount.
    """
    total = 0.0
    try:
        with open(filename, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                try:
                    price = float(row['price'])
                    quantity = int(row['quantity'])
                    total += price * quantity
                except ValueError as ve:
                    print(f"Invalid data in row {row}: {ve}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0.0
    return total

if __name__ == "__main__":
    sales_data_file = 'sales_data.csv'
    total_sales = calculate_total_sales(sales_data_file)
    print(f"Total sales from {sales_data_file}: ${total_sales:.2f}")

    # Load sales data from CSV for top-selling product analysis
    sales_data = []
    try:
        with open(sales_data_file, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                sales_data.append(row)
    except FileNotFoundError:
        print(f"Error: File '{sales_data_file}' not found.")
        sales_data = []

    top_product = get_top_selling_product(sales_data)
    if top_product:
        print("\nTop-Selling Product by Total Revenue:")
        print(f"  Product: {top_product['product']}")
        print(f"  Total Revenue: ${top_product['revenue']:.2f}")
        print(f"  Total Quantity Sold: {top_product['quantity']}")
    else:
        print("No sales data available to determine top-selling product.")


