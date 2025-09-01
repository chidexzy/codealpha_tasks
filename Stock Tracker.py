import csv
from datetime import datetime

def get_stock_prices():
    """Return hardcoded stock prices"""
    return {
        "AAPL": 175,   # Apple
        "GOOG": 2800,  # Google
        "TSLA": 750,   # Tesla
        "AMZN": 3400,  # Amazon
        "MSFT": 300    # Microsoft
    }

def display_available_stocks(stock_prices):
    """Display available stocks and their prices"""
    print("\n" + "="*40)
    print("Available Stocks and Prices:")
    print("="*40)
    for stock, price in stock_prices.items():
        print(f"{stock:6}: ${price:,}")
    print("="*40)

def get_valid_stock(stock_prices):
    """Get a valid stock symbol from user"""
    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()
        if stock == "DONE":
            return None
        if stock in stock_prices:
            return stock
        print(f"Invalid stock symbol '{stock}'. Please choose from: {', '.join(stock_prices.keys())}")

def get_valid_quantity():
    """Get a valid quantity from user"""
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity must be a positive number.")
                continue
            return quantity
        except ValueError:
            print("Please enter a valid whole number.")

def format_currency(amount):
    """Format currency with commas"""
    return f"${amount:,.2f}"

def display_portfolio(portfolio, stock_prices):
    """Display the user's portfolio in a formatted table"""
    if not portfolio:
        print("\nYour portfolio is empty.")
        return 0
    
    print("\n" + "="*60)
    print("YOUR PORTFOLIO")
    print("="*60)
    print(f"{'Stock':<8} {'Quantity':<12} {'Price':<12} {'Total Value':<15}")
    print("-" * 60)
    
    total_investment = 0
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total_investment += value
        print(f"{stock:<8} {qty:<12} {format_currency(price):<12} {format_currency(value):<15}")
    
    print("-" * 60)
    print(f"{'TOTAL':<33} {format_currency(total_investment):<15}")
    print("="*60)
    
    return total_investment

def get_save_preference():
    """Ask user if they want to save and get file preferences"""
    while True:
        save_choice = input("\nSave results to file? (y/n): ").lower().strip()
        if save_choice in ['y', 'yes']:
            return True
        elif save_choice in ['n', 'no']:
            return False
        print("Please enter 'y' for yes or 'n' for no.")

def get_file_type():
    """Get preferred file type from user"""
    while True:
        file_type = input("Save as .txt or .csv? ").lower().strip()
        if file_type in ['txt', 'csv']:
            return file_type
        print("Please enter 'txt' or 'csv'.")

def save_to_txt(portfolio, stock_prices, total_investment, filename="portfolio.txt"):
    """Save portfolio to text file"""
    try:
        with open(filename, "w") as f:
            f.write(f"Portfolio Report - Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*60 + "\n\n")
            f.write(f"{'Stock':<8} {'Quantity':<12} {'Price':<12} {'Total Value':<15}\n")
            f.write("-" * 60 + "\n")
            
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                value = price * qty
                f.write(f"{stock:<8} {qty:<12} {format_currency(price):<12} {format_currency(value):<15}\n")
            
            f.write("-" * 60 + "\n")
            f.write(f"{'TOTAL':<33} {format_currency(total_investment):<15}\n")
        
        print(f"Successfully saved as {filename}")
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False

def save_to_csv(portfolio, stock_prices, total_investment, filename="portfolio.csv"):
    """Save portfolio to CSV file"""
    try:
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([f"Portfolio Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"])
            writer.writerow([])  # Empty row
            writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
            
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                value = price * qty
                writer.writerow([stock, qty, price, value])
            
            writer.writerow([])  # Empty row
            writer.writerow(["TOTAL", "", "", total_investment])
        
        print(f"Successfully saved as {filename}")
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False

def stock_tracker():
    """Main stock tracker function"""
    print("Welcome to Stock Portfolio Tracker!")
    
    stock_prices = get_stock_prices()
    portfolio = {}
    
    display_available_stocks(stock_prices)
    
    # Stock input loop
    while True:
        stock = get_valid_stock(stock_prices)
        if stock is None:  # User typed 'done'
            break
        
        print(f"Current price of {stock}: {format_currency(stock_prices[stock])}")
        quantity = get_valid_quantity()
        
        # Add to portfolio (accumulate if stock already exists)
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        
        current_value = stock_prices[stock] * quantity
        print(f"Added {quantity} shares of {stock} (${format_currency(current_value)})")
        
        # Ask if user wants to add more stocks
        if portfolio:
            continue_choice = input("Add another stock? (y/n): ").lower().strip()
            if continue_choice not in ['y', 'yes']:
                break
    
    # Display final portfolio
    total_investment = display_portfolio(portfolio, stock_prices)
    
    if not portfolio:
        print("No stocks added to portfolio.")
        return
    
    # Save options
    if get_save_preference():
        file_type = get_file_type()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if file_type == "txt":
            filename = f"portfolio_{timestamp}.txt"
            save_to_txt(portfolio, stock_prices, total_investment, filename)
        else:  # csv
            filename = f"portfolio_{timestamp}.csv"
            save_to_csv(portfolio, stock_prices, total_investment, filename)

if __name__ == "__main__":
    stock_tracker()